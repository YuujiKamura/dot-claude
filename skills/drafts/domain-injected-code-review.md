---
name: domain-injected-code-review
description: "all. (Domain-Specific Context Injection for AI Review) Use when user mentions: ."
categories: [Audit, CLI, COM, Coverage, D3D11, Geometry, Ghostty, Graphics, IME, IPC, Regression, TSF, Testing, WASM, Win32, WinRT, WinUI3, XAML, Zig, agent-deck, android, automation, claude-skill, code-review, config, control plane, control-plane, echo, editor, ghostty, ime, java, llm, multi-agent, orchestration, prompt, pty, python, renderer, rust, scheduling, script, session-recovery, spreadsheet, terminal, test, tool, verification]
sources: [daily-2026-03-27-1100, daily-2026-03-27-0900, 3f5e4571-0398-4d3b-b5c8-9ad0cc0e8cb8, 578af3df-d409-4b2f-8208-878c27d95b6f, a655d338-09e0-46c3-aed8-c30232097f7e, 7fc0fc63-96f8-4d82-9428-8943d33d5a5d, 53fd044a-849d-4195-a37a-186dd4265e6d, daily-2026-03-27-0600, 19e69065-b6fb-45c0-8911-90ed8a69e2ba, e222e0fb-5660-41df-91fc-a9cedb6d2229, 5f463781-3e73-47a4-9052-7a8a5a2ef51d, daily-2026-03-27-1000, daily-2026-03-27-0700, 5c5b16e9-80a8-49cc-9303-c59ffa7f475d, 1eca3cfd-a37a-4e0c-9a7c-d956a793fe38, 8fbe672f-98d0-44ee-bb17-f15b9881dc41, 6f4bd58d-8666-4e70-b1ba-fdae469948cb, 754a5ce9-5c21-4592-81e5-772f4368c79a]
---

# all

Patterns: 1

## 1. Domain-Specific Context Injection for AI Review

Using environment variables to inject repository-specific constraints (e.g., zig-com.md) into automated code review prompts.

### Events

1. Implemented `REVIEW_EXTRA_CONTEXT` environment variable in `src/bin/review.rs` to allow the orchestrator to pass domain-specific known issues to the AI reviewer.
2. [INTERVENTION] User: 'The orchestrator passes domain-specific known issues (like zig-com.md) via this variable to inject them into the AI reviewer's prompt.' → AI initially failed to grasp the architectural purpose.
3. Frontmatter of `gstack/review/SKILL.md` was manually restricted to the gstack repository to prevent trigger overlap with the new `unified-review` orchestrator.

### Examples

```rust
// Example of variable used in src/bin/review.rs
let extra_context = std::env::var("REVIEW_EXTRA_CONTEXT").unwrap_or_default();
```


## Source

| Conversation | Excerpt |
|---|---|
| `7fc0fc63-96f8-4d82-9428-8943d33d5a5d` | > https://docs.google.com/spreadsheets/d/1cJ4KDegD2S4l_xma_A7Mwz2-D-aAdOQwcMs9fwPc5Oo/edit?gid=2134... |
| `3f5e4571-0398-4d3b-b5c8-9ad0cc0e8cb8` | レビュー系ツール統合の設計と実装を行え。  ## 背景 現在4つのレビュー系... |
| `5f463781-3e73-47a4-9052-7a8a5a2ef51d` | レビュー系ツール統合の設計と実装を行え。  ## 背景 現在4つのレビュー系... |
| `a655d338-09e0-46c3-aed8-c30232097f7e` | スキルマイナーで昨日の要約してみ |
| `19e69065-b6fb-45c0-8911-90ed8a69e2ba` | ai-code-reviewクレート(~/ai-code-review)のsrc/bin/review.rsにREVIEW_EXTRA_CONTEXT環境変数... |
| `578af3df-d409-4b2f-8208-878c27d95b6f` | unified-reviewスキルの残課題を片付けろ。  1. ai-code-reviewクレート(~/ai-code-revie... |
| `1eca3cfd-a37a-4e0c-9a7c-d956a793fe38` | H:\\QuickProject工事\市道南千反畑第1号線舗装補修工事\PHOTO\PIC今日写真南千反... |
| `5c5b16e9-80a8-49cc-9303-c59ffa7f475d` | echo hello from ghostty |
| `e222e0fb-5660-41df-91fc-a9cedb6d2229` | ウィンドウを非アクティブにすると先頭文字が表示されるんだがなんだこ... |
| `6f4bd58d-8666-4e70-b1ba-fdae469948cb` | GTCPもWTCPもghostty CPに繋がるがPARSE_ERROR。CP DLLが壊れてる。ゴーストティ上... |
| `8fbe672f-98d0-44ee-bb17-f15b9881dc41` | eraseLine修正のテスト。何か適当に入力してEnterした後、上矢印で履歴を呼... |
| `754a5ce9-5c21-4592-81e5-772f4368c79a` | ghostty-winのテキスト選択が動かない問題を修正しろ。チャット履歴を遡っ... |
| `53fd044a-849d-4195-a37a-186dd4265e6d` | echo hello world |
| `daily-2026-03-27-0900` | 09:00 — ghostty-win 先頭文字欠け再発 + テスト体制整備 (19 sessions)  - Issue #133: ... |
| `daily-2026-03-27-1000` | 10:00 — 全リポテスト監査・ギャップ埋め (35 sessions — メイン監督セッショ... |
| `daily-2026-03-27-1100` | 11:00 — road-drawing Phase完了・triangle-coreテスト充実 (20 sessions)  - road-drawing: Pha... |
| `daily-2026-03-27-0600` | 06:00 — agent-deck SendRaw/CP統合 (10 sessions)  - Issue #17 SendRaw: `session send` 1コマン... |
| `daily-2026-03-27-0700` | 07:00 — セッション復元・エディタ調査 (13 sessions)  - ターミナル誤終了から... |

## Citations

- `conv0004`: The user had to explicitly explain the pipeline: the orchestrator passes domain-specific known issues (like zig-com.md) via this variable to inject them into the AI reviewer's prompt.


