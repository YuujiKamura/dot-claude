# Excel シート抽出・値置換・PDF出力

Excelブックから特定シートを抜き出して独立ファイルにし、PDF出力する。(1) 元ファイルコピーによる書式完全保持、(2) 他シート参照数式を値に置換、(3) 条件付き書式の除去、(4) win32com経由のExcelページ設定を活かしたPDF出力。Excel、シート抽出、PDF、数式置換、条件付き書式、win32comと言われた時に使用。

## なぜこの手順か

- openpyxlのセルコピーでは書式（結合セル・列幅・罫線・フォント等）が不完全になる
- **元ファイルを丸ごとコピーし不要シートを削除**する方が書式を完全に保持できる
- シート削除後は他シートへの数式参照が `#REF!` になるため、削除前に値を取得して置換する
- PDF出力はwin32com（Excel COM）経由が唯一ページ設定を完全再現する方法

## 手順

### Step 1: 元ファイルをコピー

```bash
cp "元ファイル.xlsx" "抽出先.xlsx"
```

- Pythonの`shutil.copy2`はExcel/DriveFSのロックに引っかかることがある。bashの`cp`も同様の場合は別名で作成する

### Step 2: 数式の参照先から値を収集

```python
import openpyxl

src_wb = openpyxl.load_workbook("元ファイル.xlsx")

# 参照先シート（例: 基本情報入力）から値を取得
ref_sheet = src_wb["基本情報入力"]
values = {
    "J4": ref_sheet["J4"].value,  # 工事名
    "J6": ref_sheet["J6"].value,  # 発注者
    # ... 必要なセルを列挙
}
```

**注意**: `data_only=True`はExcelで開いて保存済みでないとNoneになる。数式の参照先シートから直接値を読む方が確実。

### Step 3: 不要シートを削除し数式を値に置換

```python
wb = openpyxl.load_workbook("抽出先.xlsx")

# 残すシートを特定
keep = "完成通知書"  # 例
to_delete = [n for n in wb.sheetnames if n != keep]
for name in to_delete:
    del wb[name]

# 数式セルを値に置換
ws = wb[keep]
for row in ws.iter_rows():
    for cell in row:
        if cell.value and isinstance(cell.value, str) and cell.value.startswith("="):
            # Step 2で収集した値で置換
            cell.value = resolve_value(cell.coordinate, values)
```

### Step 4: 条件付き書式を削除

```python
ws.conditional_formatting._cf_rules.clear()
wb.save("抽出先.xlsx")
```

- 入力促進用の黄色ハイライト等、提出時に不要な条件付き書式を除去

### Step 5: win32comでPDF出力

```python
import win32com.client, os

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = False
excel.DisplayAlerts = False

try:
    wb = excel.Workbooks.Open(os.path.abspath("抽出先.xlsx"))
    wb.ExportAsFixedFormat(0, os.path.abspath("出力.pdf"))  # 0 = PDF
    wb.Close(False)
finally:
    excel.Quit()
```

- `ExportAsFixedFormat(0, path)`: Type=0がPDF。Excelのページ設定（用紙サイズ・余白・印刷範囲・拡大縮小）が完全に反映される
- **必ず絶対パスを渡す**。相対パスだとExcelのカレントディレクトリ基準になり失敗する

## ファイルロック対策

| 状況 | 対処 |
|---|---|
| shutil.copy2がPermissionError | bashの`cp`を使う or 別名で作成 |
| 出力先がExcelで開かれている | `_new`サフィックス付き別名で作成し、後でリネーム |
| Google DriveFS同期中 | 数秒待って再試行 |

## よくある落とし穴

- openpyxlのセル単位コピーは**書式が崩れる**。シート抽出には「丸コピー＋不要シート削除」一択
- `data_only=True`は**Excelで計算・保存済みでないと値がNone**。参照先シートから直接読め
- openpyxlは**DrawingML（図形・画像）を保持しない**。図形がある場合はwin32comで全操作するか、図形の欠落を許容する
- 条件付き書式の`_cf_rules.clear()`はundocumentedだが動作する
