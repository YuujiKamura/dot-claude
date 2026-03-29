---
name: road-drawing
description: "road-drawing CLIとcrateの使い方。CSV/Excel→DXF図面生成。路線展開図、三角形リスト、横断歩道。road-drawing、DXF、展開図、三角形、横断歩道、図面と言われた時に使用。"
project: photo-ai
---

# road-drawing — 図面生成CLI & Rustクレート群

## リポジトリ
`~/road-drawing` (github.com/YuujiKamura/road-drawing)

## CLI使い方

### 路線展開図 (road-section)
```bash
# 単純CSV（name,x,wl,wrの4列）
road-drawing generate --input data.csv --output out.dxf --type road-section

# マルチセクションCSV（区間X,台形計算ヘッダ付き）
road-drawing generate --input 面積計算書.csv --output out.dxf --section 区間3

# 利用可能区間の一覧
road-drawing generate --input 面積計算書.csv --output unused.dxf --list-sections
```

### 三角形リスト (triangle)
```bash
# MIN/CONN/FULL形式CSV → 三角形展開図DXF
road-drawing generate --input triangles.csv --output out.dxf --type triangle
```

### 区画線マーキング (marking)
```bash
# JSON → 横断歩道DXF
road-drawing generate --input commands.json --output out.dxf --type marking
```

## クレート構成

| クレート | 役割 |
|----------|------|
| `dxf-engine` | DXFエンティティ生成・バリデーション・読み込み |
| `road-section` | 路線展開図ジオメトリ計算 |
| `excel-parser` | Excel/CSVパース（セクション検出、測点名生成、距離変換） |
| `triangle-core` | 三角形リスト計算（Heron面積、接続座標、CSV読み込み） |
| `road-marking` | 横断歩道生成、JSONコマンド実行 |

## 入力フォーマット

### 路線展開図CSV（マスタ書式）
```csv
測点名,単延長L,幅員W,幅員右
No.0,0.00,0.80,0.00
0+1.2,1.15,0.63,0.00
```

### 三角形CSV（MIN形式）
```csv
koujiname, 工事名
rosenname, 路線名
gyousyaname, 業者名
zumennum, 1
1, 6.0, 5.0, 4.0
2, 5.0, 4.0, 3.0, 1, 1
```

### マーキングJSON
```json
{"type": "crosswalk", "params": {"startOffset": "11000", "stripeCount": "7"}}
```

## ビルド・テスト
```bash
cargo build
cargo test          # 674+ tests
cargo test -p excel-parser
cargo test -p triangle-core
cargo test -p road-marking
```

## 重要定数
- `PITCH_M = 20.0` — 測点間隔(m)
- `ROUND_N = 2` — 数値丸め桁数
- `SPAN = 20` — 測点名ピッチ
- `scale = 1000.0` — m→mm変換
- `EPSILON = 0.01` — 接続辺長一致判定

## テストデータの場所
- `<project>/csv_to_dxf/data/` — 路線展開図CSV (区間1〜6, data.csv, 面積計算書)
- `<project>/trianglelist/app/src/test/resources/` — 三角形CSV (minimal, connected, 4.11)
