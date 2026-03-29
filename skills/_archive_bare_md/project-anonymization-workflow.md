---
name: project-anonymization-workflow
description: "公開リポジトリへのpush前に機密情報（工事場所、個人名、内部ID等）をサニタイズするワークフロー。匿名化、サニタイズ、機密、公開、skill-pack、リポジトリ公開と言われた時に使用。"
---

# プロジェクト匿名化ワークフロー

## 1. サニタイズ対象

コードだけでなく以下も対象:
- Markdownファイル（スキル定義、完了報告書、要約）
- 工事名・場所の固有名詞（例: 「小峯2丁目」）
- Google CloudプロジェクトID、Google Drive内部ID
- 個人名・会社名
- インデックステンプレート内の地名・番号

## 2. 高密度ファイルを優先

「要約」「完了報告書」「インデックス」ファイルは固有名詞が集中する。これらを最優先で監査。

## 3. 手順

1. `gh repo view --json visibility` でリポジトリがpublicか確認
2. publicなら全.mdファイルをgrepで固有名詞スキャン
3. 固有名詞をジェネリックプレースホルダに置換（例: `{PROJECT_NAME}`, `{LOCATION}`）
4. `.gitignore`に含めるべきファイルがないか確認

## 4. 過去の事例

- `skill-pack` (2026-03-17): 公開前監査で工事場所、GCPプロジェクトID、個人名、Drive内部IDの混入を検出
- `photo-album-web` (2026-02-17): base64埋め込みHTMLで写真が丸見え → private化
