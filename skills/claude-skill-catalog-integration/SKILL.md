---
name: claude-skill-catalog-integration
description: "スキルカタログ一括インポートとCLAUDE.mdルールの区別。Use when: skill catalog import, 大量スキル読み込み, skills refresh"
category: claude-config
---

# CLI & Tooling

Patterns: 1

## 1. Distinguish rule-file loading from large skill-catalog onboarding

A key correction was that the user wanted importing a large domain-skill corpus (hundreds of files), not `CLAUDE.md` rule behavior. Correct tooling guidance depends on this distinction.

### Steps

1. First classify the request: policy/rules loading vs domain-skill catalog ingestion; they are different systems with different failure modes.
2. For catalog onboarding, path linkage and catalog sync are the decision points; generic rules explanations are a misdiagnosis.
3. Operationally, if catalog refresh is supported in-session, prefer refresh over restart to reduce disruption.

### Examples

```text
C:\\Users\\yuuji\\.claude\\skills
```

```text
/memory refresh
```



