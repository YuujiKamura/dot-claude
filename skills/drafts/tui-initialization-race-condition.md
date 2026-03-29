---
name: tui-initialization-race-condition
description: "all. (TUI Ready-State Race Conditions) Use when user mentions: ."
categories: [AGENTS.md, AI Agents, Agent, Automation, Bash, Build, CLI, DLL, Docs, Documentation, FFI, Fix Validation, Ghostty, Guide, IME, Implementation, Integration Test, LLM, PowerShell, Prompt, README, Rust, Script, State Management, TSF, Terminal, Tutorial, UI, Unit Test, Validation, Verification, WinUI3, Windows Terminal, Zig, agent, ai-agents, bash, bug-fix, build-system, ci, clipboard, config, dll, docs, feature, files, gemini, ghostty, git, ime, llm, manual, migration, powershell, refactoring, regression-test, rust, shell, state-management, testing, tsf, tutorial, ui, verification, windows, windows-terminal, zig]
sources: [5466f2b8-2bef-45e5-8f06-029174f01631, dd7b2921-18d4-43e9-9b70-d636e46c5344, 3e7264ca-8ef5-4b04-9e85-b82c8f015058, 27539c54-c470-44d1-be81-866ab138945e, ebcb4915-cc8b-4d0c-b824-66150c8c4129, 61878fba-54b6-4ff8-9acd-d6644fd5fc45, fe2768a4-9113-4363-954f-fa62f7acc45e, 21044f1b-620a-4d82-9fb3-5fe41143594e, ec757810-d889-4790-8432-334956944d19, d658da03-ff03-4991-9a92-52bd28ea5663]
---

# all

Patterns: 1

## 1. TUI Ready-State Race Conditions

Detecting actual input readiness in interactive CLI agents

### Events

1. Keystrokes sent immediately after seeing the '❯' prompt in Claude Code were dropped because the TUI initialization wasn't finished.
2. The prompt character appeared in the buffer before the TUI event loop started listening for stdin.
3. [INTERVENTION] User: '時間で同行しようと考えてる時点で設計ミス' → AI realized that buffer-based 'Ready' detection needs to wait for secondary UI elements like the status bar.
4. Reliable 'Ready' detection was achieved by waiting for the 'bypass permissions' status text rather than just the prompt.


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


