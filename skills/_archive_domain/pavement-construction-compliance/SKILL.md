---
name: pavement-construction-compliance
description: "Miscellaneous. (Pavement Temperature Compliance Logic) Use when user mentions: ."
---

# Miscellaneous

Patterns: 1

## 1. Pavement Temperature Compliance Logic

Handling specific logic for asphalt temperature management in Japanese civil engineering. Practitioners follow the 'Display Value Principle' where compliance checks (e.g., ±4°C) are performed on rounded integers (as they appear on the digital thermometer) rather than raw floating-point data. Also addresses common spreadsheet pitfalls like aggregate formulas missing the initial data block (Block 1).

### Steps

1. Round raw temperature measurements to the nearest integer before applying tolerance checks (e.g., |ROUND(val)-145| <= 4)
2. Verify that average formulas in 'Total' (計) sheets include all daily data blocks, specifically checking for the omission of the first block
3. Sync temperature values in Excel sheets with underlying photo analysis logs (result.json) to ensure evidence-based reporting



