---
name: winrt-zig-bridge-conventions
description: "Documentation. (Zig-to-WinRT Binary Compatibility) Use when user mentions: README, docs, documentation, tutorial, guide, comment."
categories: [AGENTS.md, Ghostty, code-explanation, configuration, documentation, ghostty-win, project-scope, terminal, winui3, zig]
sources: [019d043b-dc26-7db2-911a-f41764a0f67e, d658da03-ff03-4991-9a92-52bd28ea5663, 019d0459-74ac-75d1-8b91-d0ab99812e42, 019d0487-f3a6-7991-ada0-a0f220ee43c2, 019d044e-a335-7271-9c12-67df66b02ece, 019d0444-29fb-7523-9bc0-9433013476e5, session-2026-03-19T07-39-db08116b]
---

# Documentation

Patterns: 1

## 1. Zig-to-WinRT Binary Compatibility

Bridging Zig to WinUI3 requires strict adherence to binary interface (ABI) conventions. Errors in type mapping (HSTRING to Zig slices) are the primary cause of 'Silent Failure' in Windows applications.

### Steps

1. Always use null-terminated UTF-16 for strings passed to WinRT projections to avoid memory corruption or 'Invalid Argument' errors from the COM layer.
2. Treat HRESULT values as first-class citizens in Zig error unions to ensure that WinUI3 failure codes (e.g., 0x80004001) are propagated correctly through the call stack.
3. Validate that @setRuntimeSafety(false) is only enabled after confirming that all WinRT interface handshakes are stable in a 'Debug' build first.

### Examples

```
const win = @import("win32");
const hstring = win.foundation.HSTRING;
// Mapping logic for parity
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


