---
name: tsf-ime-regression-analysis
description: "Testing & QA. (TSF Preedit & Drift Logic Recovery) Use when user mentions: test, unit test, integration, coverage, mock, assertion, TDD, fixture."
categories: [Ghostty, IME, UAF, Windows, coverage, ghostty, ime, issue-tracking, lifecycle, memory-safety, powershell, ps1, qa, regression, regression-verification, test, testing, tsf, uaf, verification, winui3, zig]
sources: [61878fba-54b6-4ff8-9acd-d6644fd5fc45, b90d05b9-0e63-4148-bbdb-80277822f82c, 1934452f-726c-4c21-9bad-ca3fd813debb, 33908a93-335d-41ec-a906-d7f2ae791545]
---

# Testing & QA

Patterns: 1

## 1. TSF Preedit & Drift Logic Recovery

Detecting and fixing TSF (Text Services Framework) regressions by targeted comparison of state synchronization logic.

### Steps

1. Visual regression sensitivity: IME preedit display and 'input drift' (cursor misalignment during composition) are fragile and often missed by standard unit tests.
2. Archive-based comparison: When refactoring large terminal surface files, use 'archive' branches of known-good states to specifically audit the presence of `preeditCalc` and attribute updates.
3. Identifying logic gaps: Regressions in complex TSF implementations often stem from missing small state-sync calls during event handler migration rather than high-level logic errors.

### Examples

```bash
# Audit specific logic blocks against working archive
git show archive/working-branch:src/apprt/winui3/Surface_generic.zig | grep -n "preedit"
```


## Source

| Conversation | Excerpt |
|---|---|
| `33908a93-335d-41ec-a906-d7f2ae791545` | The reviewer flags UAF risk. Let me verify that closeSurface doesn't free memory immediately:  ● S... |
| `1934452f-726c-4c21-9bad-ca3fd813debb` | ghostty issue 114を更新、テスト整備が適切か？調査 |
| `61878fba-54b6-4ff8-9acd-d6644fd5fc45` | コミット済み。bf9da5a7a Fix TSF preedit display and input drift during IME composition。    ... |
| `b90d05b9-0e63-4148-bbdb-80277822f82c` | Issue #112 TSF退行修正。preeditが画面に出ない。git show archive/issue113-refactor-broke... |


