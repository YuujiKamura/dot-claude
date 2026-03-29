---
name: llm-agent-observer
description: "all. (LLM-Based Terminal State Observation) Use when user mentions: ."
categories: [agent-ctl, agents, bash, bug-fix, build, ci, claude, clipboard, dll, ghostty, hacking, ime, installer, llm, manual, markdown, powershell, refactoring, rust, selection, state-management, test, verification, win32, windows-terminal, winui3, zig]
sources: [5466f2b8-2bef-45e5-8f06-029174f01631, 3e7264ca-8ef5-4b04-9e85-b82c8f015058, dd7b2921-18d4-43e9-9b70-d636e46c5344, 21044f1b-620a-4d82-9fb3-5fe41143594e, ec757810-d889-4790-8432-334956944d19, 27539c54-c470-44d1-be81-866ab138945e, 61878fba-54b6-4ff8-9acd-d6644fd5fc45, fe2768a4-9113-4363-954f-fa62f7acc45e, d658da03-ff03-4991-9a92-52bd28ea5663, ebcb4915-cc8b-4d0c-b824-66150c8c4129]
---

# all

Patterns: 1

## 1. LLM-Based Terminal State Observation

Replacing brittle string-matching patterns with LLM visual judgment for agent state tracking

### Steps

1. Hardcoded regex patterns for agent states (READY/APPROVAL) frequently broke due to minor CLI UI updates from vendors.
2. LLM (Gemini) was used to interpret terminal buffers and categorize states based on visual descriptions instead of string matching.
3. Polling interval for LLM state judgment was set to 5 seconds to balance state accuracy with API latency and cost.
4. States were refined to distinguish between READY (initial idle) and DONE (task completion) to prevent orchestration loops.
5. [INTERVENTION] User: 'LLM判定をパターンと比較するとか機械的に出来るわけがない' -> AI stopped trying to hybridize LLM judgment with keyword matchers.
6. [INTERVENTION] User: 'キーワード対応で機械判定しないようにする' -> Pattern dictionary was redefined as semantic visual descriptions for LLM reference instead of literal strings.

### Examples

```
// Refined states for LLM-based Librarian
["IDLE", "STARTING", "READY", "WORKING", "APPROVAL", "DONE"]
```


## Source

| Conversation | Excerpt |
|---|---|
| `ebcb4915-cc8b-4d0c-b824-66150c8c4129` | Implement the following plan:  # ghostty-win 日本語IME入力修正計画  ## Context ghostty-win... |
| `5466f2b8-2bef-45e5-8f06-029174f01631` | Implement the following plan:  # 司書オブザーバー: LLMベース状態管理  ## Context  age... |
| `21044f1b-620a-4d82-9fb3-5fe41143594e` | 今のゴーストティの日本語入力、めっちゃドリフトするんでまず起動テス... |
| `fe2768a4-9113-4363-954f-fa62f7acc45e` | WTのCPをDLLプロジェクト版に置き換えて内挿してる旧版を除去しろ。チーム... |
| `dd7b2921-18d4-43e9-9b70-d636e46c5344` | - テキスト選択の選択色修正（WTの実装を移植）   - ControlInteractivity.cppのZig... |
| `d658da03-ff03-4991-9a92-52bd28ea5663` | ゴーストティの公式のドキュメントを読み聞かせて |
| `ec757810-d889-4790-8432-334956944d19` | ghostty WinUI3にテキスト選択コピーを実装しろ。WTのControlInteractivity.cppを参考... |
| `27539c54-c470-44d1-be81-866ab138945e` | bash |
| `3e7264ca-8ef5-4b04-9e85-b82c8f015058` | AI and Agents If you're using AI assistance with Ghostty, Ghostty provides an AGENTS.md file read by... |
| `61878fba-54b6-4ff8-9acd-d6644fd5fc45` | コミット済み。bf9da5a7a Fix TSF preedit display and input drift during IME composition。    ... |


