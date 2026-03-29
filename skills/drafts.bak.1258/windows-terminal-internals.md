---
name: windows-terminal-internals
description: "CLI & Tooling. (Build-Specific IPC Limitations (Store vs. Dev)) Use when user mentions: CLI, script, automation, tool, plugin, extension, config."
---

# CLI & Tooling

Patterns: 1

## 1. Build-Specific IPC Limitations (Store vs. Dev)

The Windows Store version of Windows Terminal has stricter sandboxing and a different codebase than Dev/Preview builds, which can physically lack the infrastructure for custom IPC 'Control Planes'.

### Steps

1. Prioritize verifying the host build (Store vs. Dev) before debugging IPC timeouts or polling failures.
2. Recognize that Store-distributed apps often block named pipe bridging or lack the necessary hooks (like the 'Control Plane' codebase) required for external agent control.
3. When IPC bridging fails, pivot immediately to environment-level workarounds (e.g., `--yolo` flags or switching to WT Dev) rather than adjusting code-level timeout parameters.

### Examples

```bash
# Workaround when IPC cannot bridge to Store version
gemini --yolo
```



