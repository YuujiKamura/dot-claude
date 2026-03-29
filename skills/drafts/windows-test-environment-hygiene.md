---
name: windows-test-environment-hygiene
description: "Testing & QA. (Stale Session Cleanup for IPC Testing) Use when user mentions: test, unit test, integration, coverage, mock, assertion, TDD, fixture."
categories: [Ghostty, IME, UAF, Windows, coverage, ghostty, ime, issue-tracking, lifecycle, memory-safety, powershell, ps1, qa, regression, regression-verification, test, testing, tsf, uaf, verification, winui3, zig]
sources: [33908a93-335d-41ec-a906-d7f2ae791545, 61878fba-54b6-4ff8-9acd-d6644fd5fc45, 1934452f-726c-4c21-9bad-ca3fd813debb, b90d05b9-0e63-4148-bbdb-80277822f82c]
---

# Testing & QA

Patterns: 1

## 1. Stale Session Cleanup for IPC Testing

Distinguishing between code regressions and environmental pollution ('DEAD' sessions) in Windows GUI/IPC smoke tests.

### Steps

1. Diagnosing 'DEAD session' noise: Failures in control-plane or smoke tests (e.g. agent-ctl failures) are frequently caused by residual IPC states or zombie processes from previous crashes, not the latest commit.
2. Inadequacy of basic taskkill: Identifying that while `taskkill` stops the process, OS-level handles or IPC identifiers can persist, causing the next test instance to fail on initialization.
3. Workflow insight: Prioritize a 'scorched earth' cleanup (verifying process death and clearing stale session IDs) before attempting to debug logic failures in smoke tests.

### Examples

```powershell
# Example of clearing environment before re-testing
taskkill /F /IM ghostty.exe /T
# Wait for handle release before run-all-tests.ps1
```


## Source

| Conversation | Excerpt |
|---|---|
| `33908a93-335d-41ec-a906-d7f2ae791545` | The reviewer flags UAF risk. Let me verify that closeSurface doesn't free memory immediately:  ● S... |
| `1934452f-726c-4c21-9bad-ca3fd813debb` | ghostty issue 114を更新、テスト整備が適切か？調査 |
| `61878fba-54b6-4ff8-9acd-d6644fd5fc45` | コミット済み。bf9da5a7a Fix TSF preedit display and input drift during IME composition。    ... |
| `b90d05b9-0e63-4148-bbdb-80277822f82c` | Issue #112 TSF退行修正。preeditが画面に出ない。git show archive/issue113-refactor-broke... |


