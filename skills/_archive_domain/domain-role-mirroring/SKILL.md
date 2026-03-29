---
name: domain-role-mirroring
description: "Construction & Civil Engineering. (Sub-Agent Role Mirroring) Use when user mentions: 施工, 書類, サブエージェント, 役割分担, 抽出, 工事, construction, document."
---

# CLI & Tooling

Patterns: 1

## 1. Sub-Agent Role Mirroring

Generic data extraction from complex documents (like construction permits) fails to capture high-density technical facts. Deploying sub-agents that mirror real-world professional roles (Site Manager, Chief Engineer) significantly increases extraction precision.

### Steps

1. Generic extraction density is often ~10%. Mirroring specific organizational roles (e.g., Site Manager vs. Inspector) uncovers domain-specific nuances like 'Western Gas requires witnesses while NTT does not'.
2. Assign 'Site Manager' agents to social/PR timelines (flyer distribution) and 'Chief Engineer' agents to technical specs (Highblown SA, JIS Line) to prevent data flattening.
3. Use specialized agents to resolve chronological conflicts, such as mapping a noise complaint at 23:00 to a regulation start at 22:00 across different document types.

### Examples

```json
{
 "agents": [
 {"role": "Site Manager", "focus": "PR & Incident Timeline"},
 {"role": "Internal Inspector", "focus": "Heavy Machine & Utility Witness"},
 {"role": "Chief Engineer", "focus": "Permit Dates & Materials"}
 ]
}
```



