---
name: terminal-session-state-debugging
description: "Testing & QA. (Stale Session Detection in Terminal Control Planes) Use when user mentions: test, unit test, integration, coverage, mock, assertion, TDD, fixture."
categories: [IME fix, automated-test, ghostty, ime, regression, test, test-scripts, uiautomation, unit-test, verification, windows-terminal]
sources: [21044f1b-620a-4d82-9fb3-5fe41143594e, 61878fba-54b6-4ff8-9acd-d6644fd5fc45, session-2026-03-19T10-26-db08116b]
---

# Testing & QA

Patterns: 1

## 1. Stale Session Detection in Terminal Control Planes

Diagnostic strategy for distinguishing between genuine code regressions and environment pollution caused by 'DEAD sessions' in terminal agent/control plane testing.

### Steps

1. Terminal agents (like `agent-ctl`) maintain session state that outlives the terminal process; force-killing the frontend (`ghostty.exe`) without a clean shutdown signal results in 'DEAD sessions' that trigger false assertions in subsequent test runs.
2. Assertion failures in control plane smoke tests (e.g., `test-02d-control-plane`) following a forced process termination should be treated as environment pollution (stale session IDs) rather than regressions in the TSF or UI code.
3. When a push is blocked by unrelated test failures after a crash, the 'audit first' principle applies: verify if the test runner is mistakenly targeting an orphaned session record instead of the newly launched instance before attempting code fixes.

### Examples

```
FAIL: Assertion failed: test-02d-control-plane - agent-ctl smoke passed
```


## Source

| Conversation | Excerpt |
|---|---|
| `61878fba-54b6-4ff8-9acd-d6644fd5fc45` | コミット済み。bf9da5a7a Fix TSF preedit display and input drift during IME composition。    ... |
| `session-2026-03-19T10-26-db08116b` | Windows Terminalリポジトリ(https://github.com/microsoft/terminal)を調査しろ。知りたい... |
| `21044f1b-620a-4d82-9fb3-5fe41143594e` | 今のゴーストティの日本語入力、めっちゃドリフトするんでまず起動テス... |


