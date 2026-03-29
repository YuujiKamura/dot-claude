---
name: ime-input-drift-validation
description: "Testing & QA. (IME Input Drift and Startup Test Integration) Use when user mentions: test, unit test, integration, coverage, mock, assertion, TDD, fixture."
categories: [Automation, Ghostty, IME, Integration Test, TSF, Verification]
sources: [61878fba-54b6-4ff8-9acd-d6644fd5fc45, 21044f1b-620a-4d82-9fb3-5fe41143594e]
---

# Testing & QA

Patterns: 1

## 1. IME Input Drift and Startup Test Integration

Validation of Japanese input stability and the inclusion of IME scenarios in early startup tests.

### Steps

1. User identified 'heavy drift' in Japanese input (Ghostty Win) and required adding IME input scenarios to startup tests to ensure baseline stability.
2. [INTERVENTION] User: '入力できねーぞ' (I can't input!) after the AI added IME input to startup tests, indicating the automated script failed to bridge the gap between process startup and actual input processing readiness.
3. Fix bf9da5a7a specifically addressed 'TSF preedit display' to resolve input drift during IME composition.


## Source

| Conversation | Excerpt |
|---|---|
| `21044f1b-620a-4d82-9fb3-5fe41143594e` | 今のゴーストティの日本語入力、めっちゃドリフトするんでまず起動テス... |
| `61878fba-54b6-4ff8-9acd-d6644fd5fc45` | コミット済み。bf9da5a7a Fix TSF preedit display and input drift during IME composition。    ... |


