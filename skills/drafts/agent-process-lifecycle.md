---
name: agent-process-lifecycle
description: "AI & Machine Learning. (Environment-Based Lineage Tracking for Orphaned Agent Processes) Use when user mentions: LLM, GPT, Claude, Gemini, prompt, model, training, inference, embedding."
categories: [LLM, TypeScript, api, automation, camera, claude, cli, gemini, inference, mcp, model, ocr, prompting, session-analysis, skills, terminal, vision]
sources: [909856f3-4cf8-4812-8bd5-ce344cef7bcb, 2df6e00d-14ae-4a24-8c1a-b23a6114a9ae, 019d0f1b-4c98-7153-a3bd-383cb2d08ace, e9d4f4d4-2731-4833-ad93-5728f320bca4, 10230494-ad98-4309-905d-f96d4ef945e6, 3b77be31-2c7e-4f50-bc00-d93b86689764, 67c83b2d-53d8-4443-aeec-83e6d7fee81a]
---

# AI & Machine Learning

Patterns: 1

## 1. Environment-Based Lineage Tracking for Orphaned Agent Processes

Standard Parent-PID (PPID) tracking is unreliable for cleaning up agent residues because the lineage is lost if the orchestrator dies. Injecting session-specific UUIDs into the environment block allows for reliable 'embodied' process cleanup.

### Steps

1. Inject a unique session UUID (e.g., AGENTDECK_SESSION) into the environment variables at the root of an agent task to ensure propagation to all children.
2. Recover process lineage by scanning the environment blocks of active processes rather than relying on volatile system PID tables.
3. Implement a three-tier classification for cleanup: 'owned' (safe to kill if inactive), 'foreign' (unrelated tasks), and 'unknown' (system processes) to prevent accidental OS instability.

### Examples

```bash
# Injecting tracking marker at startup
export AGENTDECK_INSTANCE_ID=$(uuidgen)
```

```go
// Logic for TestClassifyStaleProcess_OwnedFromMarker
if strings.Contains(proc.Env, "AGENTDECK_INSTANCE_ID=") {
 return ProcessStateOwned
}
```


## Source

| Conversation | Excerpt |
|---|---|
| `10230494-ad98-4309-905d-f96d4ef945e6` | https://zenn.dev/chigichan24/articles/eed4a60d102997 |
| `909856f3-4cf8-4812-8bd5-ce344cef7bcb` | usage |
| `019d0f1b-4c98-7153-a3bd-383cb2d08ace` | <environment_context>   <cwd>C:\Users\yuuji</cwd>   <shell>powershell</shell>   <current_date>2026-0... |
| `e9d4f4d4-2731-4833-ad93-5728f320bca4` | Issue #1 is now partially implemented in the local agent-deck tree: launch paths already inject AGEN... |
| `67c83b2d-53d8-4443-aeec-83e6d7fee81a` | ClaudeCodeにカメラを接続した話ってあのあとどうなったんだろうな  14:16 気... |
| `2df6e00d-14ae-4a24-8c1a-b23a6114a9ae` | curl http://192.168.2.116:8080/shot.jpg で画像を C:/Users/yuuji/camera_test2.jpg に保存して... |
| `3b77be31-2c7e-4f50-bc00-d93b86689764` | curl http://192.168.2.116:8080/shot.jpg で画像を C:/Users/yuuji/camera_test.jpg に保存して... |


