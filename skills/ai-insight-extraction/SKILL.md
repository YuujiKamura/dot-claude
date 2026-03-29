---
name: ai-insight-extraction
description: "技術ログ要約はFlashよりFlagshipモデル。Use when: model selection for summarization, quality vs cost, context bloat"
category: llm-patterns
---

# AI & Machine Learning

Patterns: 1

## 1. Model Capability Over Cost for Technical Synthesis

Prioritizing reasoning depth over cost/speed when distilling complex technical logs into actionable insights.

### Steps

1. Attempting to use low-cost models (e.g., Gemini Flash) for technical distillation often results in quality loss because they struggle to manage context bloat and fail to distinguish critical architectural choices from generic boilerplate.
2. The 'bottleneck' in technical summarization isn't just cost, but the model's ability to synthesize the 'why' behind a change. Using flagship models for the extraction phase ensures the output is technically meaningful rather than just a shallow description of activity.



