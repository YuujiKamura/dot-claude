---
name: marketing-vlm-automation
description: "AI & Machine Learning. (VLM-Integrated Data-to-Proposal Loop) Use when user mentions: LLM, GPT, Claude, Gemini, prompt, model, training, inference, embedding."
---

# AI & Machine Learning

Patterns: 1

## 1. VLM-Integrated Data-to-Proposal Loop

A workflow for scaling complex business analysis by chaining MCP tools with specialized retrieval CLIs for end-to-end strategy generation.

### Steps

1. Specialized retrieval tools (like gog CLI) are necessary to bridge the gap between an LLM's internal knowledge and real-time, web-scale market data.
2. Strategy proposals gain consistency when the agent has access to 'Rule-based memory' that stores proven successful campaign structures for the specific domain.
3. The value lies in the 'loop' (Retrieve -> Analyze -> Propose) being fully executable in a single autonomous turn using the control plane.

### Examples

```
gog search "competitor-analysis" | claude-code "generate-marketing-proposal"
```



