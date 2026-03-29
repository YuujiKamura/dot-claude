---
name: semantic-issue-audit-redirection
description: "Testing & QA. (Semantic Issue-to-Commit Verification) Use when user mentions: test, unit test, integration, coverage, mock, assertion, TDD, fixture."
categories: [Automation, Ghostty, IME, Integration Test, TSF, Verification]
sources: [21044f1b-620a-4d82-9fb3-5fe41143594e, 61878fba-54b6-4ff8-9acd-d6644fd5fc45]
---

# Testing & QA

Patterns: 1

## 1. Semantic Issue-to-Commit Verification

Ensuring the AI prioritizes checking if a fix semantically satisfies an issue over performing generic git/workflow tasks.

### Steps

1. AI attempted to proceed with generic commit/push operations and environment updates after a TSF fix.
2. [INTERVENTION] User: 'そっちじゃない、CP関連のイシューが正しく更新と対応してるか調べろ' (Not that way, check if CP-related issues are correctly updated and handled).
3. The user redirected the AI to verify the actual resolution status of tracked issues rather than just managing files and commands.


## Source

| Conversation | Excerpt |
|---|---|
| `21044f1b-620a-4d82-9fb3-5fe41143594e` | 今のゴーストティの日本語入力、めっちゃドリフトするんでまず起動テス... |
| `61878fba-54b6-4ff8-9acd-d6644fd5fc45` | コミット済み。bf9da5a7a Fix TSF preedit display and input drift during IME composition。    ... |


