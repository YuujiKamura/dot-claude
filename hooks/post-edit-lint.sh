#!/bin/bash
# PostToolUse (Write|Edit) — auto lint/format by file extension
# stdin: JSON with tool_input.file_path
# exit 0 always (results via additionalContext)

METRICS_DIR="$HOME/.claude/metrics"
METRICS_FILE="$METRICS_DIR/harness.jsonl"

FILE=$(echo "$CLAUDE_TOOL_INPUT" | node -e "let d='';process.stdin.on('data',c=>d+=c);process.stdin.on('end',()=>{try{console.log(JSON.parse(d).file_path||'')}catch{}})" 2>/dev/null)
[ -z "$FILE" ] && exit 0
[ ! -f "$FILE" ] && exit 0

EXT="${FILE##*.}"
RESULT=""
LANG=""

case "$EXT" in
  rs)
    LANG="rs"
    if command -v rustfmt &>/dev/null; then
      RESULT=$(rustfmt --check "$FILE" 2>&1) || rustfmt "$FILE" 2>/dev/null
    fi
    ;;
  zig)
    LANG="zig"
    if command -v zig &>/dev/null; then
      RESULT=$(zig fmt --check "$FILE" 2>&1) || zig fmt "$FILE" 2>/dev/null
    fi
    ;;
  py)
    LANG="py"
    if command -v black &>/dev/null; then
      RESULT=$(black --check --quiet "$FILE" 2>&1) || black --quiet "$FILE" 2>/dev/null
    fi
    ;;
  js|ts|jsx|tsx|json)
    LANG="$EXT"
    if command -v prettier &>/dev/null; then
      RESULT=$(prettier --check "$FILE" 2>&1) || prettier --write "$FILE" 2>/dev/null
    fi
    ;;
esac

if [ -n "$RESULT" ]; then
  # Log to harness metrics
  mkdir -p "$METRICS_DIR"
  TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
  echo "{\"timestamp\":\"$TS\",\"hook\":\"post-edit-lint\",\"action\":\"formatted\",\"file\":\"$FILE\",\"lang\":\"$LANG\"}" >> "$METRICS_FILE"

  ESCAPED=$(echo "$RESULT" | head -5 | node -e "let d='';process.stdin.on('data',c=>d+=c);process.stdin.on('end',()=>console.log(d.trim().replace(/[\x22]/g,String.fromCharCode(92)+String.fromCharCode(34)).replace(/\n/g,' ')))" 2>/dev/null)
  echo "{\"hookSpecificOutput\":{\"hookEventName\":\"PostToolUse\",\"additionalContext\":\"post-edit-lint: auto-formatted $FILE ($ESCAPED)\"}}"
fi
exit 0
