---
name: oss-contribution-etiquette
description: "upstream PRの前にfork隔離必須。Use when: upstream contribution, gh repo fork, microsoft/terminal, etiquette failure"
category: behavior-guard
---

# CLI & Tooling

Patterns: 1

## 1. Upstream Contribution Hygiene

Working on high-profile public repositories requires strict isolation in a personal fork before any interaction with the main project metadata.

### Steps

1. Blindly pushing to or creating issues in an upstream repository (e.g., microsoft/terminal) is a major etiquette failure that risks immediate rejection. A practitioner knows to establish a fork immediately as a 'sandbox' for experimental changes.
2. Maintain all development-phase issues and branch history in the fork to avoid polluting the main project's metadata, ensuring the upstream remains clean until a solution is fully verified and ready for PR.

### Examples

```bash
# Correct workflow: Fork first, then clone
gh repo fork microsoft/terminal --clone --private
```



