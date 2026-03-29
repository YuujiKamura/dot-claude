---
name: autonomous-agent-handoff
description: "AI & Machine Learning. (The 'Don't Whine, Hand Off' Mandate) Use when user mentions: LLM, GPT, Claude, Gemini, prompt, model, training, inference, embedding."
---

# AI & Machine Learning

Patterns: 1

## 1. The 'Don't Whine, Hand Off' Mandate

A paradigm shift in autonomous agent design where context exhaustion is treated as a system event rather than a user-facing error. Instead of apologizing or pausing for confirmation when context is low, the agent uses the control plane to seamlessly boot a fresh instance and transfer the state.

### Steps

1. Context-limit warnings are considered 'noise' in autonomous workflows; the agent should prioritize using remaining tokens for a handoff protocol rather than apologies.
2. Gemini is identified as a superior target for delegated 'heavy lifting' tasks compared to older models like Codex when Claude's context window is saturated.
3. The handoff must be transparent to the user, moving the 'human-in-the-loop' requirement to the control plane level where it can be handled by automated approvals.

### Examples

```
agent-ctl handoff --target gemini --session-state ./context.json
```



