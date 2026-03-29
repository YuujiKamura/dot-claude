---
name: claude-code-workflow-enforcement
description: "Plan承認後のチーム並列実行を強制。Use when: Plan→Team, 並列実行禁止違反, 一人で順番にやるな"
category: claude-config
---

# Documentation

Patterns: 1

## 1. Mandatory Parallel Team Execution

Forcing the agent to transition from sequential task processing to parallel multi-agent execution following the approval of a plan.

### Steps

1. Mandate the use of 'Plan mode' for any non-trivial or multi-step task to establish a structured roadmap first.
2. Explicitly forbid the agent from performing planned tasks sequentially as a single agent.
3. Instruct the agent to utilize parallel dispatching tools (like a 'Team' or 'Superpowers' plugin) immediately upon plan approval to accelerate implementation.

### Examples

```
## 計画→チーム実行
- 非自明なタスクはPlanモードで計画を立てろ
- 計画承認後はチームを組んで並列実行しろ。一人で順番にやるな
```



