---
name: zig-bindgen-fix-validation-loop
description: "Reject bindgen rewrites without compile error evidence. Use when: emit.zig churn, IUnknown/IInspectable rewrite, unvalidated patch"
project: ghostty-win
---

# CLI & Tooling

Patterns: 1

## 1. Avoid architecture-prompt code churn without compile-backed evidence

Large 'investigation/fix generation' prompts produced long `emit.zig` rewrites (COM/IUnknown/IInspectable) but no verified improvement. In this domain, edits are only meaningful when tied to a failing diagnostic and a build result.

### Steps

1. Do not accept broad generated rewrites unless each change maps to a concrete compile error class.
2. Use a failure→fix→rebuild loop; if no error-class reduction is shown, treat the patch as unvalidated noise.
3. Prefer small, diagnostic-linked edits over sweeping interface/prologue rewrites in bindgen code.

### Examples

```bash
zig build
```



