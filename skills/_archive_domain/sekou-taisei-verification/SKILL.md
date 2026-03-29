# 施工体制書類整合性チェック スキル

施工体制台帳の記載内容と、根拠となるPDF書類（建設業許可証、健康保険証明書、労働保険証明書等）をGemini APIで照合し、不整合を検出・修正するスキル。

## 使用タイミング

- 施工体制台帳、施工体制シート、整合性チェック、書類確認と言われた時に使用
- 新規下請業者の書類登録時
- 定期的な書類更新確認時

## 必要な情報

1. **sekoutaisei.json** - 各社の書類URL（Google Drive）
2. **施工体制シート** - 各下請業者の記載内容（Google Sheets）
3. **Gemini API Key** - PDF読み取り用

## チェック項目

| 項目 | 確認内容 |
|------|----------|
| 建設業許可番号 | 例: (般-6)第5001号 |
| 許可年月日 | 書類右上の日付（提出日） |
| 健康保険番号 | 事業所番号 |
| 労働保険番号 | 概算確定保険料申告書の番号 |
| 主任技術者 | 氏名と資格番号 |
| 法定外労災 | 加入証明書の有効期限 |

## 実装コード

### 1. Drive APIでPDF取得

```python
from pathlib import Path
from google.oauth2.credentials import Credentials
import googleapiclient.discovery
import base64
import requests

project_root = Path(r"C:\Users\yuuji\Sanyuu2Kouku\cursor_tools\summarygenerator")
token_path = project_root / "gmail_token.json"

SCOPES = [
    'https://www.googleapis.com/auth/drive.readonly',
    'https://www.googleapis.com/auth/spreadsheets'
]

def get_drive_service():
    creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
    return googleapiclient.discovery.build('drive', 'v3', credentials=creds)

def download_pdf_as_base64(drive_service, file_id):
    """Google DriveからPDFをダウンロードしてBase64エンコード"""
    request = drive_service.files().get_media(fileId=file_id)
    content = request.execute()
    return base64.standard_b64encode(content).decode('utf-8')

def extract_file_id_from_url(url):
    """Google Drive URLからファイルIDを抽出"""
    import re
    patterns = [
        r'/file/d/([a-zA-Z0-9-_]+)',
        r'id=([a-zA-Z0-9-_]+)',
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None
```

### 2. Gemini APIでPDF内容を読み取り

```python
def read_pdf_with_gemini(pdf_base64, prompt, api_key):
    """Gemini APIでPDFの内容を読み取る"""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key={api_key}"

    payload = {
        "contents": [{
            "parts": [
                {
                    "inline_data": {
                        "mime_type": "application/pdf",
                        "data": pdf_base64
                    }
                },
                {
                    "text": prompt
                }
            ]
        }]
    }

    response = requests.post(url, json=payload)
    result = response.json()

    return result['candidates'][0]['content']['parts'][0]['text']
```

### 3. 整合性チェック実行

```python
def check_contractor_documents(contractor_data, gemini_api_key):
    """下請業者の書類整合性をチェック"""
    drive_service = get_drive_service()
    results = {}

    # 建設業許可証チェック
    if '01_建設業許可' in contractor_data['docs']:
        doc = contractor_data['docs']['01_建設業許可']
        if doc.get('url'):
            file_id = extract_file_id_from_url(doc['url'])
            pdf_base64 = download_pdf_as_base64(drive_service, file_id)

            prompt = """この建設業許可証から以下の情報を抽出してください:
1. 許可番号（例: (般-6)第5001号）
2. 許可年月日（書類右上の日付）
JSON形式で回答: {"permit_number": "...", "permit_date": "..."}"""

            response = read_pdf_with_gemini(pdf_base64, prompt, gemini_api_key)
            results['建設業許可'] = parse_json_response(response)

    # 健康保険証チェック
    if '02_事業所番号' in contractor_data['docs']:
        doc = contractor_data['docs']['02_事業所番号']
        if doc.get('url'):
            file_id = extract_file_id_from_url(doc['url'])
            pdf_base64 = download_pdf_as_base64(drive_service, file_id)

            prompt = """この書類から事業所番号（健康保険番号）を抽出してください。
JSON形式で回答: {"insurance_number": "..."}"""

            response = read_pdf_with_gemini(pdf_base64, prompt, gemini_api_key)
            results['健康保険'] = parse_json_response(response)

    # 労働保険証チェック
    if '03_労働保険番号' in contractor_data['docs']:
        doc = contractor_data['docs']['03_労働保険番号']
        if doc.get('url'):
            file_id = extract_file_id_from_url(doc['url'])
            pdf_base64 = download_pdf_as_base64(drive_service, file_id)

            prompt = """この労働保険概算確定保険料申告書から労働保険番号を抽出してください。
数字のみで回答（ハイフンなし）: {"labor_insurance": "..."}"""

            response = read_pdf_with_gemini(pdf_base64, prompt, gemini_api_key)
            results['労働保険'] = parse_json_response(response)

    return results
```

### 4. スプレッドシートとの比較

