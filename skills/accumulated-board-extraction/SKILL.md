---
name: accumulated-board-extraction
description: "累積黒板の最下段記入値ルールと温度正規表現抽出。Use when: 温度管理黒板, 到着温度, 最下段ルール, regex celsius extraction"
category: llm-patterns
---

# AI & Machine Learning

Patterns: 1

## 1. Accumulated Blackboard Data Extraction

Extracting the current measurement from cumulative construction blackboards where historical values are vertically listed.

### Steps

1. Apply the 'Lowest Filled Row' rule: when multiple temperature types (Arrival, Spreading, etc.) are listed, the bottom-most value is the current measurement for the photo.
2. Prioritize `focus_target` classification (e.g., 'Arrival Temp') over raw OCR text to disambiguate which label on a cumulative board should be matched.
3. Use a regex pattern like `[^,]*` (non-comma greedy match) followed by `[℃度]` to skip intervening labels and capture the final numeric value on a line.

### Examples

```rust
// Regex to handle cumulative labels followed by values
let pattern = format!(r"{}[^,]*(\d+\.?\d*)\s*[℃度]", regex::escape(name));
```

```text
温度管理黒板の重要ルール: 黒板に到着温度・敷均し温度・初期転圧前温度が縦に並んでいる場合、
記入済みの最下段の値がこの写真の測定値である。
```



