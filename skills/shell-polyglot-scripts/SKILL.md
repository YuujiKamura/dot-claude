---
name: shell-polyglot-scripts
description: "Windows CMD + POSIX sh 両対応のpolyglot .cmdスクリプト構築。Use when: cross-platform script, .cmd polyglot, bash+cmd dual"
category: cli-tooling
---

# CLI & Tooling

Patterns: 1

## 1. Cross-Platform Polyglot .cmd Construction

Creating CLI tools that run natively on both Windows and POSIX systems often requires polyglot .cmd files that use specific syntax tricks to remain valid in multiple shell environments simultaneously.

### Steps

1. Implement a script header that is syntactically valid in both Windows CMD and POSIX sh.
2. Use environment-specific redirection to route execution to the appropriate runtime or interpreter without requiring platform-specific wrappers.



