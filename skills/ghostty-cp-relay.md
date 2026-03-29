---
name: ghostty-cp-relay
description: GhosttyターミナルにCP(Control Plane)越しでClaude Codeを起動し、タスクを送信する手順。bind、PASTE、RAW_INPUT、persistent pipeの使い方。ゴースト、リレー、IPC、パイプ、CP、bind、エージェント連携と言われた時に使用。
---

# Ghost Ensemble Relay — Ghostty CP越しエージェント操作

## 概要

Ghosttyターミナルに Named Pipe (Control Plane) 経由で接続し、Claude Codeを起動してタスクを自動実行する。

## 前提

- Ghostty WinUI3ビルド: `~/ghostty-win/zig-out-winui3/bin/ghostty.exe`
- agent-deck: `~/agent-deck/agent-deck.exe`（bindコマンド対応）
- zig-control-plane: persistent pipe、PASTE、STATE mode/content_hash対応

## 手順

### 1. Ghostty起動

```bash
cd ~/ghostty-win && start "" "zig-out-winui3/bin/ghostty.exe" &
sleep 5
PID=$(powershell.exe -NoProfile -Command "(Get-Process -Name ghostty).Id" | tr -d '\r')
PIPE="ghostty-winui3-ghostty-${PID}-${PID}"
```

### 2. agent-deck bind（オプション — ステータス管理が要る場合）

```bash
cd ~/agent-deck
./agent-deck.exe bind --pid $PID -t my-session --path ~/ghostty-win
```

### 3. Claude Code起動

RAW_INPUTでコマンド+CRを一発送信:

```bash
B64=$(printf 'claude --dangerously-skip-permissions\r' | base64 -w0)
powershell.exe -NoProfile -Command "
  \$p = New-Object System.IO.Pipes.NamedPipeClientStream('.', '${PIPE}', [System.IO.Pipes.PipeDirection]::InOut)
  \$p.Connect(3000); \$w = New-Object System.IO.StreamWriter(\$p); \$w.AutoFlush = \$true
  \$w.WriteLine('RAW_INPUT|agent|${B64}'); \$r = New-Object System.IO.StreamReader(\$p); Write-Output \$r.ReadLine(); \$p.Close()
"
```

### 4. 信頼確認プロンプトを承認

```bash
B64=$(printf '\r' | base64 -w0)
# 同じRAW_INPUTパターンでEnter送信
```

### 5. プロンプト待ち → タスク送信

```bash
sleep 15  # Claude Code起動待ち
# 画面確認
powershell.exe -NoProfile -Command "
  ... TAIL|10 ...
"
# bypass permissions on が見えたらタスク送信
B64=$(printf 'タスク内容\r' | base64 -w0)
# RAW_INPUTで送信（テキスト+\rを一発）
```

## プロトコル早見表

| コマンド | 用途 | 応答 |
|---------|------|------|
| `PING` | 疎通確認 | `PONG\|session\|pid\|hwnd` |
| `STATE` | 状態取得（mode, content_hash含む） | `STATE\|...\|mode=cooked\|content_hash=XXXXXXXX` |
| `TAIL\|N` | 画面末尾N行取得 | ヘッダー行 + N行のテキスト |
| `RAW_INPUT\|from\|base64` | PTYに直接書き込み（TUI対応） | `QUEUED\|session\|RAW_INPUT` |
| `INPUT\|from\|base64` | テキスト入力（シェル向け） | `QUEUED\|session\|INPUT` |
| `PASTE\|from\|base64` | bracketed paste（テキスト挿入のみ、submitなし） | `QUEUED\|session\|PASTE` |
| `PERSIST` | 接続を使い回すモードに切替 | `OK\|PERSIST` |
| `LIST_TABS` | タブ一覧 | `LIST_TABS\|count\|active` + TAB行 |

## 重要な注意

- **TUIアプリ（Claude Code）にはRAW_INPUT**を使え。INPUTはシェルプロンプト向け
- **テキスト+\rを一発で送る**。分けるとsubmitされない
- **base64は`-w0`（改行なし）**で。改行入るとPARSE_ERROR
- **日本語はbase64が長くなる**。長すぎるとPARSE_ERROR。英語推奨
- **PASTEはテキスト挿入のみ**。submitは別途RAW_INPUT `\r`が必要
- **persistent pipeは10.7倍速い**。頻繁にアクセスするならPERSISTハンドシェイクを使え
- **デバッグビルドのGhosttyでClaude Codeを動かすとフリーズする**。ReleaseFastを使え
- ビルド: `cd ~/ghostty-win && ./build-winui3.sh --release`

## セッションファイル

```
%LOCALAPPDATA%\ghostty\control-plane\winui3\sessions\ghostty-{PID}-{PID}.session
```

中身: `session_name`, `pid`, `hwnd`, `pipe_path`

## 自己診断

```bash
powershell.exe -ExecutionPolicy Bypass -File ~/ghostty-win/tests/self_diagnosis/diagnose.ps1 -Attach -SkipEndurance
```

## ストレステスト

```bash
powershell.exe -ExecutionPolicy Bypass -File ~/agent-deck/tests/cp_stress_test.ps1
```

## ghost_demoリモート起動

```bash
B64=$(echo -n 'C:\Users\yuuji\ghostty-win\tools\ghost-demo\ghost_demo.exe' | base64 -w0)
B64_CR=$(printf '%s\r' "$(echo -n 'C:\Users\yuuji\ghostty-win\tools\ghost-demo\ghost_demo.exe')" | base64 -w0)
# RAW_INPUTで送信
```
