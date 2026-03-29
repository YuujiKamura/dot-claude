---
name: flutter-build
description: Flutterプロジェクトのビルド・デプロイスキル設計パターン。LLM判断を排除し、シェルスクリプトで手順を固定化する。ビルド、デプロイ、シミュレーター、flutter run、xcrun simctlと言われた時に使用。
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
user-invocable: true
---

# Flutter ビルド・デプロイ スキル設計パターン

出典: https://zenn.dev/dx_pm_product/articles/claude-code-skills-flutter-build

## 問題: LLMにビルド手順を任せると壊れる

Claudeに「ビルドして」と指示すると毎回異なるアプローチを取り、再現性ゼロ:
- ブラウザ向けにビルドされる（ターゲット違い）
- エラーを無視して先へ進む
- 環境変数を勝手に追加
- 同じコマンドでも再実行で失敗

**根本原因**: 複数ステップの作業をプロンプトで指示すると、どこかでLLMの判断ミスが入り込む。

## 解決: スキル + シェルスクリプトで手順固定

### ディレクトリ構成

```
.claude/skills/<スキル名>/
├── SKILL.md          # スキル定義 + 行動ルール
└── scripts/
    └── run-<スキル名>.sh   # 実行スクリプト
```

### SKILL.md テンプレート

```yaml
---
name: <スキル名>
description: <何をするスキルか。Claudeの自動判断用>
allowed-tools: Read, Bash
user-invocable: true
---
```

## 設計原則（4つの判断）

### 1. 全ステップ同期実行（バックグラウンド禁止）

バックグラウンド実行にするとClaudeがエラーを検知できない。
ホットリロードを諦めてでも、同期実行で各ステップの成否を確認する。

### 2. 大きなコマンドを分離する

`flutter run` のような一括コマンドを使わず、各フェーズを独立させる:

```bash
# ビルド（同期、成否を確認）
flutter build ios --simulator --dart-define=USE_MOCK_DATA=true

# インストール（simctlで直接操作）
xcrun simctl install <UUID> <.appパス>

# 起動（simctlで直接操作）
xcrun simctl launch <UUID> <bundle-id>
```

一括実行では失敗箇所が特定できない。各ステップを独立させることで、どこで失敗したかが明確になる。

### 3. 不要なステップを削除する

例: 「Flutterデバイス認識確認」ステップは、ワイヤレス検索の遅延でgrepが失敗する。
後続の `flutter build` や `xcrun simctl` はこのステップに依存していないなら、削除する。

**依存関係を整理し、実際に必要なステップだけ残す。**

### 4. SKILL.mdに行動ルールを明記する

Claudeの「勝手な判断」を封じる:

```markdown
## エラー時の行動ルール
- スクリプトがエラー終了したら出力をそのまま報告せよ
- 自動修正は行うな
- ビルド成功を自分で判断するな
```

## スクリプト実装パターン（7ステップ）

```bash
#!/bin/bash
set -euo pipefail  # どのステップで失敗しても即座に終了

# 1. 既存プロセス停止（残存flutter runを検知・停止）
# 2. Simulator.app起動確認（未起動なら起動）
# 3. デバイスのboot確認（未bootならboot）
# 4. flutter pub get（依存関係解決）
# 5. flutter build ios --simulator（同期ビルド）
# 6. xcrun simctl install（インストール）
# 7. xcrun simctl launch（起動）
```

**重要**: 毎回状態チェックするため、シミュレーター状態に関わらず正しく動作する（冪等性）。

## Skills化の判断基準

### 向いている作業
- 手順が固定的でLLMの判断が不要（ビルド、デプロイ、環境構築）
- 複数ステップで各ステップの成否確認が必要
- 繰り返し実行する定型作業

### 向いていない作業
- コードレビュー、リファクタリング（LLMの判断力が必要）
- 状況に応じて手順が変わる作業

### 原則
**「AIに任せる部分と固定化する部分を分ける」** がClaude Code安定運用のコツ。

## Windows環境への適用メモ

iOS simctlはmacOS固有だが、パターン自体は汎用:
- Android: `flutter build apk` → `adb install` → `adb shell am start`
- Web: `flutter build web` → `npx serve build/web`
- Windows: `flutter build windows` → `start build\windows\x64\runner\Release\app.exe`

同じ「分離 + 同期 + set -euo pipefail」の原則を適用する。
