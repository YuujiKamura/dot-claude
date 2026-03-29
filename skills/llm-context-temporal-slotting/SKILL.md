---
name: llm-context-temporal-slotting
description: "大量ログを時間スロット分割してLLMコンテキスト上限内に。Use when: day slot summarization, context overflow, temporal chunking"
category: llm-patterns
---

# AI & Machine Learning

Patterns: 1

## 1. Context Window Management via Temporal Slotting

When summarizing long-duration logs, chunking data into temporal 'slots' prevents exceeding LLM context limits and reduces the risk of information loss in large batches.

### Steps

1. Partition a day's worth of activity into discrete 'day slots' based on the selected granularity before invoking the summarization function.
2. Summarize each temporal slot as an independent context unit, allowing the system to handle massive log volumes that would otherwise overwhelm a single prompt.
3. Use the structured output from individual slot summaries to reconstruct a cohesive, higher-level narrative of the entire day or project duration.

### Examples

```
summarize_day_slots_with_ai(entries, granularity)
```



