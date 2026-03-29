---
name: contactsheet-pairing
description: コンタクトシート方式による着手前/竣工写真のペアリング。(1) Before/Afterを番号付きグリッド画像に合成、(2) 1コール1問で番号回答、(3) 順逆走査アンサンブルで安定化、(4) 90%精度達成。ペアリング、コンタクトシート、着手前、竣工、写真マッチング、pair-completionと言われた時に使用。
---

# コンタクトシート方式ペアリング

## 概要

舗装打換え工事の着手前写真と竣工写真を場所でペアリングする手法。
個別ファイル渡し(10%)→コンタクトシート(75%)→アンサンブル(90%)。

## コンタクトシート生成

- Before/Afterそれぞれを番号付きグリッド画像1枚に合成（Pillow）
- Before: 5列×4行（20枚）、After: 7列×3行（21枚）
- 各セル: 267×200px + 黒帯ラベル22px（B01, A01等）
- セル間ギャップ4px
- ファイル名ソート順のまま配置（シャッフルしない）

## プロンプト設計

```
傷んだ舗装をなおしている道路工事の着手前竣工写真のペアリングである。

Image 1 is a numbered grid of BEFORE-construction road photos (B01-B20).
Image 2 is a numbered grid of AFTER-construction road photos (A01-A21).

Which AFTER number (A01-A21) shows the SAME road location as {query}?
Match by: vanishing point direction, building silhouettes, road width, surrounding structures.
Output ONLY the number like A07.
```

### 重要ポイント
- **冒頭にドメイン文脈**: 「傷んだ舗装をなおしている道路工事」と明記。路面が変わるのは当然、周囲で合わせろという暗黙の指示になる
- 1コール1問。一括で全ペアを答えさせると精度が崩壊する
- 回答は番号1個だけ。余計な出力をさせない

## アンサンブル（順逆走査）

単発で外れるケースを救済する。1コール内で3回スキャンを指示:

```
Do 3 independent scans:
Scan 1: Go A01 to A21 in order, pick the best match.
Scan 2: Go A21 to A01 in reverse, pick the best match.
Scan 3: Go A01 to A21 again, pick the best match.

Output format:
Scan1: A??
Scan2: A??
Scan3: A??
Final: A?? (majority vote)
```

- 順走査だけだと先頭寄りの候補に引っ張られるバイアスを逆走査で相殺
- 単発75% → アンサンブル90%（5件中3件修正）

## 残る誤答パターン

- 撮影位置が微妙にずれて道路中心線・ダイヤマーク等が変わるケース
- 隣接番号への1ズレが主。複数回叩くと正解が出る回もある（揺らぎ）
- 撮り直しで解消可能な範囲

## Gemini呼び出し

```python
proc = subprocess.run(
    'gemini -m gemini-3-flash-preview --yolo -o text',
    input=f'@{before_sheet} @{after_sheet} {prompt}',
    capture_output=True, text=True, timeout=300, shell=True
)
```

- モデル: `gemini-3-flash-preview` 必須（未指定だとflash-liteになり精度劣化）
- `@ファイルパス` でstdin経由の画像添付

## 実績

| 方式 | 精度 | 備考 |
|------|------|------|
| 個別ファイル21枚渡し | 10% | アテンション分散 |
| コンタクトシート単発 | 75% | グリッドで一覧化 |
| コンタクトシート+アンサンブル | 90% | 順逆走査3回 |

## 着手前竣工写真帳PDF生成

ペアリング確定後、写真帳PDFを自動生成する。

### レイアウト仕様
- **用紙**: A4横（1754x1240px @150dpi = 841.92×595.32pt）
- **フォント**: 游明朝体（タイトル: yumindb.ttf 48pt、工事名: yumindb.ttf 40pt、キャプション: yuminl.ttf 28pt/24pt）
- **余白**: 上下1cm（59px @150dpi）、左右40px
- **写真領域**: 1674×1032px（枠いっぱい、アスペクト比維持で中央配置）
- **キャプション**: 写真下に測点名（中央揃え）+ 罫線 + 着手前/竣工（中央揃え）+ 罫線、罫線幅550px
- **表紙**: 「着手前-竣工写真」（48pt太字）+ 工事名（40pt太字）、工種は書かない、〇も付けない
- **ページ構成**: 表紙1枚 + 各ペア（着手前→竣工）の交互配置
- **ファイル名**: `着手前竣工_{工事名}.pdf`
- **出力先**: `写真帳まとめ/`

### フォルダ構造
ペアリング後、竣工写真フォルダ内にページ別サブフォルダを作り、着手前JPGと竣工JPGをペアで配置:
```
竣工写真/
├── P01_{測点名}/
│   ├── {before_file}.JPG   # 着手前
│   └── {after_file}.jpg    # 竣工
├── P02_{測点名}/
│   ...
```

### 生成コード要点
- `pairing_manual.json` からペア定義を読む
- フォルダ名 `P{nn}_{測点名}` から測点名を自動取得（正規表現: `r'P(\d+)_(.+)'`）
- Pillow で画像→PDF。`pages[0].save(path, 'PDF', save_all=True, append_images=pages[1:], resolution=150)`
- 日本語パスはPythonで `pathlib.Path(r'H:\...')` で渡す（MSYS2パスだとエンコーディングが壊れる）

## 関連ファイル

- テストスクリプト: `photo-ai-rust/test_contactsheet_pairing.py`
- コンタクトシート: `photo-ai-rust/pairing_thumbs/contact_before.jpg`, `contact_after.jpg`
- GT: `photo-ai-rust/pairing_manual.json`
- Issue: #101
