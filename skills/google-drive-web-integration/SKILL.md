---
name: google-drive-web-integration
description: "Google Drive File IDでモバイルpinch-zoom対応。Use when: Drive viewer, File ID, pinch-zoom, DriveFS SQLite, mobile photo"
category: web-frontend
---

# Web Development

Patterns: 1

## 1. Native Drive Viewer for Mobile Pinch-Zoom

Bypass the limitations of custom JS lightboxes on mobile by linking directly to the Google Drive native file viewer, which provides optimized high-resolution rendering and standard pinch-zoom capabilities.

### Steps

1. Retrieve Google Drive File IDs for original high-resolution photos using local metadata or DriveFS SQLite
2. Format links as 'https://drive.google.com/file/d/{FILE_ID}/view'
3. Target the native viewer for full-size viewing while keeping the web app for browsing thumbnails/previews



