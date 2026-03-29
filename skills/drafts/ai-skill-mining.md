---
name: ai-skill-mining
description: "AI & Machine Learning. (LLM-Centric Synthesis for Low-Frequency Engineering Insights) Use when user mentions: LLM, GPT, Claude, Gemini, prompt, model, training, inference, embedding."
categories: [LLM, TypeScript, api, automation, camera, claude, cli, gemini, inference, mcp, model, ocr, prompting, session-analysis, skills, terminal, vision]
sources: [909856f3-4cf8-4812-8bd5-ce344cef7bcb, 019d0f1b-4c98-7153-a3bd-383cb2d08ace, 3b77be31-2c7e-4f50-bc00-d93b86689764, 67c83b2d-53d8-4443-aeec-83e6d7fee81a, 10230494-ad98-4309-905d-f96d4ef945e6, 2df6e00d-14ae-4a24-8c1a-b23a6114a9ae, e9d4f4d4-2731-4833-ad93-5728f320bca4]
---

# AI & Machine Learning

Patterns: 1

## 1. LLM-Centric Synthesis for Low-Frequency Engineering Insights

Statistical clustering (TF-IDF) often discards the most valuable technical breakthroughs as 'noise' because they are unique and lack frequency. Effective skill mining requires LLM synthesis to recognize the structure of a novel solution where heuristics fail.

### Steps

1. Recognize that high-value problem-solving (e.g., niche systems programming) is statistically rare and will be filtered out by frequency-based clustering algorithms.
2. Avoid skipping the LLM synthesis step (e.g., via --skip-synthesis) during session analysis, as heuristic clustering alone provides no semantic utility.
3. Prioritize depth of reasoning over frequency of occurrence when identifying 'skills' from agentic session histories.

### Examples

```bash
# BAD: Generates empty clusters by skipping semantic reasoning
npx tsx scripts/analyze-sessions.ts --skip-synthesis
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


