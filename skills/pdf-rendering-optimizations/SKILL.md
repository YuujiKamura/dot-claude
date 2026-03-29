---
name: pdf-rendering-optimizations
description: "CLI & Tooling. (Object Identity Mapping in PDF Image Replacement) Use when user mentions: CLI, script, automation, tool, plugin, extension, config."
category: pdf-document
---

# CLI & Tooling

Patterns: 1

## 1. Object Identity Mapping in PDF Image Replacement

When replacing placeholder images in a generated PDF with high-quality assets, sorting by PDF ObjectId is unreliable as identifiers are assigned by internal counters (fonts, metadata, etc.) rather than visual insertion order. To ensure correct replacement, one must traverse the PDF Page tree and resolve XObject references in their specific appearance order.

### Steps

1. Iterate through the document pages using a sorted page-number map from the PDF structure.
2. Access the 'Resources' and 'XObject' dictionaries for each individual page.
3. Collect ObjectIds by resolving the names referenced in the XObject stream in the sequence they were rendered.



