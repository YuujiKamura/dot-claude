---
name: llm-batch-classification-cardinality-guardrails
description: "バッチ分類で入出力件数一致・index忠実性を最優先。Use when: batch classification, cardinality mismatch, fabricated index"
category: llm-patterns
---

# AI & Machine Learning

Patterns: 1

## 1. Cardinality and index fidelity over JSON prettiness

In batch conversation classification, the critical correctness criterion is one-to-one mapping with provided inputs. The failure mode was repeated over-generation (extra indices), even when JSON shape and allowed labels looked correct.

### Steps

1. Judge output validity first by cardinality/index fidelity: output count must equal visible input count, and indices must be exactly the provided set.
2. Reject outputs that are syntactically valid JSON but semantically invalid due to invented records; this is a high-severity hallucination in labeling pipelines.

### Examples

```python
assert len(results) == len(inputs)
assert {r['index'] for r in results} == {i['index'] for i in inputs}
```



