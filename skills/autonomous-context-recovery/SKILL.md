---
name: autonomous-context-recovery
description: "grep/glob/list_directoryで不足データを自律探索して自己復旧。Use when: context recovery, autonomous unblock, proactive discovery"
category: llm-patterns
---

# AI & Machine Learning

Patterns: 1

## 1. Search-Based Context Recovery Strategies

Truly autonomous agents should attempt to 'unblock' themselves by discovering missing context within their permitted environment before requiring human intervention.

### Steps

1. Use discovery tools (grep, glob, list_directory) to map out non-obvious project structures that might contain missing logs or data.
2. Synthesize fragments from multiple sources (prompts, debug logs, scripts) to reconstruct the original user intent.
3. Key insight: Proactive discovery is significantly more efficient than asking the user for data that is already present in the system environment.

### Examples

```bash
glob --pattern "~\.gemini\tmp\**\*.json"
```



