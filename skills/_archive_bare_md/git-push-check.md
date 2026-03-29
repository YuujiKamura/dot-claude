---
name: git-push-check
description: "ローカルリポのpush漏れ・未コミット検知。セッション開始時に全リポをスキャンしてunpushed/dirtyを報告。push漏れ、未push、dirty、git status、リポ一覧、棚卸しと言われた時に使用。"
categories: [git, devops, session-management]
---

# Git Push漏れチェック

## 検知対象

1. **unpushed commits**: `git log @{u}..HEAD` が1件以上
2. **dirty working tree**: `git status --porcelain` が出力あり
3. **no remote**: リモートが未設定のgitリポ

## 実行方法

```bash
for dir in ~/*/; do
  [ -d "$dir/.git" ] || continue
  cd "$dir"
  name=$(basename "$dir")
  unpushed=$(git log --oneline @{u}..HEAD 2>/dev/null | wc -l)
  dirty=$(git status --porcelain 2>/dev/null | wc -l)
  if [ "$unpushed" -gt 0 ] || [ "$dirty" -gt 0 ]; then
    echo "$name: unpushed=$unpushed dirty=$dirty"
  fi
  cd ~
done
```

## push前チェック

PUBLIC リポへのpush前に必ず:
1. `gh repo view --json visibility -q '.visibility'` で可視性確認
2. diffに機密データ（工事場所、個人名、API key）がないかgrep
3. LOCAL_APPDATA_FONTCONFIG_CACHE/, logs/, tmp/ は.gitignoreに入れる

## SessionStartフックへの統合

skill-minerの`check`サブコマンドとしてRustで実装し、daily-summary.shから呼ぶのが理想。
暫定的にはシェルスクリプトをフックに追加。
