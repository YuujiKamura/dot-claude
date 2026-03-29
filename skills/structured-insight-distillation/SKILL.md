---
name: structured-insight-distillation
description: "Isolate failure-to-success narratives and user corrections from procedural noise. Use when: serde(default), domain aha-moments, git/test noise filtering."
project: skill-miner
---

# AI & Machine Learning

Patterns: 1

## 1. Distinguishing Domain Insight from Procedural Noise

Effective knowledge extraction requires isolating unique judgment criteria and 'aha' moments from standard developer operations. This separation ensures the resulting skill library is high-signal and actionable.

### Steps

1. Scan for 'failure-to-success' narratives where an initial approach failed due to a subtle domain-specific constraint (e.g., spatial context requirements for VLMs).
2. Identify user corrections and redirections as prime sources of 'practitioner-only' knowledge.
3. Filter out procedural noise (e.g., git commits, test runs, config setup) to maintain focus on high-level design principles and decision criteria.

### Examples

```rust
// Procedural noise (Ignore):
let x = 1 + 1;

// Domain Insight (Prioritize):
// Old manifests must still parse; #[serde(default)] prevents failures on legacy data.
#[serde(default)]
mined_ids: Vec<String>,
```



