---
name: winui3-terminal-ui-porting
description: "CLI & Tooling. (Porting Terminal Selection Logic to WinUI3/Zig) Use when user mentions: CLI, script, automation, tool, plugin, extension, config."
categories: [Bash, Bug Fix, DLL, FFI, Feature Implementation, Ghostty, IME, Migration, Selection, Terminal, UI, WinUI3, Windows Terminal, Zig]
sources: [ec757810-d889-4790-8432-334956944d19, fe2768a4-9113-4363-954f-fa62f7acc45e, 27539c54-c470-44d1-be81-866ab138945e, dd7b2921-18d4-43e9-9b70-d636e46c5344, ebcb4915-cc8b-4d0c-b824-66150c8c4129]
---

# CLI & Tooling

Patterns: 1

## 1. Porting Terminal Selection Logic to WinUI3/Zig

Implementing mouse-based text selection and clipboard operations in a Zig-based WinUI3 terminal using Windows Terminal as a reference.

### Steps

1. Windows Terminal's ControlInteractivity.cpp (PointerPressed/Moved/Released) served as the primary behavioral reference for implementing selection in Ghostty's winui3_surface.zig.
2. Direct Win32 APIs (OpenClipboard/SetClipboardData) were prioritized over WinUI3's high-level clipboard wrapper to ensure deterministic behavior in terminal emulator contexts.
3. Selection logic was split between UI event handlers (Pointer events) and the core terminal model (Selection.zig) to maintain separation of concerns.
4. Building the project via 'zig build' inside a running Ghostty instance was found to cause process failure ('suicide'), requiring execution from an external shell.


## Source

| Conversation | Excerpt |
|---|---|
| `ebcb4915-cc8b-4d0c-b824-66150c8c4129` | Implement the following plan:  # ghostty-win 日本語IME入力修正計画  ## Context ghostty-win... |
| `fe2768a4-9113-4363-954f-fa62f7acc45e` | WTのCPをDLLプロジェクト版に置き換えて内挿してる旧版を除去しろ。チーム... |
| `dd7b2921-18d4-43e9-9b70-d636e46c5344` | - テキスト選択の選択色修正（WTの実装を移植）   - ControlInteractivity.cppのZig... |
| `ec757810-d889-4790-8432-334956944d19` | ghostty WinUI3にテキスト選択コピーを実装しろ。WTのControlInteractivity.cppを参考... |
| `27539c54-c470-44d1-be81-866ab138945e` | bash |


