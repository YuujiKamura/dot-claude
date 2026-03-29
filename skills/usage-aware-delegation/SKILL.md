---
name: usage-aware-delegation
description: Claude Code残量に応じた外注判断。(1) 残量チェックと行動レベル判定、(2) Codex MCP外注、(3) WT Control Plane経由でGemini/Codex/別Claudeに外注、(4) 仕事量と残量のバランスで自動判断。usage、残量、利用料、外注、コスト、節約、Codex委譲、チーム、並列と言われた時に使用。
project: photo-ai
---

# Usage-Aware Delegation（残量ベース外注）

## 原則

Claude Code サブスクリプションの残量を意識し、重い作業は**外部エージェントに外注**してClaude枠を温存する。外注先は2つ:

1. **Codex MCP** — 同一プロセスから直接呼べる。単発タスク向き
2. **WT Control Plane** — 別ターミナルのエージェント（Gemini CLI / Codex / 別Claude）に投げる。並列実行・長時間タスク向き

**仕事量が多いのに残量が少ないとき、自分で突っ走るな。チームを組め。**

## 残量チェックのタイミング

以下のタイミングで `/usage` を内部的に意識する:

1. **セッション開始時** — 現在の残量レベルを把握
2. **大きなタスク着手前** — 10ファイル超の変更、大規模リファクタ等
3. **セッションが30分以上続いたとき** — 消費ペースを確認
4. **compactが発生したとき** — コンテキスト圧迫 = 大量消費の兆候

## 残量レベル別の行動

| レベル | 状態 | 行動 |
|--------|------|------|
| 潤沢 | 制限なし | 通常作業。全てClaude直接 |
| 中程度 | 半分程度消費 | 大量ファイル操作はCodex MCPへ。設計・判断はClaude |
| 逼迫 | 残り少ない | 設計・判断のみClaude。実装はCodex MCP or WT経由エージェントへ |
| 枯渇 | 制限到達直前 | WT Control PlaneでGemini/Codexに全委譲。Claudeは指揮のみ |

### 逼迫〜枯渇時の判断フロー

1. 仕事量を見積もる（ファイル数、変更規模）
2. 残量と照合する
3. **残量 < 仕事量** なら外注先を選ぶ:
   - 単発・定型 → Codex MCP
   - 複数タスク並列 → WT Control Plane で複数タブに投げる
   - 調査・探索 → WT 経由で Gemini CLI に投げる（無料枠が大きい）
4. ユーザーに「どのエージェントに頼むか」を確認（`wt-control-plane` スキル参照）
5. 投げて、TAILで結果を回収して、自分は統合・判断に専念

## Codexへの委譲パターン

### 委譲する（Codex向き）
- 10+ ファイルのリネーム・import書き換え
- ボイラープレート生成（CRUD、テスト雛形）
- 定型的なリファクタリング（変数名統一、パターン適用）
- ドキュメント生成・更新
- 既知パターンのコード生成

### 委譲しない（Claude直接）
- アーキテクチャ設計・判断
- バグの原因分析・デバッグ
- セキュリティレビュー
- ドメイン知識が必要な判断（舗装、施工体制等）
- 3ファイル以下の小規模変更
- ユーザーとの対話・質問回答

## 委譲時のプロンプトテンプレート

```
mcp__codex__codex(
  prompt: "【タスク概要】
対象: {ファイルパスまたはディレクトリ}
やること: {具体的な変更内容}
制約: {コーディング規約・禁止事項}
完了条件: {何をもって完了とするか}",
  approval-policy: "never",
  sandbox: "workspace-write"
)
```

## 全キャリアの残量把握

### Claude (自分)
WT Control Plane 経由で別タブの Claude に `/usage` を送って TAIL で読む（最も確実）:

```bash
SCRIPT=~/.claude/skills/wt-control-plane/scripts/wt-control.ps1
# /usage はMINGWパス展開されるので powershell -Command で直接送る
powershell -Command '
$pipe = New-Object System.IO.Pipes.NamedPipeClientStream(".", "<pipe_name>", [System.IO.Pipes.PipeDirection]::InOut)
$pipe.Connect(5000)
$w = New-Object System.IO.StreamWriter($pipe); $r = New-Object System.IO.StreamReader($pipe)
$b64 = [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes("/usage`r"))
$w.Write("RAW_INPUT|usage|$b64"); $w.Flush()
$pipe.WaitForPipeDrain(); Start-Sleep 3
$pipe.Close()
'
# 3秒後にTAILで読む
pwsh.exe -File $SCRIPT -Command TAIL -Lines 20
```

読むべき値: `Current session: XX% used`, `Current week: XX% used`

### Gemini CLI — `/stats`
- TUI内で `/stats` を送るとトークン使用量が表示される
- **無料枠**: rate limit はあるがトークン課金なし（Google AI Studio 無料 tier）
- rate limit に当たったら待つだけ。重い調査タスクを投げるのに最適（コスト0）

### Codex CLI — `/status`
- TUI内で `/status` を送るとモデル・承認モード・トークン使用量が表示される
- rate limit に近づくと `limit left. Run /status for a breakdown.` と警告が出る
- 上限到達時: `You've hit your usage limit. Visit https://chatgpt.com/codex/settings/usage to purchase more credits`
- full-auto モードで実装タスクに最適

### 全キャリア一覧

| キャリア | 残量確認コマンド | 表記の意味 |
|---------|----------------|-----------|
| Claude | `/usage` | **XX% used** = 使用済み。残りは `100 - XX`% |
| Codex | `/status` | **XX% left** = 残り。そのまま残量 |
| Gemini | `/stats session` | **XX%** = 残り。resets in で回復時刻もわかる |

**表記が逆のキャリアがある。** Claude だけ「使った割合」で、Codex と Gemini は「残りの割合」。必ず「残り」に換算してから順列を組め。

**パーセンテージの裏にある絶対量はプランによって全く違う。** 同じ「残り70%」でも、高額プランの70%と安価プランの70%では振れる仕事量が桁違いに異なる。ユーザーの契約状況を把握せずにパーセンテージだけで判断するな。プランの規模感が分からないときはユーザーに聞け。

**課金形態・得意分野・残量はすべてユーザーの契約と状況次第で変わる。** 決め打ちするな。

3つのエージェントがいれば順列ができる。残量を見て、余裕がある順に仕事を振れ。今この瞬間の残量が全て。前回のセッションの記憶は当てにならない。

**やること**: 各キャリアに残量コマンドを送る → 出力を読む → 余裕がある順に並べる → 重い仕事から順に余裕のあるキャリアに振る。自分（Claude）の残量が一番少ないなら、自分は指揮だけして手は動かさない。

## コスト節約テクニック

1. **Explore agentを先に** — 全文Read前にgrepで絞る
2. **Read のlimit活用** — 巨大ファイルは必要部分だけ
3. **並列Codex** — 独立タスクは複数Codexセッションを同時起動
4. **compact前にsave** — コンテキスト圧縮前に重要情報をメモリへ
