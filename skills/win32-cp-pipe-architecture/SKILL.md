---
name: win32-cp-pipe-architecture
description: "Windows/Native Development. (CP Pipe Server, captureSnapshot, Command Thread Only, Session File Lifecycle) Use when user mentions: Named Pipe, control plane, CP pipe, captureSnapshot, ghost window, pipe server, TAIL, STATE."
project: ghostty-win
---

# Win32 CP Pipe Architecture

## Architecture (post-cleanup)

One command pipe thread. No event threads. No subscriber tracking.

```
ghostty.exe
  └─ PipeServer
       └─ serverThread (command handler)
            ├─ PING → PONG (pipe thread, no UI)
            ├─ STATE → captureSnapshot (1 SendMessageW)
            ├─ TAIL → captureSnapshot (1 SendMessageW)
            ├─ LIST_TABS → captureTabList (1 SendMessageW)
            ├─ SEND_INPUT → PostMessageW (async)
            ├─ RAW_INPUT → PostMessageW (async)
            ├─ PASTE → PostMessageW (async)
            ├─ NEW_TAB/CLOSE_TAB/SWITCH_TAB/FOCUS → PostMessageW (async)
            ├─ SUBSCRIBE → "SUBSCRIBE_OK" (no-op stub)
            └─ UNSUBSCRIBE → "UNSUBSCRIBE_OK" (no-op stub)
```

## What was deleted
- 2 event server threads (status, output) — ~300 lines
- throttle/flush thread — ~50 lines
- Subscriber tracking (list, lock, delivery) — ~200 lines
- Agent-deck polls TAIL/STATE directly; push events unused

## captureSnapshot (Issue #142)

Provider vtable has 1 read function:
```zig
captureSnapshot: *const fn(ctx, tab_index: usize, result: *CombinedSnapshot) bool
```

CombinedSnapshot: tab_count, active_tab, pwd[4096], title[256], viewport[65536], has_selection.
`sanitize()` clamps all lengths. Returns false → `ERROR|SNAPSHOT_FAILED`.

Old per-field functions (readBuffer, tabCount, etc.) deleted entirely.

## Session File
- Path: `LOCALAPPDATA/ghostty/control-plane/winui3/sessions/{name}.session`
- Contains: pipe_path, pid, hwnd, log_file
- Written on start, removed on stop
- `gtcp list` auto-cleans stale files (PID dead)

## Error Responses
- `ERROR|NO_TABS` — no tabs available
- `ERROR|SNAPSHOT_FAILED` — captureSnapshot returned false
- `ERROR|INTERNAL_ERROR` — catch-all
- `ERROR|PARSE_ERROR` — malformed command

## Key Files
- `~/zig-control-plane/src/pipe_server.zig` — command thread + client handling
- `~/zig-control-plane/src/main.zig` — Provider vtable + handleRequest
- `~/ghostty-win/src/apprt/winui3/control_plane.zig` — provCaptureSnapshot + CpQuery
- `~/ghostty-win/src/apprt/winui3/App.zig` — handleCpQuery (.capture_snapshot)
