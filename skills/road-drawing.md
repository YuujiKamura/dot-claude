---
name: road-drawing
description: road-drawingリポジトリの開発支援。DXF図面生成CLI（路線展開図・区画線・三角形リスト）。CSV/Excel入力→DXF出力。DXF、展開図、路線図、区画線、横断図、road-drawingと言われた時に使用。
---

# road-drawing

Excel/CSVから路線展開図・区画線展開図・三角形リストのDXFを生成するRustプロジェクト。

**リポジトリ**: `~/road-drawing`

## CLI Usage

```bash
# 路線展開図（デフォルト）
road-drawing generate -i data.csv -o output.dxf --type road-section

# 区間指定（excel-parserパイプライン使用）
road-drawing generate -i data.csv -o output.dxf --section 区間1

# 区間一覧表示
road-drawing generate -i data.csv -o unused.dxf --list-sections

# 区画線（JSONコマンド）
road-drawing generate -i commands.json -o output.dxf --type marking

# 三角形リスト
road-drawing generate -i triangles.csv -o output.dxf --type triangle

# スケール変更
road-drawing generate -i data.csv -o output.dxf --scale 500
```

## Crate Structure

```
crates/
├── dxf-engine/     — DXFエンティティ(Line/Text/Circle/LwPolyline)、Writer、Reader、Linter、Index
├── road-section/   — 路線展開図ジオメトリ計算 (StationData → geometry → DXF)
├── road-marking/   — 区画線生成 (横断歩道ストライプ、JSONコマンド実行)
├── excel-parser/   — Excel/CSVパース (区間検出、測点名生成、累積距離変換、パイプライン)
└── triangle-core/  — 三角形リスト (Heron面積、接続チェーン、CSV読込)
cli/                — road-drawing CLIツール
```

## Input Formats

### road-section CSV
```csv
測点名,累積延長,左幅員,右幅員
No.0,0.0,2.5,2.5
No.1,20.0,3.0,3.0
```
- ヘッダーあり/なし両対応。英語ヘッダー(`name,x,wl,wr`)も可
- `#`始まりはコメント行、空行はスキップ
- Shift_JISファイルも自動検出

### 台形計算書（multi-section）
```csv
区間1,台形計算,,,
測点名,単延長L,幅員W,平均幅員Wa,面積m2
No.0,0,0.8,,
,1.15,0.63,0.715,0.82
```
- `--section 区間1`で区間指定、`--list-sections`で一覧
- 単延長→累積距離自動変換、測点名自動補完

### marking JSON
```json
{"commands": [{"type": "crosswalk", "params": {"startOffset": "11000", "stripeCount": "7"}}]}
```
- params: startOffset, stripeLength, stripeWidth, stripeCount, stripeSpacing, layer

### triangle CSV
```csv
koujiname,テスト工事
rosenname,テスト路線
gyousyaname,テスト
zumennum,1
1,10.0,8.0,6.0,-1,-1
2,5.0,4.0,3.0,1,1
```
- ヘッダー4行(koujiname/rosenname/gyousyaname/zumennum) + データ行
- データ: 番号,辺a,辺b,辺c,親番号,接続タイプ

## Key APIs

```rust
// road-section: CSV → DXF
let stations = parse_road_section_csv(csv_str)?;
let geometry = calculate_road_section(&stations, &RoadSectionConfig::default());
let (lines, texts) = geometry_to_dxf(&geometry);

// excel-parser: 区間検出 + パイプライン
let sections = get_available_sections(&text, &filename);
let rows = extract_and_transform_text(&text, "区間1")?;

// road-marking: 横断歩道生成
let stripes = generate_crosswalk(&centerlines, &CrosswalkConfig::default());

// road-marking: JSONコマンド実行
let cmd = parse_command(json)?;
let result = execute_command(&cmd, &centerlines);

// DXF出力 + Lint検証
let writer = DxfWriter::new();
let dxf = writer.write(&lines, &texts);
assert!(DxfLinter::is_valid(&dxf));
```

## Rules

- DXF出力は必ず`DxfLinter::is_valid()`で検証
- スケール変換はm→mm（×1000）で統一
- 測点名ラベルはDXF color 5 (blue)、回転-90°、高さ350
- テスト命名: `test_marking_`プレフィックス必須（並列エージェント名前衝突防止）
- ビルド: `cargo build` / `cargo test`
