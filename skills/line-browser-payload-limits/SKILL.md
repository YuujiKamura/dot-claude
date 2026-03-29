---
name: line-browser-payload-limits
description: "Web Development. (LINE In-App Browser Payload Optimization) Use when user mentions: React, Vue, Next.js, CSS, HTML, frontend, backend, API, REST, GraphQL."
---

# Web Development

Patterns: 1

## 1. LINE In-App Browser Payload Optimization

The LINE in-app browser has strict memory limits; HTML files exceeding ~9-10MB often crash. Aim for payloads under 7MB by restricting the number of embedded images per page.

### Steps

1. Monitor total HTML file size including Base64-encoded assets
2. Cap the number of photos per single HTML page (typically under 100 entries for 800x600 previews)
3. Use multi-file structure instead of a Single Page Application (SPA) approach for high-density media content



