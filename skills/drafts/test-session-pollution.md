---
name: test-session-pollution
description: "Testing & QA. (Dead Session Remnants in Control Plane Testing) Use when user mentions: test, unit test, integration, coverage, mock, assertion, TDD, fixture."
categories: [Automation, Ghostty, IME, Integration Test, TSF, Verification]
sources: [21044f1b-620a-4d82-9fb3-5fe41143594e, 61878fba-54b6-4ff8-9acd-d6644fd5fc45]
---

# Testing & QA

Patterns: 1

## 1. Dead Session Remnants in Control Plane Testing

Identifying false negatives caused by stale process state and session ID confusion in test runners.

### Steps

1. Pre-push tests (test-02d-control-plane, test-02e-agent-roundtrip) failed after a successful TSF fix build.
2. Investigation revealed the failures were caused by 'DEAD session remnants'—the control plane and agent-ctl mixed current session state with stale data from previously killed Ghostty instances.
3. Found that simply killing the ghostty.exe process (taskkill) was insufficient if the test runner did not account for persistent control plane state or session ID reuse.


## Source

| Conversation | Excerpt |
|---|---|
| `21044f1b-620a-4d82-9fb3-5fe41143594e` | 今のゴーストティの日本語入力、めっちゃドリフトするんでまず起動テス... |
| `61878fba-54b6-4ff8-9acd-d6644fd5fc45` | コミット済み。bf9da5a7a Fix TSF preedit display and input drift during IME composition。    ... |


