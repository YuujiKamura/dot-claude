---
name: winrt-zig-binding-generation
description: "CLI & Tooling. (Automating WinRT/COM Bindings for Zig 0.15.2) Use when user mentions: CLI, script, automation, tool, plugin, extension, config."
categories: [Bash, Bug Fix, DLL, FFI, Feature Implementation, Ghostty, IME, Migration, Selection, Terminal, UI, WinUI3, Windows Terminal, Zig]
sources: [ec757810-d889-4790-8432-334956944d19, 27539c54-c470-44d1-be81-866ab138945e, dd7b2921-18d4-43e9-9b70-d636e46c5344, ebcb4915-cc8b-4d0c-b824-66150c8c4129, fe2768a4-9113-4363-954f-fa62f7acc45e]
---

# CLI & Tooling

Patterns: 1

## 1. Automating WinRT/COM Bindings for Zig 0.15.2

Using specialized tools to generate Zig interfaces from Windows Metadata (WinMD) files to support modern COM interaction.

### Steps

1. The win-zig-bindgen tool (located at C:\Users\yuuji\win-zig-bindgen) was updated to support Zig 0.15.2 requirements.
2. Bindings are generated from WinMD files using the --winmd and --iface arguments to ensure type-safe interaction with Windows system components.
3. Automated generation was used to prevent regressions when the Zig compiler changed its memory layout or calling conventions for COM-compatible types.


## Source

| Conversation | Excerpt |
|---|---|
| `ebcb4915-cc8b-4d0c-b824-66150c8c4129` | Implement the following plan:  # ghostty-win 日本語IME入力修正計画  ## Context ghostty-win... |
| `fe2768a4-9113-4363-954f-fa62f7acc45e` | WTのCPをDLLプロジェクト版に置き換えて内挿してる旧版を除去しろ。チーム... |
| `dd7b2921-18d4-43e9-9b70-d636e46c5344` | - テキスト選択の選択色修正（WTの実装を移植）   - ControlInteractivity.cppのZig... |
| `ec757810-d889-4790-8432-334956944d19` | ghostty WinUI3にテキスト選択コピーを実装しろ。WTのControlInteractivity.cppを参考... |
| `27539c54-c470-44d1-be81-866ab138945e` | bash |


