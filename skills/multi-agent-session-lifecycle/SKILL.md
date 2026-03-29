---
name: multi-agent-session-lifecycle
description: "Agent Orchestration. (session add/send/watch, tmux-equivalent CP operations, tool-agnostic design) Use when user mentions: multi-agent, agent-deck session, coordination, lifecycle, session add, session send, watch."
project: ghostty-win
---

# Multi-Agent Session Lifecycle

## Core Concept

agent-deck = tmux session manager reimplemented over Windows Named Pipes.

| tmux | agent-deck CP |
|------|--------------|
| `tmux capture-pane` | `TAIL` (CapturePane) |
| `tmux send-keys` | `SEND_INPUT` / `RAW_INPUT` |
| `tmux has-session` | `PING` |
| `tmux list-sessions` | `gtcp list` / session file discovery |

The upper layer (Watcher, Detect, SubmitPrompt) works identically regardless of transport.

## CLI Flow

```bash
# 1. Discover
agent-deck watch ghostty-59840          # see what's on screen

# 2. Register
agent-deck session add ghostty-59840 --name worker-1 --tool claude

# 3. Send
agent-deck send worker-1 "do the task"

# 4. Monitor
agent-deck watch worker-1 --interval 500ms
```

## Session Lifecycle

1. **Discover**: `gtcp list` finds CP sessions via .session files in LOCALAPPDATA
2. **Register**: `session add` creates Instance in SQLite, binds CPPipePath + CPPID
3. **Start tool**: `send <session> "claude"` launches Claude in the terminal
4. **Trust dismiss**: SubmitPrompt auto-dismisses "trust this folder" dialog
5. **Send task**: `send <session> "message"` → SubmitPrompt pipeline
6. **Watch**: Watcher polls TAIL at 500ms, emits BufferNotification
7. **Detect state**: consumer calls Detect(content) if needed

## Tool-Agnostic Design

Watcher doesn't know or care what's running. Hash changes = active, stable = not active. Works for:
- Claude Code (❯ prompt, spinner, ctrl+c)
- Codex CLI (› prompt)
- Gemini CLI (✦ prompt)
- Any shell ($ prompt)
- Any TUI app

Detect() is optional pattern matching for consumers that want finer state labels.

## Failure Recovery

| Problem | Detection | Action |
|---------|-----------|--------|
| Dead pipe | `gtcp list` [DEAD PIPE] | Kill + restart ghostty |
| Stale session | `gtcp list` [STALE] | Auto-cleaned |
| Trust dialog | Detect → permission | auto-dismiss via Enter |
| Tool not started | Detect → not_started | send tool name |
| Unregistered session | send error | shows discovery list + add command |
