---
name: windows-tsf-lifecycle-management
description: "Documentation. (TSF Lifecycle Integrity in UI Refactors) Use when user mentions: README, docs, documentation, tutorial, guide, comment."
categories: [Markdown, agent, config, instructions, issue, report, skills]
sources: [019cfdf9-fa0a-7492-957d-5f3b53990615, 019cfd58-8b67-70e0-a39b-fd16c2551eaa, 019cfda9-fc8d-76a2-bcd1-9a7e49ad408c, session-2026-03-17T19-52-7fd6f5af]
---

# Documentation

Patterns: 1

## 1. TSF Lifecycle Integrity in UI Refactors

Managing Text Services Framework (TSF) registrations across surface destruction and recreation to prevent input hangs.

### Steps

1. Simple surface-check replacements (like isSurfaceAlive) often cause TSF crashes if not tied to the thread manager lifecycle. Insight: TSF is 'surface-aware' and requires explicit unregistration BEFORE the underlying window surface is invalidated; merely checking 'alive' status is insufficient for input stability.
2. Auditing TSF changes requires verifying both the creation and disposal phases across the entire window lifecycle to ensure that orphaned thread manager registrations do not cause memory leaks.


## Source

| Conversation | Excerpt |
|---|---|
| `019cfdf9-fa0a-7492-957d-5f3b53990615` | # AGENTS.md instructions for C:\Users\yuuji\ghostty-win  <INSTRUCTIONS> # AGENTS.md  ## Project Scop... |
| `session-2026-03-17T19-52-7fd6f5af` | Issue #113 更新完了: https://github.com/YuujiKamura/ghostty/issues/113    Issue #113 全4項目... |
| `019cfda9-fc8d-76a2-bcd1-9a7e49ad408c` | # AGENTS.md instructions for C:\Users\yuuji  <INSTRUCTIONS> ## Skills A skill is a set of local inst... |
| `019cfd58-8b67-70e0-a39b-fd16c2551eaa` | # AGENTS.md instructions for C:\Users\yuuji  <INSTRUCTIONS> ## Skills A skill is a set of local inst... |


