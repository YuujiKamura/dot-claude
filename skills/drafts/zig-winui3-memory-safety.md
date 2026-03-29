---
name: zig-winui3-memory-safety
description: "Testing & QA. (Synchronous Destruction UAF Prevention) Use when user mentions: test, unit test, integration, coverage, mock, assertion, TDD, fixture."
categories: [Ghostty, IME, UAF, Windows, coverage, ghostty, ime, issue-tracking, lifecycle, memory-safety, powershell, ps1, qa, regression, regression-verification, test, testing, tsf, uaf, verification, winui3, zig]
sources: [33908a93-335d-41ec-a906-d7f2ae791545, 1934452f-726c-4c21-9bad-ca3fd813debb, b90d05b9-0e63-4148-bbdb-80277822f82c, 61878fba-54b6-4ff8-9acd-d6644fd5fc45]
---

# Testing & QA

Patterns: 1

## 1. Synchronous Destruction UAF Prevention

Prevents Use-After-Free (UAF) in Zig/WinUI3 callbacks where a synchronous operation (like closeSurface) immediately destroys the object context.

### Steps

1. Identifying synchronous destruction: Functions that trigger immediate `deinit` and `destroy` within a callback (e.g., `closeSurface` -> `closeTab`) make any subsequent access to `self` or its fields a memory safety violation.
2. Evaluating 'isSurfaceAlive' safety: Pointer-only comparisons (comparing addresses) are safe for aliveness checks, but any field dereference (like `self.closed`) on the same pointer after destruction is undefined behavior.
3. Judgment criterion: If memory is freed but not zeroed, field access might 'seem' to work but creates a race condition. Always check state flags *before* the destruction-triggering call or use a stable external manager reference.

### Examples

```zig
// UNSAFE: self is freed after closeSurface returns synchronously
self.app.closeSurface(self);
if (self.closed) return;
```

```zig
// SAFER: Preserve state locally or use core_initialized check
const was_closed = self.closed;
self.app.closeSurface(self);
if (was_closed) return;
```


## Source

| Conversation | Excerpt |
|---|---|
| `33908a93-335d-41ec-a906-d7f2ae791545` | The reviewer flags UAF risk. Let me verify that closeSurface doesn't free memory immediately:  ● S... |
| `1934452f-726c-4c21-9bad-ca3fd813debb` | ghostty issue 114を更新、テスト整備が適切か？調査 |
| `61878fba-54b6-4ff8-9acd-d6644fd5fc45` | コミット済み。bf9da5a7a Fix TSF preedit display and input drift during IME composition。    ... |
| `b90d05b9-0e63-4148-bbdb-80277822f82c` | Issue #112 TSF退行修正。preeditが画面に出ない。git show archive/issue113-refactor-broke... |


