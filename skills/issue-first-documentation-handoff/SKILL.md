---
name: issue-first-documentation-handoff
description: "Issue作成→並列委託の前にID採番を確定し整合性担保。Use when: issue numbering, delegation handoff, ID range mismatch"
category: custom-command
---

# Documentation

Patterns: 1

## 1. Issue numbering consistency is part of documentation correctness

For delegation-oriented documentation, issue IDs are executable references. Ambiguity in ranges/counts weakens downstream task routing even if technical grouping is reasonable.

### Steps

1. Create and link issues before execution planning so each delegated unit has stable context.
2. Keep visible IDs, claimed counts, and numeric ranges strictly consistent; mismatches are treated as reliability defects.
3. When suggesting parallel vs sequential work, anchor every bucket to concrete issue numbers.



