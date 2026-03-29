#!/bin/bash
# PostToolUse hook: コミット後にコードベース全体のアーキテクチャレビューを指示
# settings.json の PostToolUse[Bash] に登録して使用

REVIEW_BIN="C:/Users/yuuji/ai-code-review/target/release/review.exe"

INPUT=$(cat)

# Bashツール以外は無視
TOOL_NAME=$(echo "$INPUT" | python -c "import sys,json; print(json.load(sys.stdin).get('tool_name',''))" 2>/dev/null)
[ "$TOOL_NAME" = "Bash" ] || exit 0

# コマンド取得
COMMAND=$(echo "$INPUT" | python -c "import sys,json; print(json.load(sys.stdin).get('tool_input',{}).get('command',''))" 2>/dev/null)

# git commit を含まないなら無視
echo "$COMMAND" | grep -q "git commit" || exit 0

# git push なら無視
echo "$COMMAND" | grep -q "git push" && exit 0

# ツール実行結果を確認（成功したcommitのみ）
STDOUT=$(echo "$INPUT" | python -c "import sys,json; print(json.load(sys.stdin).get('tool_response',{}).get('stdout',''))" 2>/dev/null)
echo "$STDOUT" | grep -q "^\[" || exit 0

# リポジトリのルートを特定
WORK_DIR=""
WORK_DIR=$(echo "$COMMAND" | sed -n 's/.*git -C "\([^"]*\)".*/\1/p' | head -1)
[ -z "$WORK_DIR" ] && WORK_DIR=$(echo "$COMMAND" | sed -n 's/.*git -C \([^ "]*\).*/\1/p' | head -1)
[ -z "$WORK_DIR" ] && WORK_DIR=$(echo "$COMMAND" | sed -n 's/.*cd "\([^"]*\)".*git.*/\1/p' | head -1)
[ -z "$WORK_DIR" ] && WORK_DIR=$(echo "$COMMAND" | sed -n 's/.*cd \([^ ]*\).*&&.*git.*/\1/p' | head -1)

if [ -n "$WORK_DIR" ]; then
  REPO_DIR="$WORK_DIR"
else
  REPO_DIR=$(git rev-parse --show-toplevel 2>/dev/null)
fi
REPO_NAME=$(basename "$REPO_DIR" 2>/dev/null)

MSG="📋 コミット完了（${REPO_NAME}）。\\n\\n"
MSG="${MSG}【必須】コードベース全体のアーキテクチャレビューを実行せよ:\\n"
MSG="${MSG}  ${REVIEW_BIN} --dir ${REPO_DIR} --prompt architecture --context\\n"
MSG="${MSG}⚠指摘があれば修正→再コミット→再レビュー（最大3回）。✓LGTMなら次へ進め。"

printf '{"hookSpecificOutput":{"hookEventName":"PostToolUse","additionalContext":"%s"}}\n' "$MSG"
