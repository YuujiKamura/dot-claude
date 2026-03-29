---
name: field-data-normalization
description: "CLI & Tooling. (Single Source of Truth for Cumulative Field Data) Use when user mentions: CLI, script, automation, tool, plugin, extension, config."
---

# CLI & Tooling

Patterns: 1

## 1. Single Source of Truth for Cumulative Field Data

In domains like construction photo management where data is recorded cumulatively (e.g., multiple temperature readings on a single blackboard), relying on master-data 'remarks' leads to data contamination. AI-detected focal targets (focusTarget) should be the Single Source of Truth to prevent erroneous data propagation in grouped entries.

### Steps

1. Prioritize AI focus-target labels over manual remarks or master-lookup values during extraction.
2. Consolidate domain-specific labels into a strongly-typed Enum to eliminate string-match drift across multiple modules.
3. Implement a prioritized fallback logic: FocusTarget -> DetectedText (OCR) -> Remarks.



