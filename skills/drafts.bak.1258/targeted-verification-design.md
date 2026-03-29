---
name: targeted-verification-design
description: "Testing & QA. (Avoiding Performative Testing) Use when user mentions: test, unit test, integration, coverage, mock, assertion, TDD, fixture."
categories: [Ghostty, IME, UAF, Windows, coverage, ghostty, ime, issue-tracking, lifecycle, memory-safety, powershell, ps1, qa, regression, regression-verification, test, testing, tsf, uaf, verification, winui3, zig]
sources: [33908a93-335d-41ec-a906-d7f2ae791545, 1934452f-726c-4c21-9bad-ca3fd813debb, b90d05b9-0e63-4148-bbdb-80277822f82c, 61878fba-54b6-4ff8-9acd-d6644fd5fc45]
---

# Testing & QA

Patterns: 1

## 1. Avoiding Performative Testing

Shifting from generic 'pass/fail' build commands to targeted verification of specific logic transitions.

### Steps

1. Defining 'Atomic Verification Goals': Generic `zig build test` runs are often performative. Effective practitioners define specific goals: 'Confirm the closed flag transitions' or 'Verify std.log capture'.
2. Refactoring sequence: When AI lacks test clarity, the user taught to 'revert to known-good', establish infrastructure for the specific fix, and then re-apply changes to ensure measurable correctness.
3. Log-based verification: In complex GUI environments where unit tests are hard to write, using targeted log output (`std.log`) to verify internal state transitions is a primary validation strategy.

### Examples

```zig
// Instead of generic test runs, focus on:
// 1. State change: surface.closed == true
// 2. Side effect: log entry for 'Surface destroyed' exists
```


## Source

| Conversation | Excerpt |
|---|---|
| `33908a93-335d-41ec-a906-d7f2ae791545` | The reviewer flags UAF risk. Let me verify that closeSurface doesn't free memory immediately:  ● S... |
| `1934452f-726c-4c21-9bad-ca3fd813debb` | ghostty issue 114を更新、テスト整備が適切か？調査 |
| `61878fba-54b6-4ff8-9acd-d6644fd5fc45` | コミット済み。bf9da5a7a Fix TSF preedit display and input drift during IME composition。    ... |
| `b90d05b9-0e63-4148-bbdb-80277822f82c` | Issue #112 TSF退行修正。preeditが画面に出ない。git show archive/issue113-refactor-broke... |


