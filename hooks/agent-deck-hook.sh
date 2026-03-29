#!/bin/bash
# Agent-deck hook handler wrapper
# Reads stdin (Claude hook JSON), extracts session_id for AGENTDECK_INSTANCE_ID,
# then pipes the same JSON to agent-deck hook-handler.
INPUT=$(cat)
SID=$(echo "$INPUT" | sed -n 's/.*"session_id":"\([^"]*\)".*/\1/p')
EVENT=$(echo "$INPUT" | sed -n 's/.*"hook_event_name":"\([^"]*\)".*/\1/p')
AGENT_PID="${AGENTDECK_AGENT_PID:-$PPID}"
export AGENTDECK_INSTANCE_ID="${SID:-claude-unknown}"
export AGENTDECK_AGENT_PID="$AGENT_PID"

kill_agent_children() {
  local parent_pid="$1"
  [ -n "$parent_pid" ] || return 0
  if [ "${AGENTDECK_HOOK_TEST_MODE:-}" = "1" ]; then
    echo "TEST_KILL_CHILDREN:$parent_pid"
    return 0
  fi
  powershell.exe -NoProfile -ExecutionPolicy Bypass -Command \
    "Get-CimInstance Win32_Process -Filter \"ParentProcessId = $parent_pid\" | ForEach-Object { Stop-Process -Id \$_.ProcessId -Force -ErrorAction SilentlyContinue }" \
    >/dev/null 2>&1 || true
}

if [ "$EVENT" = "SessionEnd" ]; then
  kill_agent_children "$AGENT_PID"
fi

if [ "${AGENTDECK_HOOK_TEST_MODE:-}" = "1" ]; then
  echo "TEST_INSTANCE_ID:${AGENTDECK_INSTANCE_ID}"
  echo "TEST_EVENT:${EVENT}"
  echo "TEST_AGENT_PID:${AGENTDECK_AGENT_PID}"
  exit 0
fi

echo "$INPUT" | exec /c/Users/yuuji/agent-deck/agent-deck.exe hook-handler
