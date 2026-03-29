---
name: web-dev
description: "モバイル写真サイトの統合パターン集。Use when: mobile memory, cloud storage File ID, pinch-zoom, SSG, payload optimization"
category: web-frontend
---

# Web Development

Conversations: 1 | Patterns: 5

## 1. Mobile-Memory-Aware HTML Payload Optimization

Mobile in-app browsers (like LINE or social media wrappers) have much stricter memory limits than standalone browsers. Large static HTML files (e.g., >9MB) containing thousands of lines of metadata or heavy DOM structures can cause immediate crashes. Practitioners must optimize the initial payload size specifically for these environments.

### Steps

1. Audit total HTML file size and DOM element count for mobile-specific views
2. Externalize large data objects (like photo metadata) into separate JSON files
3. Implement pagination or lazy-loading for static content that exceeds memory thresholds


## 2. Cloud Storage Asset Resolution for Mobile Web Views

Relative file paths for images (`img/photo.jpg`) frequently fail when web content is accessed via cloud storage mobile apps (like Google Drive) because the app's internal viewer does not resolve relative directories like a standard web server. Reliability requires mapping assets to persistent cloud File IDs.

### Steps

1. Map local filesystem relative paths to unique cloud storage File IDs during build time
2. Inject these IDs into the web application's data layer
3. Construct direct-access URLs using provider-specific API patterns instead of standard relative paths


## 3. Mobile-Native Pinch-Zoom Integration for Web Galleries

Standard responsive modals often default to fixed-size containers (e.g., 800x600) and can inadvertently disable native browser scaling. For image-centric apps, practitioners must ensure that high-resolution assets are accessible and that native touch gestures like pinch-to-zoom are explicitly supported.

### Steps

1. Ensure viewport meta tags allow for user-initiated scaling
2. Provide links or triggers to full-resolution source images rather than CSS-scaled versions
3. Select modal components that do not capture or prevent native touch-zoom events


## 4. Build-Time Cloud Metadata Manifest Generation

To avoid the latency and rate-limiting of querying cloud storage APIs (like Google Drive API) at runtime on mobile devices, practitioners use a pre-calculated mapping file generated during a server-side build step.

### Steps

1. Run discovery scripts (e.g., Python/Node) to identify all local assets intended for cloud hosting
2. Query the cloud API to retrieve persistent IDs and metadata for those assets
3. Output a static JSON manifest (e.g., drive_file_ids.json) to be bundled with the web application


## 5. Dedicated Mobile-Specific Static Site Generation (SSG)

When a single responsive HTML file becomes too complex or heavy for mobile hardware, generating a dedicated 'lite' or mobile-specific version of the page is more effective than CSS media queries. This allows for drastic reduction in DOM complexity and asset weight.

### Steps

1. Identify features or data that are non-essential for the mobile experience
2. Create a dedicated generation script (e.g., gen_timeline_mobile.py) that targets mobile-specific constraints
3. Produce a standalone, lightweight HTML file optimized for mobile memory and bandwidth



