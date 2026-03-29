---
name: heuristic-scoring-validation
description: "頻度/鮮度/生産性スコアの休眠ペナルティと先読み検証。Use when: dormancy penalty, frequency scoring, productivity look-ahead"
category: testing-qa
---

# Testing & QA

Patterns: 1

## 1. Activity-Based Heuristic Scoring Verification

Testing scoring engines that weight frequency, freshness, and productivity. Experienced practitioners focus on 'dormancy penalties' for inactive items and verifying 'productivity' through look-ahead analysis of subsequent interactions.

### Steps

1. Verify dormancy penalty math: ensure multipliers are correctly applied based on the age of the last activity (e.g., >14 days).
2. Validate productivity detection: check if the subsequent assistant message successfully utilized the extracted item (e.g., tool usage detection).
3. Ensure multi-factor weightings (e.g., 60% frequency / 40% pattern match) are calculated accurately without rounding errors.



