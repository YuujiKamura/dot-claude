---
name: qa-knowledge-evidence-gating
description: "Require conversational evidence (user correction, debate) before accepting extracted patterns. Use when: weak evidence, generic patterns, QA skill quality."
project: skill-miner
---

# Testing & QA

Patterns: 1

## 1. Only accept patterns with explicit discussion evidence

For Testing & QA knowledge extraction, a pattern is valid only when conversation evidence shows active scrutiny (user correction, repeated back-and-forth, or explicit judgment teaching). This prevents generic process content from being mislabeled as domain expertise.

### Steps

1. Reject candidate patterns unless there is explicit conversational evidence that the criterion was debated, corrected, or reinforced.
2. Prioritize user-corrected assumptions over assistant-proposed structure, because corrections reveal real practitioner judgment.
3. Mark weakly evidenced items as out-of-scope even if technically plausible.



