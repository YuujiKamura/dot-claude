---
name: pdf-verification
description: Codex CLIを使用してPDF出力結果を検証する。使用場面: (1) PDF生成後の確認、(2) レイアウト検証、(3) 写真配置確認、(4) フォント表示確認、(5) 枠線・余白確認。トリガー: "PDF確認", "PDF検証", "出力確認", "レイアウト確認"
---

# PDF検証スキル

Codex CLIを使用してPDF出力結果を自動検証する。

## 実行手順

### 1. テストPDF生成

```bash
cd C:/Users/yuuji/Sanyuu2Kouku/photo-ai-rust

# テストデータ作成
cat > test_verify.json << 'EOF'
[
  {
    "fileName": "test1.jpg",
    "filePath": "<実際の画像パス>",
    "date": "2026-01-18",
    "photoCategory": "施工状況",
    "workType": "舗装工事",
    "variety": "表層工",
    "detail": "テスト写真1",
    "station": "No.10+0.0",
    "remarks": "備考テスト",
    "measurements": "50mm"
  }
]
EOF

# PDF生成
cargo run --release -- export test_verify.json -f pdf -o test_verify.pdf -t "検証テスト"
```

### 2. Codexで検証

```bash
codex exec --full-auto --sandbox read-only --cd C:/Users/yuuji/Sanyuu2Kouku/photo-ai-rust "生成されたPDFファイル test_verify.pdf を読み取り、以下を確認してレポートしてください:
1. ページサイズ（A4かどうか）
2. 写真が枠内に収まっているか
3. 日本語テキストが正しく表示されているか
4. フォント（明朝体かどうか）
5. 枠線の配置
6. 余白のバランス"
```

## 検証チェックリスト

| 項目 | 確認内容 |
|------|----------|
| ページサイズ | A4 (210mm x 297mm) |
| 写真枠 | 4:3比率、枠内にフィット |
| 情報欄 | 写真右側に配置 |
| フォント | 明朝体（MS明朝/游明朝） |
| 余白 | 10mm四方 |
| 枠線 | グレー(0.7)、0.5pt |

## 問題発生時

1. **写真が小さい** → printpdf 0.8はDPIベースで画像サイズ計算
   - 修正: `dpi = img_width_px * 72 / target_width_pt` で計算
   - `XObjectTransform { dpi: Some(dpi), .. }` を使用
2. 写真がはみ出す → アスペクト比計算を確認
3. 文字化け → フォント読み込み処理を確認
4. 枠線ずれ → pt/mm変換係数を確認

## printpdf 0.8 画像サイズ計算

```rust
// 公式: img_width_px * (72 / dpi) = target_width_pt
// よって: dpi = img_width_px * 72 / target_width_pt
let dpi = img_width as f32 * 72.0 / draw_width_pt;

ops.push(Op::UseXobject {
    id: image_id.clone(),
    transform: XObjectTransform {
        translate_x: Some(Pt(x)),
        translate_y: Some(Pt(y)),
        dpi: Some(dpi),  // scale_x/scale_yではなくdpiを使用
        ..Default::default()
    },
});
```

## 関連ファイル

- `src/export/pdf.rs` - PDF生成ロジック
- `src/export/layout.rs` - レイアウト定数
