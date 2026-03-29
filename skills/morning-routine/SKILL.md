---
name: morning-routine
description: 朝ルーティン。(1) skill-minerで昨日の全キャリア作業要約、(2) Claude/Gemini/Codex残量確認、(3) 残量に応じたタスク配分計画。セッション開始、朝、おはよう、振り返り、残量、今日の計画、daily、morning、routineと言われた時に使用。
---

# 朝ルーティン: 振り返り → 残量確認 → 今日の計画

セッション開始時に実行する日次ワークフロー。

## Step 1: 昨日の振り返り

skill-miner の `today` コマンドで昨日の全キャリア作業要約を取得:

```bash
cargo run --manifest-path C:/Users/yuuji/skill-miner/Cargo.toml -- today --date $(date -d yesterday +%Y-%m-%d) --format summary --by-carrier
```

出力から以下を抽出して報告:
- **主な成果**: 完了した作業（コミット、Issue クローズ等）
- **未完了/ブロック中**: 途中で止まったもの、理由
- **各キャリア稼働割合**: Claude / Codex / Gemini のセッション数比

## Step 2: AI利用残量の確認（WT Control Plane経由）

**なぜ外部観測が必要か**: 各AIエージェント（Claude/Gemini/Codex）は自分自身の残りトークン・利用枠を内部から把握できない。だから WT Control Plane で別ターミナルにエージェントを起動し、利用量表示コマンドを打たせて、画面出力を読み取る。

### 前提: WT Dev ビルドの起動

Control Plane は WT Dev ビルド（`C:\Users\yuuji\WindowsTerminal`のフォーク）にのみ搭載。Store版WTにはない。

```bash
WINDOWS_TERMINAL_CONTROL_PLANE=1 "/c/Users/yuuji/WindowsTerminal/bin/x64/Debug/WindowsTerminal/WindowsTerminal.exe" &
sleep 5
```

WT Dev ビルドが壊れてる場合の復旧手順は `wt-control-plane` スキルを参照。

### 手順: Control Plane で残量を読む

**重要: bash からの改行送信にハマりどころがある。**
- `INPUT -Text "codex\r\n"` は動かない（MSYS が `\r\n` をパス変換する）
- PowerShell 内で `[char]13 + [char]10` を組み立てて渡す
- `-Command` 引数内のパスは MSYS に変換される → `MSYS_NO_PATHCONV=1` か `cygpath -w` が必要
- WT Dev のデフォルトシェルが PowerShell の場合、`codex` が PowerShell モジュールとして解釈される → **先に `bash` を起動してからエージェントを起動する**

```bash
SCRIPT="$HOME/.claude/skills/wt-control-plane/scripts/wt-control.ps1"
WINPATH=$(cygpath -w "$SCRIPT")

# 接続確認
pwsh.exe -NoLogo -NoProfile -File "$SCRIPT" -Command DISCOVER
pwsh.exe -NoLogo -NoProfile -File "$SCRIPT" -Command PING

# --- まず bash を起動（PowerShellだとcodex/geminiがモジュール扱いされる）---
MSYS_NO_PATHCONV=1 pwsh.exe -NoLogo -NoProfile -Command "
\$text = 'bash' + [char]13 + [char]10
& '$WINPATH' -Command INPUT -Text \$text
"
sleep 3

# --- Codex の残量 ---
MSYS_NO_PATHCONV=1 pwsh.exe -NoLogo -NoProfile -Command "
\$text = 'codex' + [char]13 + [char]10
& '$WINPATH' -Command INPUT -Text \$text
"
sleep 8
# 起動メッセージに「less than X% of your weekly limit left」が出る → これが残量
# /status を打つ場合:
MSYS_NO_PATHCONV=1 pwsh.exe -NoLogo -NoProfile -Command "
\$text = '/status' + [char]13 + [char]10
& '$WINPATH' -Command INPUT -Text \$text
"
sleep 3
pwsh.exe -NoLogo -NoProfile -File "$SCRIPT" -Command TAIL -Lines 30
# 終了
MSYS_NO_PATHCONV=1 pwsh.exe -NoLogo -NoProfile -Command "
\$text = '/exit' + [char]13 + [char]10
& '$WINPATH' -Command INPUT -Text \$text
"

# --- Claude の残量 ---
MSYS_NO_PATHCONV=1 pwsh.exe -NoLogo -NoProfile -Command "
\$text = 'claude' + [char]13 + [char]10
& '$WINPATH' -Command INPUT -Text \$text
"
sleep 5
MSYS_NO_PATHCONV=1 pwsh.exe -NoLogo -NoProfile -Command "
\$text = '/usage' + [char]13 + [char]10
& '$WINPATH' -Command INPUT -Text \$text
"
sleep 3
pwsh.exe -NoLogo -NoProfile -File "$SCRIPT" -Command TAIL -Lines 20
# Ctrl+C x2 で終了
MSYS_NO_PATHCONV=1 pwsh.exe -NoLogo -NoProfile -Command "
& '$WINPATH' -Command INPUT -Text ([char]3 + [char]3)
"

# --- Gemini の残量 ---
MSYS_NO_PATHCONV=1 pwsh.exe -NoLogo -NoProfile -Command "
\$text = 'gemini' + [char]13 + [char]10
& '$WINPATH' -Command INPUT -Text \$text
"
sleep 5
MSYS_NO_PATHCONV=1 pwsh.exe -NoLogo -NoProfile -Command "
\$text = '/stats session' + [char]13 + [char]10
& '$WINPATH' -Command INPUT -Text \$text
"
sleep 3
pwsh.exe -NoLogo -NoProfile -File "$SCRIPT" -Command TAIL -Lines 20
# Ctrl+C で終了
MSYS_NO_PATHCONV=1 pwsh.exe -NoLogo -NoProfile -Command "
& '$WINPATH' -Command INPUT -Text ([char]3)
"
```

