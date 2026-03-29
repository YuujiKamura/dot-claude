---
name: ghostty-ime-tsf-qa
description: "Testing & QA. (TSF IME Input & Drift Validation) Use when user mentions: test, unit test, integration, coverage, mock, assertion, TDD, fixture."
categories: [IME fix, automated-test, ghostty, ime, regression, test, test-scripts, uiautomation, unit-test, verification, windows-terminal]
sources: [61878fba-54b6-4ff8-9acd-d6644fd5fc45, session-2026-03-19T10-26-db08116b, 21044f1b-620a-4d82-9fb3-5fe41143594e]
---

# Testing & QA

Patterns: 1

## 1. TSF IME Input & Drift Validation

Handling Japanese IME in WinUI3-based terminal emulators requires specialized TSF (Text Services Framework) testing to prevent preedit text drifting that standard ASCII keyboard tests fail to detect.

### Steps

1. Japanese IME validation must prioritize monitoring the transient *preedit* state (text-in-progress) rather than just the final *commit* event; drifting usually occurs in the TSF buffer before characters are formally sent to the terminal.
2. Generic ASCII input tests are insufficient for IME-heavy applications; specialized scenarios (e.g., `test-05-ime-input.ps1`) are mandatory to verify visual stability and proper TSF state-sync.
3. If IME input fails to register entirely ('入力できねーぞ'), the diagnostic priority should be the TSF initialization sequence and WinUI3 Island attachment points, rather than high-level application input logic.

### Examples

```
./test-05-ime-input.ps1
```

```
./build-winui3-islands.sh
```


## Source

| Conversation | Excerpt |
|---|---|
| `61878fba-54b6-4ff8-9acd-d6644fd5fc45` | コミット済み。bf9da5a7a Fix TSF preedit display and input drift during IME composition。    ... |
| `session-2026-03-19T10-26-db08116b` | Windows Terminalリポジトリ(https://github.com/microsoft/terminal)を調査しろ。知りたい... |
| `21044f1b-620a-4d82-9fb3-5fe41143594e` | 今のゴーストティの日本語入力、めっちゃドリフトするんでまず起動テス... |


