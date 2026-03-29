---
name: construction-photo-ocr-logic
description: "AI & Machine Learning. (Cumulative Blackboard Interpretation Rule) Use when user mentions: LLM, GPT, Claude, Gemini, prompt, model, training, inference, embedding."
---

# AI & Machine Learning

Patterns: 1

## 1. Cumulative Blackboard Interpretation Rule

A specific heuristic for civil engineering photos where physical blackboards track cumulative measurements; only the bottom-most entry represents the valid reading for the current state.

### Steps

1. Identify vertically stacked measurement values (e.g., arrival, spreading, and compaction temperatures) on the physical blackboard
2. Apply the 'lowest-filled-row' rule to determine the current measurement for the photo's primary description
3. Record all values in a raw text field while mapping only the latest value to the active measurement field



