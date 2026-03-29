---
name: cjk-terminal-font-metrics
description: "全角CJK文字の2セル幅レンダリング修正。Use when: CJK glyph clipping, U+3002, full-width half-width, advance width, font fallback, grid alignment"
project: ghostty-win
---

# Miscellaneous

Patterns: 1

## 1. Full-width CJK Glyph Metric Calculation

Addressing rendering glitches for full-width characters (like U+3002) in terminal emulators by strictly enforcing 2-cell width logic.

### Steps

1. Rendering glitches for CJK punctuation (e.g., the Japanese period '。') are typically width-calculation errors where the renderer treats a 2-cell character as a 1-cell character.
2. Terminal emulators must explicitly handle the distinction between half-width and full-width glyphs based on Unicode properties to ensure proper grid alignment.
3. If a glyph appears offset or clipped, verify if the font fallback chain is correctly calculating the advance width for the specific cell size of the terminal grid vs. the actual font metrics.



