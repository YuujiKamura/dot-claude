---
name: terminal-conceptual-model
description: "all. (Terminal Emulator vs Shell Host Conceptual Model) Use when user mentions: ."
categories: [agent-ctl, agents, bash, bug-fix, build, ci, claude, clipboard, dll, ghostty, hacking, ime, installer, llm, manual, markdown, powershell, refactoring, rust, selection, state-management, test, verification, win32, windows-terminal, winui3, zig]
sources: [3e7264ca-8ef5-4b04-9e85-b82c8f015058, ebcb4915-cc8b-4d0c-b824-66150c8c4129, ec757810-d889-4790-8432-334956944d19, 21044f1b-620a-4d82-9fb3-5fe41143594e, 5466f2b8-2bef-45e5-8f06-029174f01631, fe2768a4-9113-4363-954f-fa62f7acc45e, d658da03-ff03-4991-9a92-52bd28ea5663, 61878fba-54b6-4ff8-9acd-d6644fd5fc45, dd7b2921-18d4-43e9-9b70-d636e46c5344, 27539c54-c470-44d1-be81-866ab138945e]
---

# all

Patterns: 1

## 1. Terminal Emulator vs Shell Host Conceptual Model

Understanding the modern role of terminal applications as GPU renderers and IME hosts

### Steps

1. The term 'Emulator' was identified as a legacy retonym; modern apps host real shells rather than emulating physical hardware.
2. The PTY (Pseudo-Terminal) layer was clarified as being provided by the OS kernel, with the terminal app acting merely as a renderer/parser.
3. Modern terminal applications (Ghostty/WT) act primarily as GPU-accelerated renderers and IME hosts for OS-managed PTYs.
4. The use of terminals as IPC for AI agents (Agent-to-Agent communication) was noted as a temporary workaround for the lack of standardized binary protocols.


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


