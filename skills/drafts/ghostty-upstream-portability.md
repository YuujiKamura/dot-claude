---
name: ghostty-upstream-portability
description: "all. (Ghostty WinUI3 Port Portability and Upstream Blockers) Use when user mentions: ."
categories: [agent-ctl, agents, bash, bug-fix, build, ci, claude, clipboard, dll, ghostty, hacking, ime, installer, llm, manual, markdown, powershell, refactoring, rust, selection, state-management, test, verification, win32, windows-terminal, winui3, zig]
sources: [3e7264ca-8ef5-4b04-9e85-b82c8f015058, ec757810-d889-4790-8432-334956944d19, ebcb4915-cc8b-4d0c-b824-66150c8c4129, 21044f1b-620a-4d82-9fb3-5fe41143594e, dd7b2921-18d4-43e9-9b70-d636e46c5344, fe2768a4-9113-4363-954f-fa62f7acc45e, d658da03-ff03-4991-9a92-52bd28ea5663, 27539c54-c470-44d1-be81-866ab138945e, 61878fba-54b6-4ff8-9acd-d6644fd5fc45, 5466f2b8-2bef-45e5-8f06-029174f01631]
---

# all

Patterns: 1

## 1. Ghostty WinUI3 Port Portability and Upstream Blockers

Identifying and mitigating blockers for merging Windows-specific terminal features into a Zig-based core

### Steps

1. The 'Control Plane' (Rust DLL) was identified as a major blocker due to external toolchain dependencies (cargo) in a Zig-native build system.
2. NuGet package versions (1.4.230822000) and target architectures (win10-x64) were found hardcoded in build.zig.
3. debug_harness.zig was found to have high coupling with App.zig (40+ sites) for runtime debugging flags.
4. OutputDebugStringA was identified as a dead code declaration in os.zig that should be removed.
5. [INTERVENTION] User: 'おかしい。指示と違って、ゴーストティの変更になるのはなんでだ。WindowsTerminalのDev版の話をしてるのに' -> Clarified that 'WT' in the local context referred to the user's specific Windows Terminal dev fork.

### Examples

```
// Hardcoded version blocker found in build.zig
const default_path = std.fs.path.join(..., &.{ ".nuget", "packages", "microsoft.windowsappsdk", "1.4.230822000", ... });
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


