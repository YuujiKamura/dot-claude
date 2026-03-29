---
description: "PDFに解析結果を埋め込むRustライブラリ。(1) AIの解析結果をPDFに埋め込んで一体化、(2) 埋め込み済みなら再解析スキップでコスト削減。pdf-analysis-embed、PDF埋め込み、解析結果埋め込み、再解析不要、PDFメタデータと言われた時に使用。"
project: photo-ai
---

# pdf-analysis-embed

## 概要
PDFに解析結果を埋め込み、後から読み出せるRustライブラリ。解析結果がPDF自体に埋め込まれるため、再解析不要でファイル管理がシンプルになる。

## リポジトリ
- パス: `~/pdf-analysis-embed`

## なぜこれが画期的か

従来、PDFをAIで解析すると:
- 解析結果は別ファイル（JSON、テキスト等）に保存
- PDFと結果がバラバラになる
- 同じPDFを何度も再解析するコストが発生

**pdf-analysis-embed** を使うと:
- **解析結果がPDF自体に埋め込まれる**
- PDFを渡せば結果も一緒についてくる
- 再解析不要（API呼び出しコスト・時間を節約）
- ファイル管理がシンプルに

```
[従来]
document.pdf + analysis_result.json + metadata.txt = 管理が面倒

[pdf-analysis-embed]
document.pdf（解析結果内蔵） = これだけでOK
```

## ユースケース
- **書類チェッカー**: PDF整合性チェック結果を埋め込み、チェック済みPDFとして保存
- **写真台帳AI**: 解析済みの写真台帳PDFを作成、再解析なしで結果参照
- **契約書レビュー**: AIレビュー結果を契約書PDFに埋め込み、担当者間で共有

## 技術スタック
- **言語**: Rust
- **主要依存クレート**:
  - `lopdf`: PDF構造操作
  - `pdf-extract`: テキスト抽出
  - `serde`/`serde_json`: シリアライゼーション
  - `base64`: エンコーディング
  - `chrono`: タイムスタンプ

## 主要API

### AnalysisResult構造体
```rust
use pdf_analysis_embed::AnalysisResult;

let result = AnalysisResult::new("整合性チェック完了: 問題なし")
    .with_analyzer("ShoruiChecker v1.0")
    .with_source("gemini-2.5-pro")
    .with_extra("追加情報: 3件の警告あり")
    .with_timestamp();
```

### embed_result - 解析結果の埋め込み
```rust
use pdf_analysis_embed::embed_result;

embed_result(path, &result)?;
```

### read_result - 解析結果の読み出し
```rust
use pdf_analysis_embed::read_result;

match read_result(path)? {
    Some(result) => {
        println!("既に解析済み: {}", result.content);
        // 再解析をスキップ
    }
    None => {
        println!("未解析: 解析を実行");
        // 解析を実行
    }
}
```

### extract_text - テキスト抽出
```rust
use pdf_analysis_embed::extract_text;

let text = extract_text(path)?;
// このテキストをAIに送って解析
```

### メタデータ操作
```rust
use pdf_analysis_embed::{get_metadata, set_metadata, PdfMetadata};

let metadata = get_metadata(path)?;
println!("Title: {:?}", metadata.title);
```

## 技術的な仕組み
PDFのInfo辞書（メタデータ領域）にBase64エンコードしたJSONを格納。
- PDFビューアでは見えない（通常の閲覧に影響なし）
- 標準的なPDF構造を利用（特殊なフォーマットではない）
- どのPDFリーダーでも開ける互換性を維持

## 依存関係として使用
```toml
[dependencies]
pdf-analysis-embed = { path = "../pdf-analysis-embed" }
```

## 連携スキル
- `shorui-checker`: PDF整合性チェック結果の埋め込みに使用
- `photo-ai-rust`: 写真台帳PDFへの解析結果埋め込みに活用可能
