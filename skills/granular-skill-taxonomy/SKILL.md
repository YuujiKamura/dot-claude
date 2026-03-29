---
name: granular-skill-taxonomy
description: "粗いドメインカテゴリからトピック単位slugへスキル粒度を細分化。Use when: skill slug naming, coarse category, CLAUDE.md noise filter"
category: skill-mining-meta
---

# CLI & Tooling

Patterns: 1

## 1. Topic-Level Skill Generation

Shifting from broad domain categories to specific topic-based slugs to make extracted knowledge actionable.

### Steps

1. Broad categories like 'cli-tooling' are too coarse for effective retrieval; skills should be grouped by specific topics like 'claude-plugin-dev'.
2. System reminders and agent-specific behavior rules (from CLAUDE.md) must be filtered out during extraction to keep the knowledge base purely domain-focused.
3. Extraction templates must explicitly prioritize 'Why' decisions and 'Failure->Success' stories over procedural step-by-step code logs.

### Examples

```
// src/generator.rs: stop using coarse domain slugs; generate topic-specific slugs instead
```



