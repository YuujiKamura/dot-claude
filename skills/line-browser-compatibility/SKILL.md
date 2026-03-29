---
name: line-browser-compatibility
description: "Web Development. (LINE In-App Browser Constraints Management) Use when user mentions: React, Vue, Next.js, CSS, HTML, frontend, backend, API, REST, GraphQL."
category: web-frontend
---

# Web Development

Patterns: 1

## 1. LINE In-App Browser Constraints Management

Specific techniques to handle the technical limitations of the LINE in-app browser, which is more prone to crashing with large DOM/binary assets than standard system browsers.

### Steps

1. Limit the number of base64-encoded images per page to ensure the total HTML payload does not exceed the crash threshold (roughly 8-10MB).
2. Include a redirect script (e.g., `LINE_REDIRECT_JS`) to prompt users to open the gallery in the device's system browser if enhanced capabilities are needed.

### Examples

```
LINEブラウザでは9.2MBのHTML自体がクラッシュ
```

```
LINE redirect JS（既存`LINE_REDIRECT_JS`再利用）
```



