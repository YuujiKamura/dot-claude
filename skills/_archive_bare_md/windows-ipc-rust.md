---
name: windows-ipc-rust
description: "CLI & Tooling. (Non-blocking Named Pipe Recovery in Rust) Use when user mentions: CLI, script, automation, tool, plugin, extension, config."
---

# CLI & Tooling

Patterns: 1

## 1. Non-blocking Named Pipe Recovery in Rust

Standard PowerShell or C++ async/wait implementations often block UI threads during high-output agent activity. A dedicated Rust CLI using Win32 pipe primitives provides robust recovery without deadlocks.

### Steps

1. Avoid using `RunAsync` with fixed `wait_for` durations in the main UI thread; this causes the application to freeze when pipes are locked by heavy I/O.
2. Implement a dedicated IPC helper (e.g., `agent-ctl`) that uses `WaitNamedPipeW` with a specific timeout (e.g., 5s) to detect busy pipes.
3. Apply a jittered backoff strategy (e.g., 2-second delay) and a strict retry limit (e.g., 3 attempts) to handle 'Pipe Busy' errors gracefully instead of failing immediately.
4. Use Rust for IPC logic to leverage low-level Win32 API control while maintaining memory safety during high-concurrency pipe operations.

### Examples

```rust
// src/pipe.rs pattern for robust connection
loop {
 if WaitNamedPipeW(pipe_name, 5000) != 0 {
 break Ok(File::open(pipe_name)?);
 }
 if retry_count >= 3 { return Err(Timeout); }
 sleep(Duration::from_secs(2));
 retry_count += 1;
}
```



