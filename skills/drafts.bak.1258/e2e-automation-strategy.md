---
name: e2e-automation-strategy
description: "Testing & QA. (Identifying Framework-Level Automation Gaps) Use when user mentions: test, unit test, integration, coverage, mock, assertion, TDD, fixture."
---

# Testing & QA

Patterns: 1

## 1. Identifying Framework-Level Automation Gaps

Recognizing when a bug is 'un-automatable' via standard tools allows a strategic pivot to 'Internal-E2E', where test hooks are compiled directly into the binary to expose hidden event paths.

### Steps

1. When UI automation stalls or fails to reproduce a manual bug, the root cause is often the abstraction layer of the automation driver (e.g., a driver simulating 'Keyboard' vs 'IME' input).
2. The failure of 'Standard Delegation' (e.g., asking an LLM to just 'run a test script') is a signal that the underlying input interface is fundamentally bypassing the code path under investigation.
3. Instead of fighting external automation tools, build 'Testability Hooks' into the application logic that allow external scripts to trigger internal, private framework methods.

### Examples

```powershell
# Example of the pivot: Moving from UI clicking to a custom command
./ghostty.exe --control-plane "IME_INJECT|$( [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes('あ')) )"
```