```python
def compare_with_spreadsheet(sheets_service, spreadsheet_id, pdf_results):
    """施工体制シートの値とPDF読み取り結果を比較"""
    # シートから現在の値を取得
    sheet_values = read_google_sheet(sheets_service, spreadsheet_id, '工事内容', 'A:C')

    discrepancies = []

    # 各項目を比較
    for item_name, pdf_value in pdf_results.items():
        sheet_value = find_value_in_sheet(sheet_values, item_name)

        # 番号の正規化（ハイフン、スペース除去）して比較
        normalized_pdf = normalize_number(pdf_value)
        normalized_sheet = normalize_number(sheet_value)

        if normalized_pdf != normalized_sheet:
            discrepancies.append({
                'item': item_name,
                'sheet_value': sheet_value,
                'pdf_value': pdf_value,
                'status': 'mismatch'
            })

    return discrepancies

def normalize_number(value):
    """番号を正規化（比較用）"""
    if not value:
        return ''
    import re
    return re.sub(r'[-\s　]', '', str(value))
```

### 5. 修正の適用

```python
def apply_fixes(sheets_service, spreadsheet_id, discrepancies):
    """不整合を施工体制シートに反映"""
    for item in discrepancies:
        if item['status'] == 'mismatch':
            # セルアドレスを特定して更新
            cell_address = get_cell_address_for_item(item['item'])
            update_cell(sheets_service, spreadsheet_id, '工事内容', cell_address, item['pdf_value'])
            print(f"修正: {item['item']} {item['sheet_value']} → {item['pdf_value']}")
```

## 結果の保存形式

```json
{
  "verification": {
    "last_checked": "2025-12-31",
    "results": [
      {
        "contractor": "業者名",
        "status": "ok|warning|error",
        "items": {
          "建設業許可": {"status": "ok", "sheet": "値", "pdf": "値"},
          "健康保険": {"status": "missing", "note": "未提出"},
          "主任技術者": {"status": "fixed", "old": "旧値", "new": "新値"}
        }
      }
    ]
  }
}
```

## 提出先・提出日チェック

暴対法誓約書や作業員名簿など、提出先名称や提出日が空欄になっていないかをチェックする機能。

### チェック対象書類

- `08_作業員名簿` - 作業員名簿（PDF形式のみ）
- `09_暴対法誓約書` - 暴力団排除誓約書

### チェック内容

1. **提出先の空欄検出**
   - 「殿」「様」「御中」のみで会社名がない
   - 完全に空欄

2. **提出日の空欄検出**
   - 「令和　年　月　日」のように数字が入っていない
   - 完全に空欄

3. **工期との整合性**
   - 提出日が工期開始の3ヶ月以上前 → 警告
   - 提出日が工期終了の3ヶ月以上後 → 警告

### 実行スクリプト

```bash
python C:\Users\yuuji\Sanyuu2Kouku\SekouTaiseiMaker\scripts\check_document_dates.py
```

### Gemini API プロンプト

```python
prompt = """この書類から以下の情報を抽出してください:

1. 提出先（宛先）: 書類の冒頭にある「○○殿」や「○○様」の部分。空欄の場合は「空欄」と回答。
2. 提出日/作成日: 書類の右上や署名欄付近にある日付。空欄の場合は「空欄」と回答。

JSON形式で回答:
{
  "destination": "提出先の名称（空欄の場合は「空欄」）",
  "date": "日付（令和X年X月X日形式、空欄の場合は「空欄」）"
}"""
```

### 空欄判定ロジック

```python
# 提出先の空欄判定
dest_is_empty = (
    not destination or
    destination in ['空欄', '記載なし', 'なし', '空', '殿', '様', '御中'] or
    len(destination.replace('殿', '').replace('様', '').replace('御中', '').strip()) == 0
)

# 日付の空欄判定
date_is_empty = (
    not date_str or
    date_str in ['空欄', '記載なし', 'なし', '空'] or
    re.match(r'^令和\s*年\s*月\s*日$', date_str) or  # 数字なしパターン
    not re.search(r'\d', date_str)  # 数字が含まれていない
)
```

### 結果保存形式

```json
{
  "check_date": "2025-12-31T13:54:38",
  "project_name": "工事名",
  "results": [
    {
      "contractor": "業者名",
      "doc_type": "09_暴対法誓約書",
      "file": "ファイル名.pdf",
      "destination": "御中",
      "date": "令和 年 月 日",
      "warnings": [
        "提出先が空欄または未記入",
        "提出日が空欄または未記入 (令和 年 月 日)"
      ]
    }
  ]
}
```

## 注意事項

1. **修正先は施工体制シート** - 施工体制台帳はIMPORTRANGEで参照しているため、元データを修正する
2. **許可年月日の意味** - 許可の有効期間開始日ではなく、書類右上の提出日付
3. **番号の正規化** - ハイフンやスペースの有無で不一致と判定しないよう正規化して比較
4. **Geminiモデル** - `gemini-2.0-flash-exp` を使用（PDF読み取り対応）
5. **スプレッドシート形式はスキップ** - xlsx形式の作業員名簿はGemini APIで読めないためスキップ
