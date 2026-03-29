#!/bin/bash
# PreToolUse (Write|Edit) — block editing hook/config files
# exit 2 = block, exit 0 = allow

METRICS_DIR="$HOME/.claude/metrics"
METRICS_FILE="$METRICS_DIR/harness.jsonl"

FILE=$(echo "$CLAUDE_TOOL_INPUT" | node -e "let d='';process.stdin.on('data',c=>d+=c);process.stdin.on('end',()=>{try{console.log(JSON.parse(d).file_path||'')}catch{}})" 2>/dev/null)
[ -z "$FILE" ] && exit 0

# Normalize: backslash->forward slash, lowercase (using node to avoid sed issues on Windows)
FILE_NORM=$(node -e "console.log(process.argv[1].split(String.fromCharCode(92)).join('/').toLowerCase())" "$FILE" 2>/dev/null)

BLOCKED=false
REASON=""

if echo "$FILE_NORM" | grep -qE '\.claude/hooks/'; then
  BLOCKED=true
  REASON="hook files are protected"
fi

if echo "$FILE_NORM" | grep -qE '\.claude/settings\.json'; then
  BLOCKED=true
  REASON="settings.json is protected (use /update-config skill)"
fi

if echo "$FILE_NORM" | grep -qE '(lefthook\.yml|\.pre-commit-config\.yaml|\.husky/)'; then
  BLOCKED=true
  REASON="CI/hook config is protected"
fi

if [ "$BLOCKED" = true ]; then
  # Log to harness metrics
  mkdir -p "$METRICS_DIR"
  TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
  echo "{\"timestamp\":\"$TS\",\"hook\":\"pre-edit-guard\",\"action\":\"blocked\",\"file\":\"$FILE\",\"reason\":\"$REASON\"}" >> "$METRICS_FILE"

  echo "{\"hookSpecificOutput\":{\"hookEventName\":\"PreToolUse\",\"additionalContext\":\"BLOCKED: Cannot edit $FILE — $REASON. Edit manually if needed.\"}}" >&2
  exit 2
fi

exit 0
