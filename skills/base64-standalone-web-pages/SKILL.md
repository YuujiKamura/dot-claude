---
name: base64-standalone-web-pages
description: "Base64画像埋め込みでGoogle Drive等のパス制限を回避。Use when: base64 embed, photoMeta, 800x600 preview, Drive hosted HTML"
category: web-frontend
---

# Web Development

Patterns: 1

## 1. Base64 Embedding for Path-Independent Portability

Ensure media displays correctly when hosted on restricted environments like Google Drive (where relative paths often break) by embedding medium-resolution previews directly as Base64 strings.

### Steps

1. Resize preview images to a mobile-friendly resolution (e.g., 800x600)
2. Convert these previews to Base64 strings and store them in a 'photoMeta' JSON object within the HTML
3. Update the 'openModal' or rendering logic to pull from the embedded string rather than an external URL



