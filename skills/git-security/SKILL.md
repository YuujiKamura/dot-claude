---
name: git-security
description: Gitセキュリティ基本ルール。(1) APIキー・シークレットのコミット防止、(2) .gitignoreの設定確認、(3) 漏洩時の履歴削除と無効化対応。Git、セキュリティ、漏洩、APIキー、シークレット、コミット防止と言われた時に使用。
---

# Git セキュリティ基本ルール

## 絶対にコミットしてはいけないもの

1. **APIキー・シークレット**
   - `AIzaSy...`, `sk-...`, `ghp_...` など
   - `.env` ファイル
   - `credentials.json`, `secrets.yaml`

2. **認証情報**
   - パスワード
   - トークン
   - 秘密鍵 (`*.pem`, `*.key`, `id_rsa`)

3. **個人情報**
   - 顧客データ
   - メールアドレスリスト

## 事前対策

### .gitignore に必ず含めるもの

```gitignore
# 環境変数
.env
.env.*
*.local

# 認証情報
credentials.json
secrets.yaml
*.pem
*.key

# IDE/ツール設定（機密情報が含まれる可能性）
.claude/settings.local.json
```

### コミット前チェック

```bash
# ステージング内容を確認
git diff --cached

# 機密情報パターンを検索
git diff --cached | grep -iE "(api_key|secret|password|token|AIzaSy|sk-)"
```

## 漏洩時の対応

### 1. 即座にキーを無効化
漏洩したキーは**履歴から消す前に無効化**する。履歴削除には時間がかかり、その間に悪用される可能性がある。

### 2. 履歴から完全削除

```bash
# ファイルを履歴から削除
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch <ファイルパス>" \
  --prune-empty --tag-name-filter cat -- --all

# クリーンアップ
rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# 強制プッシュ
git push origin --force --all
```

### 3. 新しいキーを発行
古いキーは二度と使わない。

## Claudeへの指示

- **許可設定にAPIキーを含めない**
  - `Bash(GEMINI_API_KEY="..." npx tsx:*)` ← NG
  - `Bash(npx tsx:*)` ← OK（実行時に環境変数で渡す）

- **コードにハードコードしない**
  ```typescript
  // NG
  const API_KEY = "AIzaSy...";

  // OK
  const API_KEY = process.env.GEMINI_API_KEY;
  ```

- **コミット前に機密情報の有無を確認する**
