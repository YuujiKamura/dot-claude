---
name: terminal-ime-debugging
description: "Miscellaneous. (IME Preedit Layer Regression Prevention) Use when user mentions: ."
categories: [Git, WinUI3, WinUI3-Islands, Zig, analysis, bash, build-system, civil-engineering, cleanup, construction, construction-tech, crash, data-analysis, data-structure, debugging, disk-usage, extraction, ime, investigation, japanese, logging, logs, maintenance, meta, paveos, photo-analysis, project-management, refactor, refactoring, regression, system, terminal, tsf, win32, winui3, zig]
sources: [session-2026-03-16T20-01-8c1bcdf3, session-2026-03-16T20-01-a5b9ff58, 952919a2-b68b-4083-9b15-60a6cb0e3a57, b62d15d0-d67d-4c6a-9492-9766d0ab4806, session-2026-03-17T20-24-8401b53a, 4530e97b-83b9-476c-ae3c-8b5fd6a18524, 2af3b91e-14ed-4d46-9158-1375d496ac00, d1afaf4b-d648-4089-a6d3-4c91b03e78bc, 2661ead5-68c2-406e-a797-74de2e17d8b6, feb10a29-d26d-42e7-8828-75d3bebf68f8, d6a686ec-2362-4891-ad22-ca28baae17e1, 9ab97fda-e156-4cbd-96fb-bb5415a70bae]
---

# Miscellaneous

Patterns: 1

## 1. IME Preedit Layer Regression Prevention

Techniques for debugging and restoring IME (Input Method Editor) preedit text visibility in terminal surfaces after complex refactoring.

### Steps

1. Recognize that IME preedit display (text shown during composition) is a highly fragile layer that often breaks during refactoring of the surface or TSF bindings.
2. When composition fails, compare current TSF (Text Services Framework) bindings against known-good historical branches to identify lost display logic or coordinate mapping.
3. Verify 'input drift' alongside visibility to ensure the IME window correctly tracks the cursor position on the virtual terminal surface.

### Examples

```bash
git show archive/issue113-refactor-broken:src/apprt/winui3/tsf.zig
```


## Source

| Conversation | Excerpt |
|---|---|
| `9ab97fda-e156-4cbd-96fb-bb5415a70bae` | ShipOSならぬPaveOSをもじってつくってみようかと |
| `session-2026-03-16T20-01-8c1bcdf3` | ﻿Below are summaries from Claude Code conversations in the "Miscellaneous" domain.  Each conversat... |
| `session-2026-03-16T20-01-a5b9ff58` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `952919a2-b68b-4083-9b15-60a6cb0e3a57` | Implement the following plan:  # Issue #113 リファクタ段階適用計画  ## Context Issue #113... |
| `d1afaf4b-d648-4089-a6d3-4c91b03e78bc` | ghostty-winがイシュー１１３の変更のあと起動しなくなったのでチームで原... |
| `session-2026-03-17T20-24-8401b53a` | ghostty-winがIssue #113のリファクタ後に起動しなくなった。debug.logの最後は以... |
| `d6a686ec-2362-4891-ad22-ca28baae17e1` | 南千反畑の切削オーバーレイの４日間で、乳剤散布をしたあと、最初の温... |
| `2af3b91e-14ed-4d46-9158-1375d496ac00` | Fix TSF preedit display regression in ghostty-win. Compare git show archive/issue113-refactor-broken... |
| `2661ead5-68c2-406e-a797-74de2e17d8b6` | Replace all 184 fileLog calls with std.log in App.zig tsf.zig nonclient_island_window.zig tabview_ru... |
| `4530e97b-83b9-476c-ae3c-8b5fd6a18524` | Implement the following plan:  # 旧WinUI3実装の除去 (Issue #118)  ## Context `src/apprt/winui3... |
| `feb10a29-d26d-42e7-8828-75d3bebf68f8` | Cドライブの容量が最近圧迫されてるんで内訳を精査 |
| `b62d15d0-d67d-4c6a-9492-9766d0ab4806` | bash |


