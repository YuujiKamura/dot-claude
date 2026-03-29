---
name: agent-ctl-standardization
description: "AI & Machine Learning. (Universal Agent-Session Abstraction) Use when user mentions: LLM, GPT, Claude, Gemini, prompt, model, training, inference, embedding."
---

# AI & Machine Learning

Patterns: 1

## 1. Universal Agent-Session Abstraction

A design principle suggesting that agent management should be a universal CLI standard (like Git) that abstracts the underlying transport layer (Named Pipes, Unix Sockets, etc.).

### Steps

1. Treat terminal sessions as 'pluggable backends'; the agent should interact with a session ID, not a specific OS-level pipe or window name.
2. Abstraction is superior to deep integration; build a CLI layer 'over' the terminal rather than building agent logic 'into' the terminal software.
3. Use named sessions to enable human-readable tracking of complex multi-agent graphs (e.g., 'researcher-session', 'reviewer-session').

### Examples

```
agent-ctl list-sessions
```

```
agent-ctl attach --session lead-dev
```



