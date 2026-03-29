---
name: windows-tsf-ime-integration
description: "Miscellaneous. (TSF vs. TextBox for Terminal IME) Use when user mentions: ."
---

# Miscellaneous

Patterns: 1

## 1. TSF vs. TextBox for Terminal IME

Decision criteria for implementing Japanese IME in terminal emulators, favoring Text Services Framework (TSF) over high-level UI controls for precise state management.

### Steps

1. Choose TSF over standard TextBox controls because terminals require clause-level decoration (e.g., specific underlines for the active conversion segment) which TextBox abstractions obscure.
2. Prioritize TSF to obtain exact boundaries between committed and uncommitted text; UI control 'diffing' is too imprecise for terminal buffer synchronization.
3. Use TSF to ensure accurate cursor positioning inside the active composition string, allowing the terminal to render the 'pre-edit' state natively within its grid.

### Examples

```
// TSF provides metadata that standard TextBox lacks
const clause_start = composition.getClauseStart();
const clause_end = composition.getClauseEnd();
```



