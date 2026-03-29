---
name: winui3-xaml-islands
description: "CLI & Tooling. (Step-Phase Debugging for WinUI3/XAML Crashes) Use when user mentions: CLI, script, automation, tool, plugin, extension, config."
---

# CLI & Tooling

Patterns: 1

## 1. Step-Phase Debugging for WinUI3/XAML Crashes

Migration to declarative XAML in Zig/WinUI3 often causes immediate freezes or specific EXCEPTION codes during the early initialization phases.

### Steps

1. Map crash events to specific initialization 'steps' (e.g., Step 1: `initXaml`) to differentiate between COM apartment failures and declarative UI syntax errors.
2. Identify `EXCEPTION code=0x80000003` as a potential assertion failure or breakpoint hit within the WinUI3 Island host, often triggered by incorrect threading context during XAML loading.
3. Trace regressions back to the move from programmatic UI generation to declarative XAML to find mismatches in asset loading or host initialization sequence.

### Examples

```log
# Example crash pattern in ghostty_debug.log
[init] initXaml step 1
EXCEPTION code=0x80000003 at 0x7FFA2B45E8D2
```



