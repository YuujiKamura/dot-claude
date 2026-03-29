---
name: mobile-web-photo-galleries
description: "Web Development. (Mobile Optimization for Large Image Timelines) Use when user mentions: React, Vue, Next.js, CSS, HTML, frontend, backend, API, REST, GraphQL."
---

# Web Development

Patterns: 1

## 1. Mobile Optimization for Large Image Timelines

Strategies for handling high-volume photo galleries (600+ images) in memory-constrained mobile environments like the LINE in-app browser to prevent crashes and ensure high-resolution access.

### Steps

1. Split single large HTML files (e.g., >9MB) into smaller logical units (e.g., daily pages) to stay under a ~7MB threshold for mobile browser stability.
2. Implement an index page (e.g., `timeline_index.html`) containing thumbnails and links to sub-pages to reduce initial memory footprint.
3. Embed 800x600 preview images as base64 strings directly in the HTML to avoid relative path resolution issues common when sharing via cloud storage (Google Drive).
4. Offload full-resolution pinch-zoom functionality to native viewers by linking directly to cloud-native preview URLs instead of building custom JS modals.

### Examples

```
https://drive.google.com/file/d/{ID}/view
```

```
<!-- timeline_day_0212.html -->
<header>
 <h1>2026/02/12</h1>
 <span class="meta">94枚</span>
 <a href="{index_drive_link}">← 一覧に戻る</a>
</header>
```

```
timeline_day_0210.html (92枚、6.7MB)
timeline_day_0212.html (94枚、6.6MB)
```



