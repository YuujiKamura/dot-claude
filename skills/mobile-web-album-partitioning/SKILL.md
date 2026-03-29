---
name: mobile-web-album-partitioning
description: "Web Development. (Date-Based Partitioning for Large Photo Galleries) Use when user mentions: React, Vue, Next.js, CSS, HTML, frontend, backend, API, REST, GraphQL."
category: web-frontend
---

# Web Development

Patterns: 1

## 1. Date-Based Partitioning for Large Photo Galleries

To prevent mobile browsers (especially LINE) from crashing due to large HTML payloads, split massive photo timelines (e.g., 600+ photos) into date-specific sub-pages linked by a lightweight index.

### Steps

1. Group source photos by date (YYYY-MM-DD)
2. Generate individual HTML files per day with a target size of 2MB to 7MB
3. Create a 'timeline_index.html' containing thumbnails and links to each day-page
4. Include count metadata and a primary thumbnail for each day in the index



