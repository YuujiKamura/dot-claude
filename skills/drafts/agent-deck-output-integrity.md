---
name: agent-deck-output-integrity
description: "all. (Terminal Output Protocol Integrity) Use when user mentions: ."
categories: [AGENTS.md, CHANGELOG, CI/CD, CLI, Codex, DXF, E2E, Flutter, Flutter Web, Git, GitHub Actions, GitHub Pages, Go, IPC, MSYS, Named Pipe, PATH, Rust, TDD, UI, WASM, Windows, YAML, Zig, abstraction, agent-deck, agents, bridge, build, configuration, debugging, deploy, deployment, fix, ghostty, hang, history, instructions, issues, multi-agent, npm, path conversion, planning, policy, prompt detection, protocol, rules, session, skills, state management, summary, test design, test script, tmux, tool discovery, unit test]
sources: [5cfa5177-006a-45bf-9aa5-edd5ed4c5045, 019d31cd-4977-7622-95f1-0d49d2ab928d, 019d31c9-d8e7-78f2-924f-bbfdda20250a, 019d31c4-42e7-77d0-8d45-5645f5d4db6b, 609c58c2-41a5-48be-bcd1-bc0b3ba8f5f0, 957a772b-7a57-4e93-9404-750a7a83cb6c, f2f8b97a-4ccb-4ac3-b059-4d07320b77ab, 019d31e3-7b14-7be2-b397-186723bc81f7, 42ed25b3-322c-415d-b21b-5f935d6fa814, b498183c-1134-4922-bc16-44682e071b6c, 262248ac-cdbf-43f7-a95d-08f4500a75e0, 311940a6-5e4d-4f52-b408-1115b57af910, 994a76ba-0ba1-49d2-bed6-a010d12a9790, 9c60d8ca-3397-4c3b-9195-f5976c3d6c82, e90e48fa-7876-48cc-ba5d-de039d7b2fec, 019d31e9-1c41-7942-b823-299e28da3cfe, 643e9f02-59e8-4b74-8f18-b94122458b0d, 019d330d-20ed-7d40-9172-3917e4cc07bb, 9fee7a94-895c-4fbc-96d5-4441e689350f, 36d68b82-399e-4d03-b932-cfb7a7e8b96c, a1908622-7835-4c49-b57c-5af86d62eeca, 019d31dc-34ca-77e1-a2e0-5180a9639fe5, 91ab98b8-3e5d-4a8c-af34-ba648d3f5d09, 31cce2f9-922a-4582-b84f-f5bc8d7da6b1, 019d31d2-2353-7920-b263-568cabd93c62, c4b6f524-336e-44e3-8f96-35cc9012c90a, 9aa5f514-653b-49f6-b425-9d2f988274cc, 019d333b-de9c-7982-a936-21654fa87c28, 019d31b5-29de-7741-9c33-9ede2eaa900b, 019d32dc-d174-77e0-8f74-8548db56e634, 05e21a92-3925-4032-a107-466dd1ffc323, a8f21999-2d50-4a80-8d2f-dc3576627e80, 019d32fb-f4ca-73d3-bfb5-b4396f5857b8, 22d5a462-2fdc-4e9e-84d9-84d6f501fb6f, 38f00943-cf30-4323-9f93-aefca457dfb9, 019d31d9-850d-7682-b6f1-fdba78da1588, 019d31ca-4e77-78e1-bca3-df133e85f9c6, 019d32df-35a8-76e1-b0cc-256439b7febf, 019d31c3-8d83-7b80-bffc-b2347a29d965, 019d31c6-ecb0-7630-9158-b005383bcdbe, e122629d-2f82-4a39-91d5-fdcf479211fe]
---

# all

Patterns: 1

## 1. Terminal Output Protocol Integrity

Fixing regressions where management protocol metadata replaces terminal content

### Events

1. agent-deck session output was found to return only protocol headers (e.g., TAIL|session|N) instead of the actual shell content.
2. The issue was traced to incorrect stripTailHeader logic that failed to properly parse the raw pipe buffer when protocol variants were mixed.
3. User: 'agent-deck session outputがTAILヘッダーだけ返す問題がまだ残ってる。Issue #21で修正したはずだが、古いバイナリでは再発する。' [INTERVENTION]


