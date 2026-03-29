---
description: "工事写真帳メーカープロジェクトの開発支援。(1) 写真解析機能の追加・修正、(2) PDF/Excel出力の改善、(3) AI解析パイプラインの調整。工事写真、黒板OCR、Gemini、写真台帳と言われた時に使用。"
---

# GASPhotoAIManager (工事写真帳メーカー)

## 概要

工事写真をAIで自動分類・整理し、写真台帳を生成するツール。Google Gemini 2.5 Flashによる黒板OCR、着手前/完了写真の自動ペアリング、PDF/Excel出力機能を提供。

**デモ**: https://yuujikamura.github.io/GASPhotoAIManager/

## 技術スタック

- **Frontend**: React 19 + TypeScript + Vite + Tailwind CSS
- **AI**: Google Gemini 2.5 Flash (メイン)、Claude Code SDK (ローカル専用)
- **出力**: ExcelJS, pdf-lib, html2pdf
- **ストレージ**: IndexedDB (履歴), LocalStorage (設定)

## ディレクトリ構造

```
C:/Users/yuuji/GASPhotoAIManager/
├── App.tsx                 # メインアプリケーションコンポーネント
├── index.tsx               # エントリーポイント
├── types.ts                # 共通型定義
│
├── cli/                    # CLIツール・サーバー
│   ├── commands/           # analyze, config, server コマンド
│   └── adapters/           # APIキー・画像アダプター
│
├── components/             # Reactコンポーネント
│   ├── PreviewView/        # メインビュー
│   ├── AIFrameworkDashboard/  # AI設定ダッシュボード
│   ├── PhotoAlbumView/     # 写真アルバム表示
│   └── MasterEditorModal/  # マスターデータ編集
│
├── hooks/                  # React Hooks
│   ├── usePhotosState.ts   # 写真状態管理
│   ├── useAnalysisSteps.ts # 解析ステップ管理
│   ├── usePdfHandlers.ts   # PDF操作
│   └── useApiKey.ts        # APIキー管理
│
├── services/               # バックエンドサービス
│   ├── gemini/             # Gemini API関連
│   ├── engram/             # トークン圧縮最適化
│   ├── learningService.ts  # 学習機能
│   └── localApiService.ts  # ローカルAPI接続
│
├── shared/                 # 共有コード
│   ├── core/               # 解析ロジック
│   ├── generators/         # Excel/PDF生成コア
│   └── layout-config/      # レイアウト設定
│
├── utils/                  # ユーティリティ
│   ├── excelGenerator.ts   # Excel出力
│   ├── pdfGenerator.ts     # PDF出力
│   ├── promptLoader.ts     # プロンプト読み込み
│   └── storage/            # IndexedDB操作
│
├── types/                  # TypeScript型定義
│   ├── photo.ts            # 写真関連型
│   └── analysis.ts         # 解析関連型
│
├── prompts/                # AIプロンプトテンプレート
├── tests/                  # Vitestテスト
├── scripts/                # ビルド・解析スクリプト
│
├── photo-ai-rust/          # Rust版実装 (WASM)
└── rust-app/               # Rust実装
```

## 主要コマンド

```bash
# 開発
npm run dev              # 開発サーバー起動
npm run build            # プロダクションビルド
npm run test             # テスト実行
npm run preview          # ビルド結果プレビュー

# CLI
npm run cli              # CLI解析ツール
npm run a                # analyze のショートカット
npm run aw               # analyze:web のショートカット

# サーバー
npm run server           # WebSocketサーバー (port 3001)
npm run build:server     # サーバービルド
npm run build:cli        # CLIビルド

# コード生成
npm run generate:ts      # TypeScriptレイアウト生成
npm run generate:rs      # Rustレイアウト生成
npm run generate:all     # 全て生成
npm run sync:to-rust     # Rustプロジェクトへ同期

# プロンプト
npm run prompt:test      # プロンプトテスト
npm run prompt:eval      # プロンプト評価
```

## 動作モード

| モード | 説明 | AI |
|--------|------|-----|
| Web (GitHub Pages) | https://yuujikamura.github.io/GASPhotoAIManager/ | Gemini API |
| Web (ローカル) | `npm run dev` | Gemini or Claude SDK |
| CLI | `npm run cli` | Gemini or Claude SDK |
| Server | `npm run server` (WebSocket on :3001) | Claude SDK |

## 主要機能

- **黒板OCR**: 工事黒板から工種・種別・細別・測点・備考を抽出
- **景観ペアリング**: 着手前/完了写真の自動マッチング
- **Engramトークン最適化**: 解析結果を圧縮してトークン消費75-80%削減
- **スマートPDF**: セッションデータ埋め込み、後から復元可能
- **Excel出力**: 工事写真台帳形式のExcel生成

## 重要ファイル

| ファイル | 役割 |
|----------|------|
| `App.tsx` | アプリ全体の状態管理とルーティング |
| `hooks/usePhotosState.ts` | 写真データの統合管理 |
| `services/gemini/models.ts` | Gemini API呼び出し |
| `services/engram/` | トークン最適化 |
| `utils/excelGenerator.ts` | Excel出力 |
| `utils/pdfGenerator.ts` | PDF出力 |
| `utils/promptLoader.ts` | プロンプト管理 |
| `prompts/` | AIプロンプトテンプレート |

## ワークフロー

- **PR不要**: mainブランチに直接プッシュ
- **ビルド確認**: `npm run build` 成功を確認してからコミット
- **テスト**: ビルドが通ればOK

## セキュリティ注意

コミット禁止:
- APIキー、認証情報
- 個人情報（氏名、住所、電話番号）
- 工事固有情報（工事名、単価）

## アーキテクチャ

```
写真 → AI解析(Gemini/Claude) → JSON → PDF/Excel
         ↓
    Engram圧縮 → 履歴保存(IndexedDB)
```

**最終成果物**: PDF（印刷提出用）、Excel（編集用）
