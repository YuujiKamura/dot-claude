---
name: temporal-wait-state-nuance
description: "AI & Machine Learning. (Temporal Differentiation of Agent Wait-States) Use when user mentions: LLM, GPT, Claude, Gemini, prompt, model, training, inference, embedding."
categories: [Agent, Claude, LLM, State Management]
sources: [5466f2b8-2bef-45e5-8f06-029174f01631]
---

# AI & Machine Learning

Patterns: 1

## 1. Temporal Differentiation of Agent Wait-States

Distinguishing between initial, intermediate, and terminal wait-states to prevent downstream orchestration errors.

### Steps

1. [INTERVENTION] User: 'ただし、アイドル、と、エージェントレディ、アプローバル、ダン、っていう、複数の待ち状態があるのが最大の特徴なんで、詳しく区別させるように状態を分けておく。そうしないと受ける側が間違えるんで' -> Directed the creation of a granular state machine to capture subtle temporal differences.
2. Defined 'READY' as the initial state (started, waiting for the first task) vs 'DONE' as the terminal state (task finished, result displayed, waiting for the next task).
3. Identified 'STARTING' (banner/loading visible) and 'IDLE' (no agent, shell prompt only) as critical non-working states to prevent early task injection.
4. The orchestrator (agent-ctl) uses these distinct wait states to determine when it is safe to send the next command or when it must wait for user permission ('APPROVAL').

### Examples

```json
{
 "IDLE": "Agent not started, shell prompt only",
 "STARTING": "Agent loading, banner or loading indicator visible",
 "READY": "Agent started, waiting for first task",
 "WORKING": "Task in progress, output streaming",
 "APPROVAL": "Waiting for user permission (Allow once, Yes/No)",
 "DONE": "Task finished, results displayed, waiting for next task"
}
```


## Source

| Conversation | Excerpt |
|---|---|
| `5466f2b8-2bef-45e5-8f06-029174f01631` | Implement the following plan:  # 司書オブザーバー: LLMベース状態管理  ## Context  age... |


