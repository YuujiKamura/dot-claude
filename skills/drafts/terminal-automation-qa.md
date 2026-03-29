---
name: terminal-automation-qa
description: "Testing & QA. (Shared-Session Buffer Pollution) Use when user mentions: test, unit test, integration, coverage, mock, assertion, TDD, fixture."
categories: [Ghostty, PowerShell, UI Automation, UIA, WinUI3, Zig, agent-relay, automation, bug-fix, codex, debugging, full-cycle, ghostty, observer, powershell, regression, rust, test, test-runner, testing, unit test, zig]
sources: [019d0a8c-3fa4-7392-a290-40875bebe972, c42de711-110d-49be-b7ed-740b942448eb, 019d0a53-6fc0-7a00-ac36-d8fd6d9068e1, 019d0a3d-b481-7fe2-94a6-21470a809e04, 019d0a33-9937-7040-a3db-144bf6dd2d1e, 019d0a4a-6008-78d2-8ecd-e4e922ed96a4, 2c86c97c-dc29-4295-bbd8-72031a88287b, 019d0a88-a7e2-7c41-87b1-36235d9688b3, 214201b8-edfa-4539-a2a8-461bdcbd1c9f, 019d0a5b-2859-7a80-be65-63e182bb3679, badcf37d-2773-42da-9188-3e0e7665623d, 019d0a44-8a22-75c1-9b33-248629974a86]
---

# Testing & QA

Patterns: 1

## 1. Shared-Session Buffer Pollution

UIA tests for terminal applications often fail due to 'buffer pollution' when multiple tests run sequentially in the same session. Lingering state, unconsumed input, or scrollback content from previous tests cause non-deterministic failures in subsequent ones.

### Steps

1. Recognize that sequential execution in a single terminal instance creates hidden state dependencies; a failure in test N often triggers a false negative in test N+1 due to unconsumed input or lingering screen content.
2. Avoid 'band-aid' fixes like injecting `cls` (clear screen) into individual tests; true isolation requires resetting the terminal state or spawning fresh sessions/processes per test case to ensure a clean slate.
3. Distinguish between a 'broken system' (bug in the app) and a 'broken test design' (architectural flaw in the test runner's orchestration of sessions).

### Examples

```
cls # Ineffective: clears view but doesn't flush the input buffer or reset session state
```

```
Stop-Process -Name ghostty; Start-Process ghostty # Better: ensures isolation by restarting the host
```


## Source

| Conversation | Excerpt |
|---|---|
| `019d0a5b-2859-7a80-be65-63e182bb3679` | <environment_context>   <cwd>C:\Users\yuuji</cwd>   <shell>powershell</shell>   <current_date>2026-0... |
| `019d0a53-6fc0-7a00-ac36-d8fd6d9068e1` | <environment_context>   <cwd>C:\Users\yuuji</cwd>   <shell>powershell</shell>   <current_date>2026-0... |
| `019d0a4a-6008-78d2-8ecd-e4e922ed96a4` | <environment_context>   <cwd>C:\Users\yuuji</cwd>   <shell>powershell</shell>   <current_date>2026-0... |
| `019d0a44-8a22-75c1-9b33-248629974a86` | <environment_context>   <cwd>C:\Users\yuuji</cwd>   <shell>powershell</shell>   <current_date>2026-0... |
| `019d0a3d-b481-7fe2-94a6-21470a809e04` | <environment_context>   <cwd>C:\Users\yuuji</cwd>   <shell>powershell</shell>   <current_date>2026-0... |
| `019d0a33-9937-7040-a3db-144bf6dd2d1e` | <environment_context>   <cwd>C:\Users\yuuji</cwd>   <shell>powershell</shell>   <current_date>2026-0... |
| `019d0a8c-3fa4-7392-a290-40875bebe972` | <environment_context>   <cwd>C:\Users\yuuji</cwd>   <shell>powershell</shell>   <current_date>2026-0... |
| `019d0a88-a7e2-7c41-87b1-36235d9688b3` | <environment_context>   <cwd>C:\Users\yuuji</cwd>   <shell>powershell</shell>   <current_date>2026-0... |
| `2c86c97c-dc29-4295-bbd8-72031a88287b` | codexにゴーストティウィンの129イシューの直しをやらせたらなんかUIAテス... |
| `badcf37d-2773-42da-9188-3e0e7665623d` | エージェントリレーの現状を確認、ゴーストティのUIAテストで使ってるん... |
| `c42de711-110d-49be-b7ed-740b942448eb` | ゴーストティのUIAテストPASSしてるやつまで毎回実行してダサすぎるのでチ... |
| `214201b8-edfa-4539-a2a8-461bdcbd1c9f` | ● まとめ    修正内容:   - control-plane-server/src/ffi.rs: from_utf16_lossy → from_utf8_l... |


