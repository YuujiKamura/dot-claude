# ai-code-review

AIによる自動コードレビュークレート

## 場所

`~/ai-code-review/`

## 概要

ファイル監視とAI分析を組み合わせた自動コードレビューライブラリ。

## 依存関係

- `folder-watcher` (`../folder-watcher`) - ファイル監視
- `cli-ai-analyzer` (`../cli-ai-analyzer`) - AI呼び出し

## 主要API

```rust
use ai_code_review::{CodeReviewer, Backend, PromptType};

// 監視モード
let mut reviewer = CodeReviewer::new(Path::new("./src"))?
    .with_backend(Backend::Gemini)      // or Backend::Claude
    .with_extensions(&["rs", "ts", "py"])
    .with_prompt_type(PromptType::Default)  // Default, Quick, Security, Architecture
    .with_debounce(500)                 // ミリ秒
    .with_log_file(Path::new(".code-reviews.log"))
    .on_review(|result| {
        println!("{}: {}", result.name, result.review);
    });

reviewer.start()?;
// ...
reviewer.stop()?;

// 単発レビュー
let result = reviewer.review_file(Path::new("src/main.rs"))?;
```

## プロンプトタイプ

| タイプ | 用途 |
|--------|------|
| `Default` | 総合（設計、品質、バグ） |
| `Quick` | 重大な問題のみ（高速） |
| `Security` | セキュリティ観点 |
| `Architecture` | 設計・アーキテクチャ観点 |

## ReviewResult

```rust
struct ReviewResult {
    path: PathBuf,
    name: String,
    review: String,
    timestamp: String,
    has_issues: bool,
    severity: ReviewSeverity,  // Ok, Info, Warning, Error
}
```

## 使用例

```bash
# Cargo.tomlに追加
[dependencies]
ai-code-review = { path = "../ai-code-review" }
```

## GitHub

https://github.com/YuujiKamura/ai-code-review
