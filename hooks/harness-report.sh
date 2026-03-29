#!/bin/bash
# harness-report.sh — Summarize harness guard metrics from harness.jsonl
#
# Usage: bash ~/.claude/hooks/harness-report.sh [--json]

METRICS_FILE="$HOME/.claude/metrics/harness.jsonl"

if [ ! -f "$METRICS_FILE" ]; then
    echo "No harness data found at $METRICS_FILE"
    exit 0
fi

TOTAL=$(wc -l < "$METRICS_FILE")
echo "=== Harness Guard Report ==="
echo "Total events: $TOTAL"
echo ""

# Use node with the file path passed as argv, not interpolated into JS
node -e "
const fs = require('fs');
const path = require('path');
const filePath = path.resolve(process.argv[1]);
const lines = fs.readFileSync(filePath, 'utf8').trim().split('\n').filter(l => l);
const byHook = {};
const byAction = {};
const byHookAction = {};

for (const line of lines) {
    try {
        const e = JSON.parse(line);
        byHook[e.hook] = (byHook[e.hook] || 0) + 1;
        byAction[e.action] = (byAction[e.action] || 0) + 1;
        const key = e.hook + ':' + e.action;
        byHookAction[key] = (byHookAction[key] || 0) + 1;
    } catch {}
}

console.log('--- Events by Hook ---');
console.log('');
for (const [hook, count] of Object.entries(byHook).sort((a,b) => b[1]-a[1])) {
    console.log('  ' + hook + ': ' + count);
}

console.log('');
console.log('--- Events by Action ---');
console.log('');
for (const [action, count] of Object.entries(byAction).sort((a,b) => b[1]-a[1])) {
    console.log('  ' + action + ': ' + count);
}

console.log('');
console.log('--- Events by Hook:Action ---');
console.log('');
for (const [key, count] of Object.entries(byHookAction).sort((a,b) => b[1]-a[1])) {
    console.log('  ' + key + ': ' + count);
}

// Blocks vs Formats summary
console.log('');
console.log('--- Blocks vs Formats ---');
console.log('');
const blocked = byAction['blocked'] || 0;
const formatted = byAction['formatted'] || 0;
const passed = byAction['passed'] || 0;
const timeout = byAction['timeout'] || 0;
console.log('  blocked:   ' + blocked);
console.log('  passed:    ' + passed);
console.log('  formatted: ' + formatted);
if (timeout) console.log('  timeout:   ' + timeout);

// Last 10 events
console.log('');
console.log('--- Last 10 Events ---');
console.log('');
const last5 = lines.slice(-10);
for (const line of last5) {
    try {
        const e = JSON.parse(line);
        const ts = e.timestamp || 'unknown';
        const hook = e.hook || '?';
        const action = e.action || '?';
        const file = e.file || e.command || '';
        const reason = e.reason || '';
        const extra = [file, reason].filter(Boolean).join(' | ');
        console.log('  [' + ts + '] ' + hook + ' -> ' + action + (extra ? ' (' + extra + ')' : ''));
    } catch {}
}
" "$METRICS_FILE" 2>/dev/null

echo ""
echo "Raw data: $METRICS_FILE"
