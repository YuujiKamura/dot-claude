---
name: multimodal-cli-debugging
description: "AI & Machine Learning. (On-Demand Visual Grounding for Protocol-Blind Debugging) Use when user mentions: LLM, GPT, Claude, Gemini, prompt, model, training, inference, embedding."
categories: [LLM, TypeScript, api, automation, camera, claude, cli, gemini, inference, mcp, model, ocr, prompting, session-analysis, skills, terminal, vision]
sources: [019d0f1b-4c98-7153-a3bd-383cb2d08ace, 909856f3-4cf8-4812-8bd5-ce344cef7bcb, e9d4f4d4-2731-4833-ad93-5728f320bca4, 2df6e00d-14ae-4a24-8c1a-b23a6114a9ae, 3b77be31-2c7e-4f50-bc00-d93b86689764, 10230494-ad98-4309-905d-f96d4ef945e6, 67c83b2d-53d8-4443-aeec-83e6d7fee81a]
---

# AI & Machine Learning

Patterns: 1

## 1. On-Demand Visual Grounding for Protocol-Blind Debugging

CLI agents are blind to GUI states or windowing events (like PostMessageW) that don't appear in standard logs. An on-demand snapshot architecture provides visual grounding for 'embodied' debugging without the token costs of continuous video.

### Steps

1. Reject continuous frame polling for CLI agents due to prohibitive API token costs and context window saturation.
2. Use an on-demand 'push' architecture where the user or a specific failure trigger captures a visual snapshot (e.g., via an IP camera or screen grab).
3. Utilize visual context specifically for 'protocol-blind' issues where internal system logs/traces are insufficient to explain GUI rendering or event loop failures.

### Examples

```bash
# On-demand snapshot from a physical 'eye' (IP Camera)
curl -s -o C:/Users/yuuji/camera_test.jpg http://192.168.2.116:8080/shot.jpg
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


