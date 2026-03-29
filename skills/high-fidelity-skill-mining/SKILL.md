---
name: high-fidelity-skill-mining
description: "Filter meta-files, enforce topic-level naming, require literal code in steps. Use when: abstract summaries, skill granularity, CLAUDE.md leaking into skills."
project: skill-miner
---

# AI & Machine Learning

Patterns: 1

## 1. High-Fidelity Technical Skill Extraction

Refining extraction criteria to move from abstract summaries to actionable, concrete technical patterns.

### Steps

1. Filter out meta-files and system instructions (e.g., CLAUDE.md, settings.json) that contain generic behavioral rules rather than unique problem context.
2. Enforce topic-level granularity in naming to ensure skills remain specific and immediately useful for practitioners.
3. Validate that extracted 'steps' contain literal code patterns (e.g., specific polyglot headers or command flags) rather than high-level descriptions.



