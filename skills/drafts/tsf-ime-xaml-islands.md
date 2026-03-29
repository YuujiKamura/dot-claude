---
name: tsf-ime-xaml-islands
description: "CLI & Tooling. (TSF Focus and Composition Synchronizing in XAML Islands) Use when user mentions: CLI, script, automation, tool, plugin, extension, config."
categories: [Bash, Bug Fix, DLL, FFI, Feature Implementation, Ghostty, IME, Migration, Selection, Terminal, UI, WinUI3, Windows Terminal, Zig]
sources: [fe2768a4-9113-4363-954f-fa62f7acc45e, dd7b2921-18d4-43e9-9b70-d636e46c5344, 27539c54-c470-44d1-be81-866ab138945e, ebcb4915-cc8b-4d0c-b824-66150c8c4129, ec757810-d889-4790-8432-334956944d19]
---

# CLI & Tooling

Patterns: 1

## 1. TSF Focus and Composition Synchronizing in XAML Islands

Fixing Japanese IME failures caused by HWND volatility and event consumption in WinUI3/XAML Island environments.

### Steps

1. TSF associateFocus was initially called only once at startup, but the internal HWND of XAML Islands changed dynamically, causing a mismatch (e.g., 0x66e072a vs 0x39e0cca) that broke IME tracking.
2. Calling associateFocus with the current HWND inside the onXamlGotFocus handler resolved the focus tracking issue and allowed the IME candidate window to appear correctly.
3. The textEditSinkOnEndEdit event was failing to commit text because it was restricted to _compositions == 1; loosening the check to >= 1 enabled proper delivery of multi-step conversions.
4. The IME 'Enter' key for commitment was being marked as .consumed in handleKeyEvent, which prevented TSF from delivering the finalized string to the terminal buffer.
5. A suppression flag was added to onXamlCharacterReceived to prevent duplicate input when both TSF and XAML event paths delivered the same committed character.


## Source

| Conversation | Excerpt |
|---|---|
| `ebcb4915-cc8b-4d0c-b824-66150c8c4129` | Implement the following plan:  # ghostty-win 日本語IME入力修正計画  ## Context ghostty-win... |
| `fe2768a4-9113-4363-954f-fa62f7acc45e` | WTのCPをDLLプロジェクト版に置き換えて内挿してる旧版を除去しろ。チーム... |
| `dd7b2921-18d4-43e9-9b70-d636e46c5344` | - テキスト選択の選択色修正（WTの実装を移植）   - ControlInteractivity.cppのZig... |
| `ec757810-d889-4790-8432-334956944d19` | ghostty WinUI3にテキスト選択コピーを実装しろ。WTのControlInteractivity.cppを参考... |
| `27539c54-c470-44d1-be81-866ab138945e` | bash |


