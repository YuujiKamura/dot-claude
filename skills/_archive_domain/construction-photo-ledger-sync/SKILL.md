---
name: construction-photo-ledger-sync
description: "Miscellaneous. (Construction Photo to Ledger Mapping) Use when user mentions: ."
---

# Miscellaneous

Patterns: 1

## 1. Construction Photo to Ledger Mapping

Workflows for integrating AI-tagged construction photos with official inspection documents. This involves domain-specific terminology nuances, such as distinguishing between a simple 'Inspection' (社内検査) and an 'Inspection Status' (社内検査実施状況) for formal reporting, and mapping photo-derived results to Work-as-Built (出来形管理) or Quality Control (品質管理) ledgers.

### Steps

1. Cross-reference photo timestamps with Material Verification (材料確認) and Quality Control folders to populate aggregate tables
2. Update remark fields based on specific reporting requirements (e.g., adding 'status' suffix to inspection items)
3. Filter out materials (e.g., PK-3 or coarse grain) from ledger templates if they are not confirmed by the actual site photos or material logs



