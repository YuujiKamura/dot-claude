---
description: "ShoruiCheckerプロジェクトの開発支援。(1) PDF整合性チェック機能の開発・修正、(2) Tauri/Rust バックエンド開発、(3) フロントエンドUI開発。ShoruiChecker、書類チェッカー、PDF解析、整合性チェックと言われた時に使用。"
project: photo-ai
---

# ShoruiChecker (PDF整合性チェッカー)

## 概要

PDFファイルの整合性をAI(Gemini)で解析するWindowsデスクトップアプリケーション。
複数のPDFを比較して矛盾点や不整合を検出する機能を持つ。

主な機能:
- PDFドラッグ&ドロップによる解析
- 個別解析・照合解析（複数PDF比較）
- フォルダ監視（PDF追加時に自動通知）
- コードレビュー機能（Geminiによるバックグラウンドレビュー）
- 解析結果のPDF埋め込み保存
- システムトレイ常駐

## 技術スタック

### フロントエンド
- Vanilla HTML/CSS/JavaScript (フレームワークなし)
- Tauri API (`@tauri-apps/api`)

### バックエンド (Rust)
- Tauri 2.x
- lopdf (PDF操作)
- notify (ファイルシステム監視)
- tokio (非同期処理)
- chrono (日時処理)

### AI連携
- Gemini CLI (gemini-cli) を外部プロセスとして呼び出し
- モデル: gemini-2.5-pro

## ディレクトリ構造

```
~/ShoruiChecker/
├── src/                          # フロントエンド
│   ├── index.html               # メインHTML
│   ├── main.js                  # メインJavaScript
│   ├── styles.css               # スタイルシート
│   ├── assets/                  # 静的アセット
│   └── utils/                   # ユーティリティ関数
│       ├── analysis.js
│       ├── clipboard.js
│       ├── text.js
│       └── ui.js
├── src-tauri/                    # Rustバックエンド
│   ├── Cargo.toml               # Rust依存関係
│   ├── tauri.conf.json          # Tauri設定
│   └── src/
│       ├── main.rs              # エントリポイント (ヘッドレスモード対応)
│       ├── lib.rs               # メインライブラリ・Tauriセットアップ
│       ├── analysis.rs          # PDF解析ロジック
│       ├── code_review.rs       # コードレビュー機能
│       ├── error.rs             # エラー型定義
│       ├── events.rs            # イベント定義
│       ├── gemini.rs            # Gemini認証
│       ├── gemini_cli.rs        # Gemini CLI呼び出し
│       ├── guidelines.rs        # ガイドライン生成
│       ├── history.rs           # 解析履歴管理
│       ├── pdf_embed.rs         # PDF結果埋め込み
│       ├── settings.rs          # 設定管理
│       └── watcher.rs           # フォルダ監視
├── tests/
│   └── frontend/                # フロントエンドテスト (Node.js test)
├── scripts/
│   ├── tdd/                     # TDD支援スクリプト
│   │   ├── guard.js             # テストウォッチャー
│   │   ├── from-issue.js        # Issue駆動開発
│   │   └── from-issue-gh.js     # GitHub Issue連携
│   └── logging/                 # ログ関連スクリプト
├── install-context-menu.ps1     # 右クリックメニュー登録
└── uninstall-context-menu.ps1   # 右クリックメニュー解除
```

## 主要コマンド

### 開発

```bash
# 開発サーバー起動 (Tauri dev mode)
npm run tauri dev

# ビルド
npm run tauri build
```

### テスト

```bash
# 全テスト実行
npm test

# フロントエンドテストのみ
npm run test:frontend

# Rustテストのみ
npm run test:tauri
# または
cd src-tauri && cargo test
```

### TDD支援

```bash
# テストウォッチャー
npm run tdd:guard

# Issue駆動開発
npm run tdd:issue
npm run tdd:issue:gh
```

### ヘッドレスモード

```bash
# GUIなしでPDF解析
shoruichecker --headless <file.pdf>
```

## 重要ファイル

| ファイル | 役割 |
|---------|------|
| `src-tauri/src/lib.rs` | Tauriアプリ初期化、コマンド登録 |
| `src-tauri/src/analysis.rs` | PDF解析のコアロジック |
| `src-tauri/src/gemini_cli.rs` | Gemini CLI呼び出し処理 |
| `src/main.js` | フロントエンドメインロジック |
| `src/index.html` | UI構造定義 |
| `src-tauri/tauri.conf.json` | Tauri設定 |

## Tauriコマンド一覧

```rust
// PDF解析
analyze_pdfs

// フォルダ監視
get_startup_file, get_watch_folder, set_watch_folder, stop_watching

// Gemini認証
open_gemini_auth, check_gemini_auth

// 設定
get_model, set_model

// 履歴
get_all_history

// PDF埋め込み
embed_pdf_result, read_pdf_result

// ガイドライン
generate_guidelines

// コードレビュー
get_code_watch_folder, is_code_review_enabled,
set_code_watch_folder, set_code_review_enabled, stop_code_watching
```

## 開発上の注意

- Gemini CLI (`gemini`) がPATHに必要
- Windows専用 (`CREATE_NO_WINDOW` フラグ使用)
- PDF解析結果はメタデータとしてPDFに埋め込み可能
- フォルダ監視はサブフォルダも含む
