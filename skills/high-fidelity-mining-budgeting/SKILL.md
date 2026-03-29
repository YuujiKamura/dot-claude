---
name: high-fidelity-mining-budgeting
description: "LLMトークン上限内でコード詳細を保持する切り詰め戦略。Use when: truncation 2000-3000 chars, token budget, Gemini Flash 1M"
category: skill-mining-meta
---

# AI & Machine Learning

Patterns: 1

## 1. LLM Context Budgeting for Pattern Mining

Managing truncation limits and conversation history depth to capture actionable code snippets and complex JSON structures without exceeding model token limits (e.g., Gemini Flash 1M tokens).

### Steps

1. Calculate total token capacity and safety margins for the target LLM
2. Set message truncation limits high enough (e.g., 2000-3000 characters) to preserve core technical content like code blocks and schemas
3. Increase conversation turn limits to capture late-stage corrections and final refined patterns



