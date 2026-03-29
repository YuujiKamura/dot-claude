---
name: rust-win32-ffi
description: "Testing & QA. (FFI Encoding Boundary Mismatch) Use when user mentions: test, unit test, integration, coverage, mock, assertion, TDD, fixture."
categories: [Ghostty, PowerShell, UI Automation, UIA, WinUI3, Zig, agent-relay, automation, bug-fix, codex, debugging, full-cycle, ghostty, observer, powershell, regression, rust, test, test-runner, testing, unit test, zig]
sources: [019d0a88-a7e2-7c41-87b1-36235d9688b3, 019d0a53-6fc0-7a00-ac36-d8fd6d9068e1, 019d0a33-9937-7040-a3db-144bf6dd2d1e, badcf37d-2773-42da-9188-3e0e7665623d, 214201b8-edfa-4539-a2a8-461bdcbd1c9f, 019d0a4a-6008-78d2-8ecd-e4e922ed96a4, 2c86c97c-dc29-4295-bbd8-72031a88287b, 019d0a3d-b481-7fe2-94a6-21470a809e04, c42de711-110d-49be-b7ed-740b942448eb, 019d0a8c-3fa4-7392-a290-40875bebe972, 019d0a44-8a22-75c1-9b33-248629974a86, 019d0a5b-2859-7a80-be65-63e182bb3679]
---

# Testing & QA

Patterns: 1

## 1. FFI Encoding Boundary Mismatch

Text garbling in IPC/FFI pipelines (like 'CP INPUT') often stems from UTF-16 vs UTF-8 mismatches at the boundary between Windows-native components and Rust backends.

### Steps

1. When IPC messages are received but content is garbled, prioritize auditing the decoding primitive (e.g., `from_utf16` vs `from_utf8`) at the FFI boundary over investigating transport or control plane logic.
2. Do not assume a high pass rate (e.g., 10/11) rules out encoding issues; specific character sequences or keyboard-heavy tests can trigger latent encoding bugs that simpler tests miss.
3. Avoid excessive cross-file tracing for suspected transport issues until the data integrity at the entry/exit points (FFI) is verified.

### Examples

```
// Error: Received UTF-8 bytes but decoded as UTF-16
let s = String::from_utf16_lossy(bytes);

// Fix: Corrected to match the actual stream encoding
let s = String::from_utf8_lossy(bytes);
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


