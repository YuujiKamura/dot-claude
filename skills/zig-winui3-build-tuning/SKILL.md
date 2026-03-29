---
name: zig-winui3-build-tuning
description: "-Dslow-safety=false for responsive debug builds. Use when: debug build slow, COM boundary overhead, build-winui3.sh flags, winui3 runtime"
project: ghostty-win
---

# Testing & QA

Patterns: 1

## 1. Selective Safety Disabling for UI Interactivity

Full Zig runtime safety checks can make WinUI3 debug builds unusable due to the high volume of COM/WinRT boundary crossings. Selective disabling of 'slow' safety checks is critical for maintaining developer productivity.

### Steps

1. Identify performance bottlenecks caused by exhaustive integrity checks in debug builds that break UI responsiveness.
2. Use custom build flags (e.g., `-Dslow-safety=false`) to bypass expensive checks while maintaining core logic assertions.
3. Ensure build scripts enforce consistent runtime targets (e.g., `winui3` (consolidated from former `winui3_islands`)) to prevent binary mismatches.

### Examples

```bash
exec zig build -Dapp-runtime=winui3 -Dslow-safety=false --prefix zig-out-winui3 "$@"
```