## Source

| Conversation | Excerpt |
|---|---|
| `a8f21999-2d50-4a80-8d2f-dc3576627e80` | エージェントデック絡みの状態管理の直しをやらせてたんだけど、なんか... |
| `019d32fb-f4ca-73d3-bfb5-b4396f5857b8` | <environment_context>   <cwd>C:\Users\yuuji</cwd>   <shell>powershell</shell>   <current_date>2026-0... |
| `91ab98b8-3e5d-4a8c-af34-ba648d3f5d09` | agent-deckリポジトリのTAILハング問題を調査しろ。internal/tmux/driver_cp.goのsendRe... |
| `994a76ba-0ba1-49d2-bed6-a010d12a9790` | agent-deck の状態取得仕上げタスク。internal/session と internal/tmux を中心に、状... |
| `36d68b82-399e-4d03-b932-cfb7a7e8b96c` | agent-deck の prompt/readiness 判定を直せ。背景: internal/send/submit_prompt.go には prot... |
| `262248ac-cdbf-43f7-a95d-08f4500a75e0` | CHANGELOG.md の最新エントリ3件を読んで、各バージョン番号とタイトルだけ... |
| `05e21a92-3925-4032-a107-466dd1ffc323` | go test ./internal/session/ -run TestMapRawStatus -v を実行して、全サブテストの結果... |
| `019d330d-20ed-7d40-9172-3917e4cc07bb` | <environment_context>   <cwd>C:\Users\yuuji</cwd>   <shell>powershell</shell>   <current_date>2026-0... |
| `019d333b-de9c-7982-a936-21654fa87c28` | <environment_context>   <cwd>C:\Users\yuuji</cwd>   <shell>powershell</shell>   <current_date>2026-0... |
| `019d32df-35a8-76e1-b0cc-256439b7febf` | <environment_context>   <cwd>C:\Users\yuuji</cwd>   <shell>powershell</shell>   <current_date>2026-0... |
| `f2f8b97a-4ccb-4ac3-b059-4d07320b77ab` | エージェントデック越しに、今2つのエージェントが作業してるので状況を... |
| `019d32dc-d174-77e0-8f74-8548db56e634` | <environment_context>   <cwd>C:\Users\yuuji</cwd>   <shell>powershell</shell>   <current_date>2026-0... |
| `643e9f02-59e8-4b74-8f18-b94122458b0d` | claude --dangerously-skip-permissions |
| `5cfa5177-006a-45bf-9aa5-edd5ed4c5045` | Issue #141デバッグ。SUBSCRIBEは通るがEVENTが来ない。cd ~/ghostty-win。zig-control-pla... |
| `9fee7a94-895c-4fbc-96d5-4441e689350f` | 何か1日分の仕事を履歴から考えてほしいが |
| `a1908622-7835-4c49-b57c-5af86d62eeca` | agent-deck Issue #24: SubmitPrompt汎用層を実装しろ。cd ~/agent-deck。INVESTIGATION.mdとAG... |
| `e90e48fa-7876-48cc-ba5d-de039d7b2fec` | agent-deck Issue #24。cd ~/agent-deck。CpDriver.CreateSessionを直せ。ghostty起動→パイプ... |
| `c4b6f524-336e-44e3-8f96-35cc9012c90a` | agent-deck CpDriver.CreateSessionのテスト役。cd ~/agent-deck。INVESTIGATION.mdを読め。E2E... |
| `b498183c-1134-4922-bc16-44682e071b6c` | agent-deck Issue #24のテスト役。cd ~/agent-deck。INVESTIGATION.mdとAGENTS.mdを読め。Subm... |
| `38f00943-cf30-4323-9f93-aefca457dfb9` | agent-deck Issue #24: CpDriver.CreateSession修正。cd ~/agent-deck。INVESTIGATION.mdを読め。... |
| `22d5a462-2fdc-4e9e-84d9-84d6f501fb6f` | agent-deck CpDriver.CreateSessionのテスト役。cd ~/agent-deck。E2Eテストを書け: (1) agen... |
| `e122629d-2f82-4a39-91d5-fdcf479211fe` | agent-deck Issue #24のテスト役。cd ~/agent-deck。Codex CLIへのプロンプト送信テス... |
| `609c58c2-41a5-48be-bcd1-bc0b3ba8f5f0` | agent-deck Issue #24を直せ。cd ~/agent-deck。CpDriver.CreateSessionの実装(ddf2866)はある... |
| `9aa5f514-653b-49f6-b425-9d2f988274cc` | claude --dangerously-skip-permissions |
| `019d31e9-1c41-7942-b823-299e28da3cfe` | <environment_context>   <cwd>C:\Users\yuuji</cwd>   <shell>powershell</shell>   <current_date>2026-0... |
| `019d31dc-34ca-77e1-a2e0-5180a9639fe5` | <environment_context>   <cwd>C:\Users\yuuji\road-drawing</cwd>   <shell>powershell</shell>   <curren... |
| `42ed25b3-322c-415d-b21b-5f935d6fa814` | road-drawing Issue #10の実装役A。Flutter Web側を担当。35652(プランナー)から計画... |
| `019d31e3-7b14-7be2-b397-186723bc81f7` | # AGENTS.md instructions for C:\Users\yuuji\agent-deck  <INSTRUCTIONS> # Agent-Deck Development Rule... |
| `019d31d9-850d-7682-b6f1-fdba78da1588` | # AGENTS.md instructions for C:\Users\yuuji\agent-deck  <INSTRUCTIONS> # Agent-Deck Development Rule... |
| `019d31d2-2353-7920-b263-568cabd93c62` | <environment_context>   <cwd>C:\Users\yuuji\agent-deck</cwd>   <shell>powershell</shell>   <current_... |
| `019d31cd-4977-7622-95f1-0d49d2ab928d` | <environment_context>   <cwd>C:\Users\yuuji\agent-deck</cwd>   <shell>powershell</shell>   <current_... |
| `019d31ca-4e77-78e1-bca3-df133e85f9c6` | <environment_context>   <cwd>C:\Users\yuuji\agent-deck</cwd>   <shell>powershell</shell>   <current_... |
| `019d31c9-d8e7-78f2-924f-bbfdda20250a` | <environment_context>   <cwd>C:\Users\yuuji\agent-deck</cwd>   <shell>powershell</shell>   <current_... |
| `019d31c6-ecb0-7630-9158-b005383bcdbe` | <environment_context>   <cwd>C:\Users\yuuji\agent-deck</cwd>   <shell>powershell</shell>   <current_... |
| `311940a6-5e4d-4f52-b408-1115b57af910` | 生きてるか？agent-deckのCD ~/agent-deck をして、/usage のMSYSパス変換問題を調べ... |
| `019d31c4-42e7-77d0-8d45-5645f5d4db6b` | <environment_context>   <cwd>C:\Users\yuuji\road-drawing</cwd>   <shell>powershell</shell>   <curren... |
| `019d31c3-8d83-7b80-bffc-b2347a29d965` | <environment_context>   <cwd>C:\Users\yuuji\road-drawing</cwd>   <shell>powershell</shell>   <curren... |
| `019d31b5-29de-7741-9c33-9ede2eaa900b` | <environment_context>   <cwd>C:\Users\yuuji\road-drawing</cwd>   <shell>powershell</shell>   <curren... |
| `31cce2f9-922a-4582-b84f-f5bc8d7da6b1` | road-drawing Issue #10のテスト役。Flutter Web + Rust WASMのテストを書け。(1) Flutter w... |
| `9c60d8ca-3397-4c3b-9195-f5976c3d6c82` | road-drawing Issue #10のテスト役B。WASM bridge専任。通信手段: agent-deck session send <... |
| `957a772b-7a57-4e93-9404-750a7a83cb6c` | road-drawing Issue #10の実装役B。Rust WASM bridge側を担当。35652(プランナー)から計... |

## Citations

- `b498183c`: agent-deck session outputがTAILヘッダーだけ返す問題がまだ残ってる。Issue #21で修正したはずだが、古いバイナリでは再発する。


