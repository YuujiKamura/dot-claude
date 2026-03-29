---
name: xaml-islands-input-routing
description: "Documentation. (Custom Titlebar Input Routing in XAML Islands) Use when user mentions: README, docs, documentation, tutorial, guide, comment."
categories: [Markdown, agent, config, instructions, issue, report, skills]
sources: [019cfda9-fc8d-76a2-bcd1-9a7e49ad408c, 019cfdf9-fa0a-7492-957d-5f3b53990615, 019cfd58-8b67-70e0-a39b-fd16c2551eaa, session-2026-03-17T19-52-7fd6f5af]
---

# Documentation

Patterns: 1

## 1. Custom Titlebar Input Routing in XAML Islands

Resolving hit-test failures in layered windows hosted within XAML Islands environments by verifying Z-order against known-good host implementations.

### Steps

1. Individual hit-test debugging often fails because visual visibility (alpha=255) is confused with input visibility. Insight: In XAML Islands, the DesktopWindowXamlSource Z-order can take absolute precedence over layered windows using WS_EX_LAYERED | WS_EX_NOREDIRECTIONBITMAP, requiring a manual 'reference implementation' check against Windows Terminal to identify input masking.
2. Validation of custom drag bars (e.g., titlebar_h=45) requires confirming if the island host is transparently intercepting mouse messages. Correcting this involves checking the host's Z-order relative to the custom HWND rather than just verifying window styles.

### Examples

```cpp
// Reference for routing logic in Windows Terminal
src/cascadia/WindowsTerminal/NonClientIslandWindow.cpp
```

```zig
// Styles prone to hit-test masking when DesktopWindowXamlSource is present
WS_EX_LAYERED | WS_EX_NOREDIRECTIONBITMAP
```


## Source

| Conversation | Excerpt |
|---|---|
| `019cfdf9-fa0a-7492-957d-5f3b53990615` | # AGENTS.md instructions for C:\Users\yuuji\ghostty-win  <INSTRUCTIONS> # AGENTS.md  ## Project Scop... |
| `session-2026-03-17T19-52-7fd6f5af` | Issue #113 更新完了: https://github.com/YuujiKamura/ghostty/issues/113    Issue #113 全4項目... |
| `019cfda9-fc8d-76a2-bcd1-9a7e49ad408c` | # AGENTS.md instructions for C:\Users\yuuji  <INSTRUCTIONS> ## Skills A skill is a set of local inst... |
| `019cfd58-8b67-70e0-a39b-fd16c2551eaa` | # AGENTS.md instructions for C:\Users\yuuji  <INSTRUCTIONS> ## Skills A skill is a set of local inst... |


