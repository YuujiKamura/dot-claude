---
name: winui3-zig-release-diagnostics
description: "Documentation. (WinUI3 Release-Mode Diagnostics in Zig) Use when user mentions: README, docs, documentation, tutorial, guide, comment."
categories: [AGENTS.md, Ghostty, code-explanation, configuration, documentation, ghostty-win, project-scope, terminal, winui3, zig]
sources: [d658da03-ff03-4991-9a92-52bd28ea5663, session-2026-03-19T07-39-db08116b, 019d0444-29fb-7523-9bc0-9433013476e5, 019d0487-f3a6-7991-ada0-a0f220ee43c2, 019d0459-74ac-75d1-8b91-d0ab99812e42, 019d044e-a335-7271-9c12-67df66b02ece, 019d043b-dc26-7db2-911a-f41764a0f67e]
---

# Documentation

Patterns: 1

## 1. WinUI3 Release-Mode Diagnostics in Zig

ReleaseFast builds in Zig often mask WinRT initialization crashes (like E_NOTIMPL) because @setRuntimeSafety(false) removes panic traces. Explicit diagnostic logging at every XAML setup step is required to pinpoint which projected API is failing when standard debuggers are unavailable.

### Steps

1. Treat E_NOTIMPL (0x80004001) during initXaml as a signature of a missing or incorrectly projected WinUI3 interface implementation rather than a logic bug.
2. Manually instrument every initialization step with numeric IDs; when ReleaseFast crashes, the last successful log ID isolates the failing WinRT call.
3. Bypass the lack of runtime safety by inserting custom logging before/after suspected WinRT calls to confirm return codes (HRESULT) manually.

### Examples

```
// Inside src/apprt/winui3/App.zig
log.debug("initXaml step 8: Configuring window...", .{});
const hr = self.xaml_window.init();
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


