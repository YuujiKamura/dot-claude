#!/usr/bin/env python3
"""
Pre-commit review hook for Claude Code.
Delegates to review.exe for architecture + security review.

Runs review.exe --hook on staged diff.
For large diffs (>500 lines), extracts added lines only for sensitive data scan via Gemini CLI.
"""
import json
import subprocess
import sys
import os
import re
import shutil
import tempfile
from datetime import datetime, timezone

REVIEW_BIN = os.environ.get("REVIEW_BIN", "C:/Users/yuuji/ai-code-review/target/release/review.exe")
MAX_LINES = int(os.environ.get("REVIEW_MAX_LINES", "500"))
GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
DEBUG = os.environ.get("REVIEW_DEBUG", "").lower() in ("1", "true")

METRICS_DIR = os.path.join(os.path.expanduser("~"), ".claude", "metrics")
METRICS_FILE = os.path.join(METRICS_DIR, "harness.jsonl")

def log_harness(hook, action, **kwargs):
    """Append a JSONL line to harness.jsonl."""
    os.makedirs(METRICS_DIR, exist_ok=True)
    entry = {
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "hook": hook,
        "action": action,
    }
    entry.update(kwargs)
    try:
        with open(METRICS_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except OSError:
        pass

def debug(msg):
    if DEBUG:
        print(f"[DEBUG] {msg}", file=sys.stderr)

def extract_working_dir(command):
    """Extract working directory from cd command."""
    for pattern in [r'cd\s+"([^"]+)"\s*&&', r"cd\s+'([^']+)'\s*&&", r'cd\s+(\S+)\s*&&']:
        match = re.search(pattern, command)
        if match:
            candidate = match.group(1)
            try:
                result = subprocess.run(
                    ["git", "rev-parse", "--show-toplevel"],
                    capture_output=True, timeout=5, cwd=candidate
                )
                if result.returncode == 0:
                    return candidate
            except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
                pass
    return None

def get_staged_diff(cwd=None):
    try:
        result = subprocess.run(
            ["git", "diff", "--cached"],
            capture_output=True, timeout=30, cwd=cwd,
            encoding="utf-8", errors="replace"
        )
        return result.stdout.strip() if result.stdout else ""
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return ""

def get_repo_visibility(cwd=None):
    try:
        result = subprocess.run(
            ["gh", "repo", "view", "--json", "visibility"],
            capture_output=True, timeout=10, cwd=cwd,
            encoding="utf-8", errors="replace"
        )
        if result.returncode == 0 and result.stdout:
            return json.loads(result.stdout).get("visibility", "UNKNOWN")
    except (subprocess.TimeoutExpired, FileNotFoundError, json.JSONDecodeError):
        pass
    return "UNKNOWN"

def run_review_exe(cwd=None):
    """Run review.exe --hook --prompt architecture --context."""
    env = os.environ.copy()
    if cwd:
        env["GIT_WORK_TREE"] = cwd
    try:
        result = subprocess.run(
            [REVIEW_BIN, "--hook", "--prompt", "architecture", "--context"],
            capture_output=True, timeout=120, cwd=cwd
        )
        # review.exe outputs to stderr; decode with UTF-8 first, cp932 fallback
        try:
            output = result.stderr.decode("utf-8").strip()
        except UnicodeDecodeError:
            output = result.stderr.decode("cp932", errors="replace").strip()
        return output, result.returncode
    except subprocess.TimeoutExpired:
        return "Warning: Review timeout (120s) -- continuing without blocking", 3
    except FileNotFoundError:
        return f"Warning: review.exe not found at: {REVIEW_BIN}", 1

def run_sensitive_data_scan(diff, visibility, cwd=None):
    """For large diffs, extract added lines and scan for sensitive data via Gemini."""
    added = []
    for line in diff.split('\n'):
        if line.startswith('+') and not line.startswith('+++'):
            added.append(line[1:])
    if not added:
        return "", 0

    gemini_path = shutil.which("gemini")
    if not gemini_path:
        appdata = os.environ.get("APPDATA", "")
        candidate = os.path.join(appdata, "npm", "gemini.cmd")
        if os.path.exists(candidate):
            gemini_path = candidate
        else:
            return "Warning: Gemini CLI not found for sensitive data scan", 1

    vis_warn = ""
    if visibility == "PUBLIC":
        vis_warn = "\nWARNING: PUBLIC REPOSITORY -- any committed data is visible to the internet.\n"

    prompt = f"""Pre-commit sensitive data scan. Respond LGTM if safe, or BLOCKED quoting the line.
{vis_warn}
Check for: API keys, tokens, passwords, real company/person names,
project-specific dates (e.g. 20260211), real measurement values,
camera file names (e.g. R0010315.JPG), paths with usernames, construction project identifiers.

EXCEPTIONS -- do NOT flag these (standard OSS metadata):
- GitHub/GitLab repository URLs (e.g. github.com/user/repo in Cargo.toml, package.json)
- Copyright notices in LICENSE files (e.g. "Copyright (c) 2026 AuthorName")
- Package author fields, maintainer names in manifest files
- Git dependency URLs (e.g. git = "https://github.com/...")
- crates.io / npm / PyPI package metadata (repository, homepage, documentation URLs)
- Dummy/placeholder usernames in test code (e.g. "testuser", "example_user")
- Paths using obvious placeholder usernames in test assertions

```
{chr(10).join(added)}
```"""

    try:
        with tempfile.TemporaryDirectory() as td:
            pf = os.path.join(td, "prompt.txt")
            with open(pf, "w", encoding="utf-8") as f:
                f.write(prompt)

            if sys.platform == "win32":
                ps = os.path.join(td, "run.ps1")
                with open(ps, "w", encoding="utf-8") as f:
                    f.write(f"$OutputEncoding = [Console]::OutputEncoding = [Text.Encoding]::UTF8\n")
                    f.write(f"Get-Content -Raw -Encoding UTF8 '{pf}' | & '{gemini_path}' -m {GEMINI_MODEL} -o text\n")
                env = os.environ.copy()
                env["PYTHONIOENCODING"] = "utf-8"
                result = subprocess.run(
                    ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", ps],
                    capture_output=True, timeout=120, env=env
                )
                try:
                    output = result.stdout.decode("utf-8").strip()
                except UnicodeDecodeError:
                    output = result.stdout.decode("cp932", errors="replace").strip()
            else:
                with open(pf, "r", encoding="utf-8") as f:
                    content = f.read()
                result = subprocess.run(
                    [gemini_path, "-m", GEMINI_MODEL, "-o", "text"],
                    input=content, capture_output=True, timeout=120, encoding="utf-8"
                )
                output = (result.stdout or "").strip()

            lines = [l for l in output.split('\n')
                     if not l.startswith("Loaded cached") and not l.startswith("Hook registry")]
            output = '\n'.join(lines).strip()
            blocked = 1 if ("BLOCKED" in output or result.returncode != 0) else 0
            return output, blocked
    except Exception as e:
        return f"Warning: Sensitive scan error: {e}", 1

DESTRUCTIVE_PATTERNS = [
    (r'git\s+push\s+.*--force(?:-with-lease)?(?:\s|$)', 'force push is blocked -- use normal push'),
    (r'git\s+reset\s+--hard', 'hard reset is blocked -- use git stash instead'),
    (r'git\s+clean\s+-[a-z]*f', 'git clean -f is blocked -- remove files manually'),
    (r'rm\s+-[a-z]*r[a-z]*f|rm\s+-[a-z]*f[a-z]*r', 'recursive forced remove is blocked -- remove files individually'),
    (r'git\s+checkout\s+--\s+\.', 'git checkout -- . is blocked -- checkout specific files'),
]

def check_destructive(command):
    for pattern, message in DESTRUCTIVE_PATTERNS:
        if re.search(pattern, command):
            print(f'[BLOCKED] {message}', file=sys.stderr)
            return True
    return False

def main():
    debug("Hook started")

    try:
        input_data = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        sys.exit(0)

    if input_data.get("tool_name") != "Bash":
        sys.exit(0)

    command = input_data.get("tool_input", {}).get("command", "")

    # Check destructive commands FIRST (applies to all commands, not just git commit)
    if check_destructive(command):
        log_harness("pre-commit-review", "blocked", command=command[:200], reason="destructive command")
        sys.exit(2)

    if "git commit" not in command:
        sys.exit(0)

    if re.search(r'--no-verify(?:\s|$)', command):
        print("[BLOCKED] --no-verify is not allowed", file=sys.stderr)
        log_harness("pre-commit-review", "blocked", command=command[:200], reason="--no-verify")
        sys.exit(2)

    debug("Detected git commit")

    work_dir = extract_working_dir(command)
    if work_dir is None:
        try:
            result = subprocess.run(
                ["git", "rev-parse", "--show-toplevel"],
                capture_output=True, timeout=5,
                encoding="utf-8", errors="replace"
            )
            if result.returncode == 0 and result.stdout.strip():
                work_dir = result.stdout.strip()
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
    diff = get_staged_diff(cwd=work_dir)
    if not diff:
        sys.exit(0)

    content_line_count = sum(1 for line in diff.split('\n')
                             if (line.startswith('+') and not line.startswith('+++'))
                             or (line.startswith('-') and not line.startswith('---')))
    total_lines = len(diff.split('\n'))
    visibility = get_repo_visibility(cwd=work_dir)

    if content_line_count <= MAX_LINES:
        # Normal size: full architecture + security review via review.exe
        print(f"\n=== Pre-commit Review ({visibility}) ===", file=sys.stderr)
        print(f"review.exe --hook --prompt architecture --context ({content_line_count} content lines / {total_lines} total)\n", file=sys.stderr)

        output, rc = run_review_exe(cwd=work_dir)
        print(output, file=sys.stderr)
        print("\n=== Review Complete ===\n", file=sys.stderr)

        if rc == 3:
            # Timeout: warn but don't block
            log_harness("pre-commit-review", "timeout", lines=content_line_count)
        elif rc != 0:
            print("[BLOCKED] Fix issues above before committing.", file=sys.stderr)
            log_harness("pre-commit-review", "blocked", lines=content_line_count, reason="review failed")
            sys.exit(2)
        else:
            log_harness("pre-commit-review", "passed", lines=content_line_count)
    else:
        # Large diff: sensitive data scan only (architecture review skipped)
        added_count = sum(1 for l in diff.split('\n') if l.startswith('+') and not l.startswith('+++'))
        print(f"\n=== Pre-commit Safety Scan ({visibility}) ===", file=sys.stderr)
        print(f"Large diff ({content_line_count} content lines / {total_lines} total) -- scanning {added_count} added lines for sensitive data\n", file=sys.stderr)

        output, rc = run_sensitive_data_scan(diff, visibility, cwd=work_dir)
        print(output, file=sys.stderr)
        print("\n=== Scan Complete ===\n", file=sys.stderr)

        if rc != 0:
            print("[BLOCKED] Sensitive data detected. Fix before committing.", file=sys.stderr)
            log_harness("pre-commit-review", "blocked", lines=content_line_count, reason="sensitive data")
            sys.exit(2)
        else:
            log_harness("pre-commit-review", "passed", lines=content_line_count, scan_type="sensitive-only")

    sys.exit(0)

if __name__ == "__main__":
    main()
