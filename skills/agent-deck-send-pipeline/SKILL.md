---
name: agent-deck-send-pipeline
description: "agent-deck send pipeline: SubmitPrompt 3-phase, Watcher/Detect status polling, trust dialog dismiss. Use when: agent-deck send, session add, verifyAccepted, BufferNotification, detect.go"
project: ghostty-win
---

# agent-deck Send Pipeline

## CLI UX (Issue #25, resolved)

```
agent-deck session add ghostty-59840 --name my-agent --tool claude
agent-deck send my-agent "do something"
agent-deck watch my-agent --interval 500ms
```

- `send` / `ask` / `session send` — all route to same handler
- `session add <name|pid>` — register CP session into deck by name or PID
- Unregistered sessions: error with discovery list + registration command
- Tool auto-detected from session name or --tool flag

## Status Detection (Issue #24, resolved)

### Layer 1: Watcher (`internal/status/watcher.go`)
Polls CapturePane at 500ms (configurable). Emits `BufferNotification`:
- `Content` — raw screen text
- `Hash` — SHA-256 of content
- `Changed` — hash differs from previous
- `StableFor` — consecutive identical reads

No state judgment. Consumer decides what content means.

### Layer 2: Detect (`internal/status/detect.go`)
Optional pattern matcher called by consumer when hash stabilizes:
- `active` — spinner, "ctrl+c to interrupt", token counter
- `idle` — Claude ❯, Codex ›, Gemini ✦, shell $
- `permission` — "Allow once", Y/n, trust dialog
- `not_started` — cmd.exe/bash prompt, no agent markers
- `starting` — "Accessing workspace", loading

### What was deleted
- Hook fast path (instance.go) — Watcher replaces it
- PromptDetector (detector.go ~465 lines) — merged into Detect()
- Protocol.IsReady() 4 implementations — delegate to Detect()
- Event subscription as primary source — CP events now optional refinement
- 6-variable verifyAccepted state machine → simplified to sawActive + stableCount

## SubmitPrompt (`internal/send/submit_prompt.go`)

### 3-Phase Pipeline
1. `dismissBlockingPrompt` — trust dialog auto-dismiss (before everything)
2. `waitForReady` — detect tool prompt via Detect()
3. `Send` — RAW_INPUT via CP pipe
4. `verifyAccepted` — poll until Detect says active, then idle

### verifyAccepted (simplified)
- `sawActive` — saw active state after send
- `stableCount` — consecutive idle/waiting reads
- After 8 idle reads without ever seeing active → resend or Ctrl+C

## Key Files
- `cmd/agent-deck/send_cmd.go` — unified send handler
- `cmd/agent-deck/watch_cmd.go` — watch command
- `cmd/agent-deck/session_cmd.go` — session add handler
- `internal/status/watcher.go` — BufferNotification emitter
- `internal/status/detect.go` — screen pattern matcher
- `internal/send/submit_prompt.go` — SubmitPrompt pipeline