### 読み取り値の解釈

| キャリア | 何を見るか | 読み方 |
|---|---|---|
| Codex | 起動時メッセージ | 「less than **X%** of your weekly limit left」→ 残り X% 未満 |
| Codex | `/status` | TUI更新で見えにくい場合あり。起動時メッセージの方が確実 |
| Claude | `/usage` | 「**XX%** used」→ 残り = 100 - XX% |
| Gemini | `/stats session` | 「**XX%**」→ 残り = XX%（直読み） |

### 判定基準

- **潤沢** (>70%): 設計・デバッグ含め自由に使用
- **注意** (40-70%): 大タスクはGemini/Codexに外注
- **逼迫** (15-40%): 判断のみClaude、実装は全外注
- **枯渇** (<15%): 使用停止、他キャリアのみ

### フォールバック

WT Dev ビルドが起動できない場合:
- Claude: `node ~/bin/claude-usage.mjs --json` を試す（OAuth API、401なら不可）
- Codex/Gemini: 「WT Dev を起動してから再試行するか、手動で確認してください」と報告

## Step 3: 今日のタスク確認と配分

### タスク収集
1. 主要リポジトリの未解決Issue:
   ```bash
   gh issue list --repo YuujiKamura/skill-miner --limit 5
   gh issue list --repo YuujiKamura/ghostty --limit 5
   ```
2. MEMORY.md のアクティブプロジェクト状況
3. PLAN.md があるプロジェクト（ghostty-win等）の次ステップ

### 配分ルール
残量に応じて各タスクに担当キャリアを割り当てる:

| タスク種別 | Claude潤沢時 | Claude逼迫時 |
|---|---|---|
| 設計・アーキテクチャ | Claude | Claude（短時間） |
| バグ調査・デバッグ | Claude | Claude（調査のみ→実装外注） |
| 機械的リファクタリング | Gemini/Codex | Gemini/Codex |
| テスト追加 | Codex | Codex |
| ドキュメント・Issue整理 | Gemini | Gemini |

### 出力フォーマット

```markdown
## 昨日の成果
- [成果1]
- [成果2]

## 利用残量
| キャリア | 残量 | リセット | 判定 |
|---|---|---|---|
| Claude | XX% | HH:MM | 潤沢/注意/逼迫/枯渇 |
| Codex | XX% | - | 同上 |
| Gemini | XX% | - | 同上 |

## 今日の計画
| 優先度 | タスク | 担当 | 理由 |
|---|---|---|---|
| P0 | ... | Claude | 設計判断が必要 |
| P1 | ... | Codex | 機械的なリファクタ |
| P2 | ... | Gemini | ドキュメント整理 |
```

## 連携スキル
- `usage-aware-delegation`: 作業中の残量監視と外注判断
- `codex-delegation`: Codex MCP経由の委譲パターン
- `wt-control-plane`: 別ターミナルでのエージェント操作
- `plan-then-parallel`: 計画→Issue→並列実行

## 既知の問題・注意事項
- WT Dev ビルドは Store版WTと同時起動可能だが、MSIX配置は競合する → exe直接起動を使う
- `OpenConsole.slnx` は VS 2022 17.10+ でないと開けない
- Codex の `/status` 出力はTUI再描画で上書きされやすい。起動時の「less than X%」メッセージの方が確実
- Control Plane のソースは `C:\Users\yuuji\WindowsTerminal\src\cascadia\TerminalApp\ControlPlane.cpp`
- git remote: `fork` → `YuujiKamura/windows-terminal-agent-relay`, branch: `control-plane-integration`
