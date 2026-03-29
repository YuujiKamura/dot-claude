---
name: terminal-logic-verbatim-translation
description: "Documentation. (1:1 Translation for Complex Terminal Logic) Use when user mentions: README, docs, documentation, tutorial, guide, comment."
categories: [AGENTS.md, Ghostty, code-explanation, configuration, documentation, ghostty-win, project-scope, terminal, winui3, zig]
sources: [d658da03-ff03-4991-9a92-52bd28ea5663, 019d0487-f3a6-7991-ada0-a0f220ee43c2, 019d0444-29fb-7523-9bc0-9433013476e5, 019d044e-a335-7271-9c12-67df66b02ece, session-2026-03-19T07-39-db08116b, 019d0459-74ac-75d1-8b91-d0ab99812e42, 019d043b-dc26-7db2-911a-f41764a0f67e]
---

# Documentation

Patterns: 1

## 1. 1:1 Translation for Complex Terminal Logic

Implementing terminal interactivity (selection, pointer mapping) from scratch is high-risk due to coordinate complexity. A strict 1:1 translation of proven C++ code (e.g., from Windows Terminal) provides a known-good baseline, preventing regressions that occur during 'idiomatic' rewrites.

### Steps

1. Prioritize 'mechanical' parity over 'Zig-idiomatic' code when migrating legacy C++ terminal interactivity to ensure mathematical correctness of coordinate mapping.
2. Map winrt::hstring directly to [:0]const u16 (UTF-16 null-terminated) to maintain memory layout compatibility with Windows APIs without intermediate allocations.
3. Translate C++ exceptions to Zig error unions to maintain the original control flow logic without introducing new state-management bugs.
4. Decouple translated logic into a standalone module (e.g., ControlInteractivity.zig) before attempting integration to allow for isolated unit testing against original C++ benchmarks.

### Examples

```
// C++: void OnPointerPressed(PointerEventArgs const& args)
// Zig equivalent for parity:
pub fn onPointerPressed(self: *Self, args: *const PointerEventArgs) anyerror!void { ... }
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


