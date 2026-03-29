---
name: a2a-orchestration-topology
description: "all. (Agent-to-Agent Communication Topology) Use when user mentions: ."
categories: [agent-ctl, agents, bash, bug-fix, build, ci, claude, clipboard, dll, ghostty, hacking, ime, installer, llm, manual, markdown, powershell, refactoring, rust, selection, state-management, test, verification, win32, windows-terminal, winui3, zig]
sources: [3e7264ca-8ef5-4b04-9e85-b82c8f015058, ebcb4915-cc8b-4d0c-b824-66150c8c4129, 61878fba-54b6-4ff8-9acd-d6644fd5fc45, 5466f2b8-2bef-45e5-8f06-029174f01631, dd7b2921-18d4-43e9-9b70-d636e46c5344, fe2768a4-9113-4363-954f-fa62f7acc45e, 21044f1b-620a-4d82-9fb3-5fe41143594e, d658da03-ff03-4991-9a92-52bd28ea5663, 27539c54-c470-44d1-be81-866ab138945e, ec757810-d889-4790-8432-334956944d19]
---

# all

Patterns: 1

## 1. Agent-to-Agent Communication Topology

Trade-offs between direct P2P agent interaction and centralized hub-and-spoke orchestration

### Steps

1. Direct P2P agent communication (N-body problem) was found to scale poorly (N*(N-1)/2 paths) and exhaust context windows quickly.
2. Centralized orchestration (Hub & Spoke) with asynchronous task dispatch was identified as the industry-standard winner for scaling to 3+ agents.
3. The value of the 'agent-relay' project was pivotally redefined as 'low-level terminal control' (Control Plane) rather than the communication protocol itself.
4. git worktree was used to isolate agent file-system modifications while maintaining a shared repository history.
5. tmux (and its Windows equivalent, WT Control Plane) provided the mechanism for persistent, scriptable terminal interaction for agents.


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


