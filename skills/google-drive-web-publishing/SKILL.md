---
name: google-drive-web-publishing
description: "Web Development. (DriveFS-Integrated Photo Web Generation) Use when user mentions: React, Vue, Next.js, CSS, HTML, frontend, backend, API, REST, GraphQL."
category: web-frontend
---

# Web Development

Patterns: 1

## 1. DriveFS-Integrated Photo Web Generation

A workflow for generating static photo sites that use Google Drive as a backend, leveraging local File Stream metadata for path resolution and native viewer integration.

### Steps

1. Retrieve Google Drive File IDs from the local DriveFS SQLite database (or `drive_file_ids.json`) to construct permanent direct-access links.
2. Use `https://drive.google.com/file/d/{ID}/view` for original photo links to leverage Google's native mobile-optimized viewer (pinch-zoom, rotation).
3. Verify the existence of high-resolution modal previews in the `photoMeta` JSON structure (e.g., checking for `modalB64` fields) during build-time validation.

### Examples

```
grep -n "var PHOTOS" "/h/マイドライブ/〇市道.../timeline.html" | head -3
```

```
find /h/マイドライブ -maxdepth 3 -name "timeline.html"
```

```
// Check if photoMeta has modalB64 field
var meta = photoMeta[0];
if (meta.modalB64) { ... }
```



