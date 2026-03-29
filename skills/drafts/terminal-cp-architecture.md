---
name: terminal-cp-architecture
description: "CLI & Tooling. (Inlined vs. DLL-based Terminal Control Plane Migration) Use when user mentions: CLI, script, automation, tool, plugin, extension, config."
categories: [Bash, Bug Fix, DLL, FFI, Feature Implementation, Ghostty, IME, Migration, Selection, Terminal, UI, WinUI3, Windows Terminal, Zig]
sources: [ebcb4915-cc8b-4d0c-b824-66150c8c4129, ec757810-d889-4790-8432-334956944d19, fe2768a4-9113-4363-954f-fa62f7acc45e, dd7b2921-18d4-43e9-9b70-d636e46c5344, 27539c54-c470-44d1-be81-866ab138945e]
---

# CLI & Tooling

Patterns: 1

## 1. Inlined vs. DLL-based Terminal Control Plane Migration

Strategies for replacing forked/inlined control logic with modular DLL implementations in Windows Terminal environments.

### Steps

1. Found that Windows Terminal 'Dev version' had control plane logic manually inlined into the Cascadia codebase, creating maintenance debt compared to the standalone control-plane-server DLL.
2. [INTERVENTION] User: 'おかしい。指示と違って、ゴーストティの変更になるのはなんでだ。WindowsTerminalのDev版の話をしてるのに' — Corrected the AI when it mistakenly targeted Ghostty source files instead of the Windows Terminal fork.
3. AI misinterpreted 'WT CP' as Ghostty's internal win32/control_plane.zig (579 lines) because it was unaware the user was working on a custom fork of Windows Terminal.
4. The terminal-control-plane repository was found to be archived, which initially led the AI to assume the logic had been consolidated into the terminal app rather than moved to a DLL.
5. The migration strategy required freezing the legacy inlined C++ implementation in WT and replacing it with FFI calls to a new control-plane-server DLL.


## Source

| Conversation | Excerpt |
|---|---|
| `ebcb4915-cc8b-4d0c-b824-66150c8c4129` | Implement the following plan:  # ghostty-win 日本語IME入力修正計画  ## Context ghostty-win... |
| `fe2768a4-9113-4363-954f-fa62f7acc45e` | WTのCPをDLLプロジェクト版に置き換えて内挿してる旧版を除去しろ。チーム... |
| `dd7b2921-18d4-43e9-9b70-d636e46c5344` | - テキスト選択の選択色修正（WTの実装を移植）   - ControlInteractivity.cppのZig... |
| `ec757810-d889-4790-8432-334956944d19` | ghostty WinUI3にテキスト選択コピーを実装しろ。WTのControlInteractivity.cppを参考... |
| `27539c54-c470-44d1-be81-866ab138945e` | bash |


