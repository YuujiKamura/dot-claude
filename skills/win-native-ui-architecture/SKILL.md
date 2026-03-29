---
name: win-native-ui-architecture
description: "GTK移植の複雑性→WT準拠のWindows-nativeアーキテクチャに切替。Use when: forced port, GTK paradigm, platform-native, WT alignment, WinUI3 XAML Islands"
project: ghostty-win
---

# Miscellaneous

Patterns: 1

## 1. Platform-Native Reference Alignment

Porting Linux-centric architectures (like GTK-based apps) to Windows often results in 'unreadable' complexity. Aligning with established Windows-native blueprints like Windows Terminal for WinUI 3/XAML Islands implementations significantly reduces implementation friction.

### Steps

1. Identify if the current design is a 'forced port' of a foreign paradigm (e.g., GTK) which leads to convoluted logic.
2. Shift the architectural reference point from the upstream project to a platform-native equivalent (e.g., Windows Terminal for Windows terminal emulators).
3. Treat AI generation of 'confusingly complex' investigation results as a signal that the underlying design is violating platform-native conventions.
4. Prioritize native OS idioms over cross-platform abstractions when UI implementation becomes a bottleneck.

### Examples

```
gh issue create --title "Align implementation with Windows Terminal patterns"
```



