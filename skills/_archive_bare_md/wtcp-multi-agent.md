---
name: wtcp-multi-agent
description: Use when managing multiple AI agents (Claude/Codex/Gemini) across WT tabs and windows via Control Plane. Triggers on multi-agent, parallel agents, tab management, new tab, switch tab, WT operations, 複数エージェント, タブ追加, ウィンドウ追加
---

# WT Control Plane: Multi-Agent Management

Launch, manage, and orchestrate multiple AI agents across Windows Terminal tabs and windows via the Control Plane named pipe protocol.

## Prerequisites

- Fork WT binary: `~/WindowsTerminal/bin/x64/Debug/WindowsTerminal/WindowsTerminal.exe`
- CP DLL: `control_plane_server.dll` in the same directory
- agent-ctl binary: `~/agent-relay/target/release/agent-ctl.exe` (or debug)
- Hook wrapper: `~/.claude/hooks/agent-deck-hook.sh`
- Hook files: `~/.agent-deck/hooks/`

## Session Discovery

Session files live in `$LOCALAPPDATA/WindowsTerminal/control-plane/winui3/sessions/*.session`. Each contains key=value pairs: `session_name`, `pid`, `hwnd`, `pipe_name`, `pipe_path`, `log_file`.

agent-ctl searches these directories:
- `$LOCALAPPDATA/WindowsTerminal/control-plane/winui3/sessions/`
- `$LOCALAPPDATA/Packages/WindowsTerminalDev_8wekyb3d8bbwe/LocalCache/Local/WindowsTerminal/control-plane/winui3/sessions/`
- `$LOCALAPPDATA/ghostty/control-plane/winui3/sessions/`

Session hint: any substring of session_name. Empty string matches first alive session.

## 1. Launch a Fork WT Window

```bash
WINDOWS_TERMINAL_CONTROL_PLANE=1 ~/WindowsTerminal/bin/x64/Debug/WindowsTerminal/WindowsTerminal.exe &
sleep 8  # wait for CP DLL to create named pipe
```

Or via agent-ctl run (auto-launches if no alive session):
```bash
agent-ctl run --agent claude --task "do something" --exe ~/WindowsTerminal/bin/x64/Debug/WindowsTerminal/WindowsTerminal.exe
```

## 2. Tab Management via agent-ctl

```bash
# List all tabs
agent-ctl tab "" list

# Create a new tab (returns new tab index)
agent-ctl tab "" new

# Switch to tab by index (0-based)
agent-ctl tab "" switch 1

# Close a specific tab
agent-ctl tab "" close 2

# Close active tab (no index)
agent-ctl tab "" close

# List tabs (shortcut)
agent-ctl tabs ""
```

## 3. Protocol Reference (Named Pipe)

Each pipe connection is one request-response then close. The CP DLL is single-connection; rapid-fire requests may fail. Wait 1s between calls if needed.

| Action | Request | Response |
|--------|---------|----------|
| Ping | `PING` | `PONG\|session\|pid\|hwnd` |
| Read active tab | `TAIL\|30` | Raw terminal text (30 lines) |
| Read specific tab | `TAIL\|30\|2` | Raw text from tab index 2 |
| Send text (bracketed paste) | `INPUT\|from\|base64(text)` | `ACK\|session\|pid` |
| Send raw key | `RAW_INPUT\|from\|base64(\r)` | `ACK\|session\|pid` |
| New tab | `NEW_TAB` | Tab info |
| Close tab | `CLOSE_TAB` or `CLOSE_TAB\|index` | Response |
| Switch tab | `SWITCH_TAB\|index` | Response |
| List tabs | `LIST_TABS` | Tab list |
| State (active) | `STATE` | State info |
| State (specific tab) | `STATE\|tab_index` | State info |
| Focus window | `FOCUS` | Response |
| Error | any | `ERR\|session\|message` |

## 4. Raw Pipe Access (PowerShell)

When agent-ctl is not available or for custom automation:

```bash
# Discover session
SESSION=$(ls -t "$LOCALAPPDATA/WindowsTerminal/control-plane/winui3/sessions/"*.session 2>/dev/null | head -1)
PIPE=$(grep "^pipe_path=" "$SESSION" | cut -d= -f2)
PIPE_NAME=$(echo "$PIPE" | sed 's|\\\\\.\\pipe\\||')

# Send a protocol message via PowerShell
send_pipe() {
  local msg="$1"
  powershell.exe -NoProfile -Command "
    \$p = New-Object System.IO.Pipes.NamedPipeClientStream('.','$PIPE_NAME',[System.IO.Pipes.PipeDirection]::InOut)
    \$p.Connect(5000)
    \$sw = New-Object System.IO.StreamWriter(\$p)
    \$sr = New-Object System.IO.StreamReader(\$p)
    \$sw.Write('$msg'); \$sw.Flush(); \$p.WaitForPipeDrain()
    \$resp = \$sr.ReadToEnd(); Write-Output \$resp; \$p.Close()
  "
}

# Examples
send_pipe "PING"
send_pipe "LIST_TABS"
send_pipe "NEW_TAB"
send_pipe "SWITCH_TAB|1"
send_pipe "TAIL|30|0"
```

## 5. Multi-Agent Parallel Setup

Launch 3 agents in separate tabs:

```bash
# Tab 0 already exists (default shell)
# Launch Claude in tab 0
agent-ctl launch "" claude

# Create tab 1 and launch Codex
agent-ctl tab "" new
agent-ctl tab "" switch 1
agent-ctl launch "" codex

# Create tab 2 and launch Gemini
agent-ctl tab "" new
agent-ctl tab "" switch 2
agent-ctl launch "" gemini
```

