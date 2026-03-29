---
name: skill-mining-optimization
description: "Override broad categories with task-specific slugs for skill extraction. Use when: merged skills, 'cli-tooling' too broad, domain subdivision needed."
project: skill-miner
---

# CLI & Tooling

Patterns: 1

## 1. Granular Domain Classification for Technical Skills

Broad domain labels like 'cli-tooling' or 'ai-ml' are insufficient for high-quality skill extraction. Practitioners must subdivide domains into narrow, specific categories to prevent distinct technical patterns from being merged into generic, low-value skills.

### Steps

1. Analyze conversation context for specific library, framework, or tool-specific APIs.
2. Override broad categories with task-specific slugs (e.g., 'claude-plugin-dev' instead of 'cli-tooling') to preserve technical nuances.



