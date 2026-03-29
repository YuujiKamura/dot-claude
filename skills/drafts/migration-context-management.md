---
name: migration-context-management
description: "CLI & Tooling. (Preventing 'Zombie' Edits During Large Migrations) Use when user mentions: CLI, script, automation, tool, plugin, extension, config."
categories: [DLL, IME, WinUI3, Windows, Windows Terminal, XAML, Zig, agent-config, automation, bugfix, build-config, cli, code-review, debugging, exploration, feature-implementation, generic, ghostty, git, ime, instructions, investigation, issue, issue-investigation, performance, refactoring, repository-management, rust, shell-selection, skills, terminal, test, tool, tsf, ui, ui-migration, windows, windows-terminal, winui3, zig]
sources: [873a2658-b340-47cd-afaa-15616524bde9, session-2026-03-19T08-53-6733c910, 22645b87-277a-4561-94a4-886877d8efd2, 68f8b109-c790-43b0-87ce-3d93e2f226c2, 86e33ced-f323-41de-865a-1ed088fcba99, aa0da96a-11bd-4fc6-bf03-89ceb07a43b8, session-2026-03-19T06-50-b4190e5b, 019d05fe-b220-7200-8c13-6d7e6dc8b609, 4c49d7aa-3fa8-47ec-a183-c199c3abf4a3, session-2026-03-18T23-58-30cb74bb, ebcb4915-cc8b-4d0c-b824-66150c8c4129, cad6d765-4fed-4272-9510-e5171d80fc23, 9e4e06b1-f482-4067-8633-fa88de993d6b, session-2026-03-19T00-55-e48fc28c, 27539c54-c470-44d1-be81-866ab138945e, dd7b2921-18d4-43e9-9b70-d636e46c5344, fe2768a4-9113-4363-954f-fa62f7acc45e, session-2026-03-19T06-22-708ec066, 019d04db-d5f2-7d41-b6e8-997f746b390c, a4c0b267-f8cb-47a8-80b5-8a6cbb69c62e, 3f292985-6699-44e2-b6b4-15b7cdb71bd8, c24ccbea-d293-4037-8ac4-c0e6622163b3, session-2026-03-19T00-21-c0e56b9f, ec757810-d889-4790-8432-334956944d19, 08c0e683-317c-4a50-a212-aa682c82557f, 952919a2-b68b-4083-9b15-60a6cb0e3a57]
---

# CLI & Tooling

Patterns: 1

## 1. Preventing 'Zombie' Edits During Large Migrations

Long-running migrations (like WinUI3 Islands) create duplicate or 'zombie' folder structures that frequently confuse AI agents into modifying deprecated code.

### Steps

1. AI agents often mistake legacy folders (e.g., 'winui3/') for active targets if the new version is in a similarly named folder (e.g., 'winui3_islands/').
2. Explicit user-correction is required to 'freeze' the old code path; the refactor is not complete until the agent successfully converts hardcoded types into generic functions (comptime App: type).
3. Replacing custom logging (fileLog) with standard library logging (std.log) across the entire project is a critical final step to remove dependency on deprecated utility functions.

### Examples

```zig
// Transitioning to generic surface
pub fn Surface(comptime App: type) type {
 return struct {
 const Self = @this();
 // ...
 };
}
```


## Source

| Conversation | Excerpt |
|---|---|
| `aa0da96a-11bd-4fc6-bf03-89ceb07a43b8` | ghostty issue 112を閉じてもいいか実装を精査 |
| `a4c0b267-f8cb-47a8-80b5-8a6cbb69c62e` | チャット履歴辿って118の続きをやれ |
| `68f8b109-c790-43b0-87ce-3d93e2f226c2` | ghostty issue 113を閉じてもいいか実装を精査 |
| `cad6d765-4fed-4272-9510-e5171d80fc23` | ゴーストティのアイランド版以前の旧実装が残存してるのを取り除いてい... |
| `3f292985-6699-44e2-b6b4-15b7cdb71bd8` | Implement run subcommand for agent-ctl. Usage: agent-ctl run <session> --agent claude <task>. It sho... |
| `22645b87-277a-4561-94a4-886877d8efd2` | Issue #116: Replace PostMessageW wakeup with DispatcherQueue.TryEnqueue for background window perfor... |
| `86e33ced-f323-41de-865a-1ed088fcba99` | Issue #113 remaining: (1) Replace isSurfaceAlive with closed bool field in Surface.zig. Add closed:b... |
| `08c0e683-317c-4a50-a212-aa682c82557f` | Issue #112のTSF退行を修正しろ。preedit(変換途中文字列)が画面に出なくなって... |
| `9e4e06b1-f482-4067-8633-fa88de993d6b` | Surface.zigをgeneric function化しろ。is_islands分岐は全削除。手順: (1)外殻をpub fn ... |
| `c24ccbea-d293-4037-8ac4-c0e6622163b3` | Surface.zigをgeneric function形式にリファクタしろ。is_islands分岐は全削除（island... |
| `952919a2-b68b-4083-9b15-60a6cb0e3a57` | Implement the following plan:  # Issue #113 リファクタ段階適用計画  ## Context Issue #113... |
| `4c49d7aa-3fa8-47ec-a183-c199c3abf4a3` | スキルマイナーで日付が変わってからの要約をしろ |
| `session-2026-03-19T00-55-e48fc28c` | In ~/ghostty-win, review the 4 commits that were just pushed for issue #120 (upstream merge blockers... |
| `session-2026-03-19T00-21-c0e56b9f` | In ~/ghostty-win, the debug_harness module (src/apprt/winui3/debug_harness.zig) is a runtime debug c... |
| `session-2026-03-18T23-58-30cb74bb` | cd ~/ghostty-win && fix these 3 upstream merge blockers (refs issue #120). Make each a separate git ... |
| `dd7b2921-18d4-43e9-9b70-d636e46c5344` | - テキスト選択の選択色修正（WTの実装を移植）   - ControlInteractivity.cppのZig... |
| `ec757810-d889-4790-8432-334956944d19` | ghostty WinUI3にテキスト選択コピーを実装しろ。WTのControlInteractivity.cppを参考... |
| `27539c54-c470-44d1-be81-866ab138945e` | bash |
| `fe2768a4-9113-4363-954f-fa62f7acc45e` | WTのCPをDLLプロジェクト版に置き換えて内挿してる旧版を除去しろ。チーム... |
| `session-2026-03-19T06-22-708ec066` | C:\Users\yuuji\ghostty-win のリポジトリで、src/apprt/winui3/App.zig の行数と、最後の... |
| `session-2026-03-19T06-50-b4190e5b` | C:\Users\yuuji\ghostty-win の Issue #122 の調査をしろ。コードは編集するな。調査... |
| `019d04db-d5f2-7d41-b6e8-997f746b390c` | # AGENTS.md instructions for C:\Users\yuuji  <INSTRUCTIONS> ## Skills A skill is a set of local inst... |
| `ebcb4915-cc8b-4d0c-b824-66150c8c4129` | Implement the following plan:  # ghostty-win 日本語IME入力修正計画  ## Context ghostty-win... |
| `873a2658-b340-47cd-afaa-15616524bde9` | 追加イシューで、ゴーストでものカラー化、これはコマンドプロンプトで... |
| `019d05fe-b220-7200-8c13-6d7e6dc8b609` | <environment_context>   <cwd>C:\Users\yuuji</cwd>   <shell>powershell</shell>   <current_date>2026-0... |
| `session-2026-03-19T08-53-6733c910` | ghostty-winで日本語入力（IME）ができない問題を調査しろ。[13;5u[13;5u調査対... |


