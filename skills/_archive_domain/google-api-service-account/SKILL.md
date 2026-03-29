# Google API サービスアカウント認証

サービスアカウントを使ったGoogle Sheets/Drive APIアクセス。OAuthトークン切れの場合の代替手段。

## 認証情報

```
サービスアカウント: C:\Users\yuuji\visionapi-437405-ffd995e97877.json
メールアドレス: test-56@visionapi-437405.iam.gserviceaccount.com
```

## 事前準備

サービスアカウントは個人Driveにアクセスできない。対象フォルダ/ファイルを共有する必要がある：

1. Driveでフォルダを右クリック → 共有
2. `test-56@visionapi-437405.iam.gserviceaccount.com` を追加（閲覧者でOK）

## 基本コード

```python
from google.oauth2.service_account import Credentials
import googleapiclient.discovery

SCOPES = [
    'https://www.googleapis.com/auth/drive.readonly',
    'https://www.googleapis.com/auth/spreadsheets.readonly'
]

creds = Credentials.from_service_account_file(
    r'C:\Users\yuuji\visionapi-437405-ffd995e97877.json',
    scopes=SCOPES
)

drive_service = googleapiclient.discovery.build('drive', 'v3', credentials=creds)
sheets_service = googleapiclient.discovery.build('sheets', 'v4', credentials=creds)
```

## スプレッドシート検索

```python
# 共有されたファイル一覧
response = drive_service.files().list(
    pageSize=50,
    fields='files(id, name, mimeType)'
).execute()

for f in response.get('files', []):
    print(f'{f["name"]} -> {f["id"]}')
```

## シート読み取り

```python
spreadsheet_id = 'XXXXXXXXXX'

# シート一覧
info = sheets_service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
sheet_names = [s['properties']['title'] for s in info.get('sheets', [])]

# データ読み取り
result = sheets_service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range="'シート名'!A1:Z100"
).execute()
rows = result.get('values', [])
```

## 書式付きエクスポート（Excel）

Sheets API values()は値のみ。書式付きはDrive APIのexportを使う：

```python
from googleapiclient.http import MediaIoBaseDownload
import io

request = drive_service.files().export_media(
    fileId=spreadsheet_id,
    mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
)

fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while not done:
    status, done = downloader.next_chunk()

with open('output.xlsx', 'wb') as f:
    f.write(fh.getvalue())
```

## 非表示列を除いてシートをコピー

```python
import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string
from copy import copy

src_wb = openpyxl.load_workbook('source.xlsx')
ws = src_wb['SheetName']

# 非表示列を特定
hidden_cols = set()
for col_letter, dim in ws.column_dimensions.items():
    if dim.hidden:
        hidden_cols.add(column_index_from_string(col_letter))

# 新しいワークブックにコピー（非表示列スキップ）
new_wb = openpyxl.Workbook()
new_ws = new_wb.active

col_mapping = {}
new_col = 1
for old_col in range(1, ws.max_column + 1):
    if old_col not in hidden_cols:
        col_mapping[old_col] = new_col
        new_col += 1

for row in ws.iter_rows():
    for cell in row:
        if cell.column in col_mapping:
            new_cell = new_ws.cell(row=cell.row, column=col_mapping[cell.column], value=cell.value)
            if cell.has_style:
                new_cell.font = copy(cell.font)
                new_cell.border = copy(cell.border)
                new_cell.fill = copy(cell.fill)
                new_cell.number_format = copy(cell.number_format)
                new_cell.alignment = copy(cell.alignment)

new_wb.save('output.xlsx')
```

## 実例：産廃集計表

```
スプレッドシートID: 1KhW3GsB_Zfq2tyQRDy4lpOb6WWJxuwtAgpDa8Lf5uRk
場所: 12 完成届と請求書/6産廃集計表、東区市道２工区.gsheet
```

## 変更履歴

- 2026-02-03: 初版作成。サービスアカウント認証、書式付きエクスポート、非表示列削除を追加
