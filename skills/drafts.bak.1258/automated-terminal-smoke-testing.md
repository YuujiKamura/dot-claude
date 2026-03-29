---
name: automated-terminal-smoke-testing
description: "Documentation. (Non-Interactive Rendering Stress-Tests) Use when user mentions: README, docs, documentation, tutorial, guide, comment."
categories: [AGENTS.md, Ghostty, code-explanation, configuration, documentation, ghostty-win, project-scope, terminal, winui3, zig]
sources: [session-2026-03-19T07-39-db08116b, 019d0459-74ac-75d1-8b91-d0ab99812e42, 019d0487-f3a6-7991-ada0-a0f220ee43c2, d658da03-ff03-4991-9a92-52bd28ea5663, 019d044e-a335-7271-9c12-67df66b02ece, 019d0444-29fb-7523-9bc0-9433013476e5, 019d043b-dc26-7db2-911a-f41764a0f67e]
---

# Documentation

Patterns: 1

## 1. Non-Interactive Rendering Stress-Tests

Stability in high-performance terminal rendering requires automated validation that surfaces race conditions in window initialization. Using scripted animations with specific font/timing constraints is more effective than manual UI interaction.

### Steps

1. Stress-test the rendering loop by launching automated animations (e.g., ghost-demo) with minimized font sizes to maximize frame throughput and surface race conditions.
2. Set a fixed benchmark duration (e.g., 10 seconds) for automated tests; initialization crashes in ReleaseFast often occur within the first 500ms of XAML hookup.
3. Standardize validation commands in wrapper scripts to ensure that 'ReleaseFast' binaries sustain high-load rendering without XAML thread deadlocks.

### Examples

```
ghostty.exe --font-size=7 -e "tools\ghost-demo\demo-wrapper.cmd"
```


## Source

| Conversation | Excerpt |
|---|---|
| `d658da03-ff03-4991-9a92-52bd28ea5663` | ゴーストティの公式のドキュメントを読み聞かせて |
| `019d0487-f3a6-7991-ada0-a0f220ee43c2` | # AGENTS.md instructions for C:\Users\yuuji\ghostty-win  <INSTRUCTIONS> # AGENTS.md  ## Project Scop... |
| `019d0459-74ac-75d1-8b91-d0ab99812e42` | # AGENTS.md instructions for C:\Users\yuuji\ghostty-win  <INSTRUCTIONS> # AGENTS.md  ## Project Scop... |
| `019d044e-a335-7271-9c12-67df66b02ece` | # AGENTS.md instructions for C:\Users\yuuji\ghostty-win  <INSTRUCTIONS> # AGENTS.md  ## Project Scop... |
| `019d0444-29fb-7523-9bc0-9433013476e5` | # AGENTS.md instructions for C:\Users\yuuji\ghostty-win  <INSTRUCTIONS> # AGENTS.md  ## Project Scop... |
| `019d043b-dc26-7db2-911a-f41764a0f67e` | # AGENTS.md instructions for C:\Users\yuuji\ghostty-win  <INSTRUCTIONS> # AGENTS.md  ## Project Scop... |
| `session-2026-03-19T07-39-db08116b` | C:\Users\yuuji\ghostty-win\src\apprt\winui3\App.zig を読んで、initXaml関数の処理ステッ... |


