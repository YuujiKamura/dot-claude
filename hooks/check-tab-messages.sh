#!/bin/bash
# タブ間メッセージをチェックするフック
TAB_REGISTRY_DIR=~/logs/tabs

# デバッグ: フックが実行されたことを記録
echo "$(date): hook executed" >> ~/logs/tabs/hook.log

# 全.msgファイルをチェック
messages=""
for msgfile in "$TAB_REGISTRY_DIR"/*.msg; do
  [ -f "$msgfile" ] || continue
  if [ -s "$msgfile" ]; then
    content=$(cat "$msgfile")
    messages="${messages}${content}\n"
    > "$msgfile"  # 読んだら消す
  fi
done

# メッセージがあればJSON形式で出力（Claudeのコンテキストに追加される）
if [ -n "$messages" ]; then
  # JSON用にエスケープ
  escaped=$(echo -e "$messages" | sed 's/\\/\\\\/g; s/"/\\"/g' | tr '\n' ' ')
  echo "{\"hookSpecificOutput\":{\"hookEventName\":\"PostToolUse\",\"additionalContext\":\"📨 タブからのメッセージ: $escaped\"}}"
fi

exit 0
