---
name: winui3-native-rendering
description: "CLI & Tooling. (Practical Minimum Dimension Guarding) Use when user mentions: CLI, script, automation, tool, plugin, extension, config."
---

# CLI & Tooling

Patterns: 1

## 1. Practical Minimum Dimension Guarding

WinUI 3 layout cycles often report transient 1px dimensions during early measurement frames, which causes native render target (SwapChain) initialization to fail or default to unusable sizes.

### Steps

1. Simple `>0` guards for height/width are insufficient during initial layout: WinUI 3 containers (like TabView) frequently pass through a `1px` state during early measurement. Creating a swap chain at this dimension leads to rendering artifacts or immediate crashes.
2. Guard rendering initialization with a 'practical minimum' (e.g., `>=32px`) to ensure the layout has stabilized. This avoids race conditions where the native buffer is created for transient, unusable dimensions.
3. Isolate the rendering container from complex parent layouts to distinguish between native interop bugs and layout constraints. If a feature works in a direct window but fails in a TabView, the root cause is typically the parent's measure/arrange logic (reporting 0/1px) rather than the native code.

### Examples

```
if (actual_width < 32 || actual_height < 32) return; // Guard against 1px transient state
```

```
$env:GHOSTTY_WINUI3_ENABLE_TABVIEW='false'; ./ghostty.exe // Isolation test to verify layout vs interop
```



