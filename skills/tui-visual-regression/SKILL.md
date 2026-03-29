---
name: tui-visual-regression
description: "TUIレンダリングバグをスクリーンショット+VLMで自動検出。Use when: TUI visual bug, screenshot smoke test, Tab alignment, rendering glitch"
category: testing-qa
---

# CLI & Tooling

Patterns: 1

## 1. Automated Visual Smoke Testing

Closing the feedback loop for terminal UI (TUI) rendering bugs using automated screenshots and VLM analysis.

### Steps

1. Relying on standard output or return codes to debug terminal rendering is insufficient; TUI bugs (like incorrect Tab view alignment) often report 'success' at the driver level while failing visually.
2. Integrate an automated visual confirmation loop using scripts to capture screenshots of the terminal state. This allows the AI to diagnose spatial layout artifacts and rendering glitches that are invisible to text-based log analysis.

### Examples

```
powershell.exe -File .\visual_smoke_test_run.ps1
```

```
capture_terminal_screenshot --output debug_frame.png
```



