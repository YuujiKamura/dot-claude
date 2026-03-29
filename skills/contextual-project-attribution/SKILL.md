---
name: contextual-project-attribution
description: "working_dirメタデータでマルチプロジェクト活動を正確に分類。Use when: project attribution, working_dir, misattribution, LLM classifier"
category: cli-tooling
---

# CLI & Tooling

Patterns: 1

## 1. Metadata-Driven Activity Mapping

Using environmental metadata rather than string-matching snippets to correctly attribute developer work to specific projects.

### Steps

1. Hardcoded string matching or regex on history snippets is fragile and frequently misattributes work in multi-project environments.
2. Reliable attribution requires passing the full context—active working directory, prompt start, and response start—to an LLM for classification.
3. Prioritizing the directory state over message content prevents 'false positive' attribution when the user asks generic questions about tooling.

### Examples

```
// src/extractor.rs change to pass working_dir + message_head to the classifier
```



