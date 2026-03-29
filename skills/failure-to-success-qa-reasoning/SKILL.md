---
name: failure-to-success-qa-reasoning
description: "QA知見は失敗→成功の因果+定量デルタで記録。Use when: 10%→90% progression, causal QA narrative, why behind improvement"
category: testing-qa
---

# Testing & QA

Patterns: 1

## 1. Prefer causal failure→success narratives over procedural steps

High-value QA knowledge is the causal chain: what failed, why it failed, and what changed the outcome. The user explicitly emphasized quantified progression (10%→75%→90%) and the underlying reason, which is stronger than generic 'do X then Y' instructions.

### Steps

1. Capture patterns as causal contrasts (old method failed because specific constraint; new method worked because it addressed that constraint).
2. Require the 'why' behind performance gains, not just tool or pipeline changes.
3. When available, include quantified deltas to separate real QA insight from anecdotal workflow.



