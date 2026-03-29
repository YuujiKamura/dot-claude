---
name: agent-control-plane-automation
description: "AI & Machine Learning. (Prompt-Aware Execution Control) Use when user mentions: LLM, GPT, Claude, Gemini, prompt, model, training, inference, embedding."
---

# AI & Machine Learning

Patterns: 1

## 1. Prompt-Aware Execution Control

Moves beyond fragile shell-based 'sleep' loops to a state-aware control plane that can interact with sub-agents' interactive prompts.

### Steps

1. External polling with 'sleep' is a bottleneck; implement internal state monitoring (send_and_wait) to detect when a sub-agent is blocked.
2. Autonomous agents frequently stall on 'Are you sure? [y/n]' prompts; the control plane must include logic to automatically inject 'y' responses to maintain momentum.
3. Timeout handling must distinguish between 'working on a hard problem' and 'waiting for user input' to avoid premature termination of complex tasks.

### Examples

```
send_and_wait(terminal, command="npm test", auto_confirm=True, timeout=300)
```



