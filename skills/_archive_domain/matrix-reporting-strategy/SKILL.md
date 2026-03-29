---
name: matrix-reporting-strategy
description: "Construction & Civil Engineering. (Topic-Time Matrix Layout) Use when user mentions: 報告書, レイアウト, マトリクス, 工程, report, construction, timeline."
---

# CLI & Tooling

Patterns: 1

## 1. Topic-Time Matrix Layout

Sequential or single-column reporting of complex projects is monotonous and hides parallel dependencies. A 'Topic × Month' matrix format is required to visualize overlapping timelines like PR activities vs. actual construction.

### Steps

1. Avoid forcing chronological text into empty fields; use a matrix to show gaps in activity as meaningful project state.
2. Visualizing 'Regulation Start' vs 'Incident Response' (Noise Complaints) side-by-side reveals spatial/temporal correlations that sequential lists obscure.
3. Lock the final structural state once a user performs manual adjustments, as LLMs tend to revert 'messy' but functional human layouts to 'clean' but useless monotonous lists.

### Examples

```
// Expected Excel Structure:
// [Topic] | [Jan] | [Feb] | [Mar]
// PR Flyers | 537 | - | -
// Regulation | - | 22:00 | 22:00
```



