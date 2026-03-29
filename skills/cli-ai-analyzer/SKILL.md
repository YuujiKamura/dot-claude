---
description: "複数AI CLIの統一インターフェース。(1) Gemini/Claude/Ollamaを同じAPIで呼び出し、(2) バックエンド切り替えでAI変更が容易。cli-ai-analyzer、AI解析、Claude CLI、Gemini CLI、Ollama、バックエンド切り替えと言われた時に使用。"
---

# cli-ai-analyzer

## 概要

複数のAI CLIツール（Gemini, Claude, Ollama）を統一インターフェースで呼び出すRustライブラリ。プロジェクトごとにAIバックエンドを変えても呼び出しコードを変更する必要がない。

- **リポジトリ**: `C:/Users/yuuji/cli-ai-analyzer`
- **GitHub**: https://github.com/YuujiKamura/cli-ai-analyzer

## 対応バックエンド

| バックエンド | CLI ツール | ステータス |
|-------------|-----------|-----------|
| **Gemini** | [Gemini CLI](https://github.com/google/gemini-cli) | 対応済み |
| **Claude** | [Claude Code](https://github.com/anthropics/claude-code) | 計画中 |
| **Ollama** | [Ollama](https://ollama.ai/) | 計画中 |

## API

### 主要関数

| 関数 | 説明 |
|------|------|
| `analyze(prompt, files, options)` | ファイル付きで解析を実行 |
| `prompt(prompt, options)` | テキストのみで解析を実行 |
| `analyze_in_dir(dir, prompt, files, options)` | 指定ディレクトリで解析（上級者向け） |

### Backend enum

```rust
pub enum Backend {
    Gemini,  // 対応済み
    Claude,  // 計画中
    Ollama,  // 計画中
}
```

### AnalyzeOptions

| フィールド | 型 | デフォルト | 説明 |
|-----------|------|---------|------|
| `model` | String | `gemini-2.5-flash` | 使用するモデル |
| `output_format` | OutputFormat | Text | 出力形式（Text/Json） |
| `gemini_path` | Option<String> | None | カスタムCLIパス |

## 使用例

### 基本的な解析

```rust
use cli_ai_analyzer::{analyze, AnalyzeOptions};
use std::path::PathBuf;

let result = analyze(
    "この書類の内容を説明してください",
    &[PathBuf::from("document.pdf")],
    AnalyzeOptions::default(), // デフォルトは Gemini
)?;
println!("{}", result);
```

### Backend切り替え（将来対応）

```rust
use cli_ai_analyzer::{analyze, AnalyzeOptions, Backend};

// Gemini を使用（現在のデフォルト）
let result = analyze("...", &files, AnalyzeOptions::default())?;

// 将来的には Backend を切り替え可能に
// let options = AnalyzeOptions::default()
//     .with_backend(Backend::Claude)
//     .with_model("claude-3-opus");
```

### Builderパターン

```rust
use cli_ai_analyzer::AnalysisBuilder;

let result = AnalysisBuilder::new("これらの書類を比較してください")
    .file("doc1.pdf")
    .file("doc2.pdf")
    .model("gemini-2.5-flash")
    .run()?;
```

### CLI使用

```bash
# ファイル解析
cli-ai-analyzer analyze --prompt "この書類の内容を説明してください" document.pdf

# 複数ファイル
cli-ai-analyzer analyze --prompt "これらの書類を要約してください" doc1.pdf doc2.pdf

# 書類チェック（日本語）
cli-ai-analyzer check document.pdf

# 複数書類の照合
cli-ai-analyzer compare contract.pdf estimate.pdf
```

## 連携プロジェクト

### ShoruiChecker

- **パス**: `C:/Users/yuuji/ShoruiChecker`
- **用途**: PDFファイルの整合性をAIで解析するWindowsデスクトップアプリ
- **統合方法**: `src-tauri/src/gemini_cli.rs` で Gemini CLI を呼び出し

### photo-ai-rust

- **パス**: `C:/Users/yuuji/photo-ai-rust`
- **用途**: 工事写真のAI解析・黒板OCR・写真台帳生成
- **統合方法**: Claude CLI を使用して写真解析

### SekouTaiseiMaker

- **パス**: `C:/Users/yuuji/SekouTaiseiMaker`
- **用途**: 施工体制台帳管理・PDF書類のAIチェック
- **統合方法**: Gemini API（HTTP）で書類チェック

## 前提条件

使用するバックエンドに応じて、対応するCLIツールをインストール・認証:

- **Gemini**: `npm install -g @anthropic-ai/gemini-cli` → `gemini` で認証
- **Claude**: Claude Code をインストール・認証（計画中）
- **Ollama**: `ollama serve` でサーバー起動（計画中）

## 環境変数

- `GEMINI_CMD_PATH` - Gemini CLI実行ファイルのカスタムパス

## 注意事項

- Gemini CLIは `~/` 配下のファイルのみアクセス可能
- PDF/画像OCRには `gemini-2.5-pro` を使用（Flash系は非対応）
- Windows環境では `CREATE_NO_WINDOW` フラグでコンソール非表示