Or use `agent-ctl run` for the first agent (auto-creates window + launches + sends task):

```bash
# First agent: auto-launch WT + Claude + send task
agent-ctl run --agent claude --task "implement feature X" \
  --exe ~/WindowsTerminal/bin/x64/Debug/WindowsTerminal/WindowsTerminal.exe \
  --stop-at sent

# Second agent in new tab
agent-ctl tab "" new
agent-ctl tab "" switch 1
agent-ctl run --agent codex --task "write tests for feature X" --stop-at sent

# Third agent in new tab
agent-ctl tab "" new
agent-ctl tab "" switch 2
agent-ctl run --agent gemini --task "review feature X design" --stop-at sent
```

## 6. Cross-Tab Task Dispatch

Send a task to a specific tab without switching the active tab:

```bash
# Read output from tab 1 (Codex)
agent-ctl read "" --lines 30 --tab 1

# Check state of tab 2
# (STATE|tab_index via raw pipe)
send_pipe "STATE|2"

# Send text to active tab only (INPUT goes to whichever tab is focused)
# To target a specific tab: switch first, send, switch back
agent-ctl tab "" switch 1
agent-ctl send "" "your task here"
agent-ctl tab "" switch 0
```

Note: `TAIL|lines|tab_index` reads from any tab without switching. But `INPUT` always goes to the active tab. To send input to a non-active tab, switch first.

## 7. Agent-Agnostic Task Cycle

The standard cycle works for Claude, Codex, and Gemini:

```bash
# 1. Send task (INPUT + Enter)
agent-ctl send "" "refactor the error handling in src/main.rs"

# 2. Wait for completion (Librarian-based state detection)
agent-ctl wait "" --timeout 600 --auto-approve

# 3. Read result
agent-ctl read "" --lines 50
```

### Librarian States

The Librarian (LLM-based state judge) reads terminal buffer and classifies:

| State | Meaning |
|-------|---------|
| SHELL_IDLE | No agent running, bare shell prompt |
| AGENT_STARTING | Agent is loading/initializing |
| AGENT_READY | Agent prompt visible, waiting for input |
| AGENT_WORKING | Agent is processing a task |
| AGENT_APPROVAL | Agent asking for permission (tool use, etc.) |
| AGENT_DONE | Agent finished, showing results |
| AGENT_INTERRUPTED | Ctrl+C or similar interruption |
| AGENT_ERROR | Agent crashed or errored |

### Stop Agents

Each agent has a different stop method:

```bash
agent-ctl stop "" claude    # Ctrl+C twice
agent-ctl stop "" codex     # /exit + Enter
agent-ctl stop "" gemini    # Ctrl+C once
```

## 8. Multiple WT Windows (Separate Sessions)

For completely isolated sessions (separate pipe, separate session file):

```bash
# Window 1
WINDOWS_TERMINAL_CONTROL_PLANE=1 ~/WindowsTerminal/bin/x64/Debug/WindowsTerminal/WindowsTerminal.exe &

# Window 2 (separate process = separate session file + pipe)
WINDOWS_TERMINAL_CONTROL_PLANE=1 ~/WindowsTerminal/bin/x64/Debug/WindowsTerminal/WindowsTerminal.exe &

# List all sessions to see both
agent-ctl list --alive-only

# Target a specific session by hint (substring of session_name)
agent-ctl send "session-abc" "task for window 1"
agent-ctl send "session-xyz" "task for window 2"
```

Each WT process creates its own `.session` file with a unique pipe. Use `agent-ctl list --alive-only` to enumerate, then target by session hint.

## 9. Automated Smoke Test

Verify CP connectivity:

```bash
agent-ctl smoke ""
# Runs: PING + LIST_TABS + STATE
```

## 10. Hook-Based Completion Detection (Legacy)

Hook files at `~/.agent-deck/hooks/{session_id}.json`:

```json
{"status":"running","event":"UserPromptSubmit","ts":1774048869}
{"status":"waiting","event":"Stop","ts":1774048873}
```

Poll loop (use `agent-ctl wait` instead when possible):
```bash
HOOK_FILE=$(ls -t ~/.agent-deck/hooks/*.json 2>/dev/null | head -1)
while true; do
  STATUS=$(python -c "import json; print(json.load(open('$HOOK_FILE'))['status'])")
  [ "$STATUS" = "waiting" ] && break
  sleep 2
done
```

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Using store `wt.exe` | Store WT has no CP DLL. Use fork binary only |
| Pipe not found | CP DLL creates pipe on startup. Wait 5-8s after launch |
| Rapid pipe calls fail | Named pipe is single-connection. Add 1s delay between calls |
| INPUT to wrong tab | INPUT goes to active tab. Switch first with SWITCH_TAB |
| `\\` eaten by bash | Use PowerShell for pipe paths, or Write tool for scripts |
| Trust prompt blocks agent | First Claude launch shows "trust this folder?". Send RAW_INPUT `\r` to approve |
| `AGENTDECK_INSTANCE_ID` missing | Hook wrapper (`agent-deck-hook.sh`) sets it from stdin session_id |
| Env var wrong | Must be `WINDOWS_TERMINAL_CONTROL_PLANE=1` (not GHOSTTY_CONTROL_PLANE for WT) |

## Benchmark

| Operation | Latency |
|-----------|---------|
| PING | <1ms |
| TAIL (30 lines) | 0.5ms |
| INPUT | 2.9ms |
| Hook detection | ~200ms (async) |
| Agent response | 6-9s (API dependent) |
