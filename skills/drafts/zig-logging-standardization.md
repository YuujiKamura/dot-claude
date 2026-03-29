---
name: zig-logging-standardization
description: "Documentation. (Audit-Driven Migration to std.log) Use when user mentions: README, docs, documentation, tutorial, guide, comment."
categories: [Markdown, agent, config, instructions, issue, report, skills]
sources: [019cfda9-fc8d-76a2-bcd1-9a7e49ad408c, 019cfd58-8b67-70e0-a39b-fd16c2551eaa, 019cfdf9-fa0a-7492-957d-5f3b53990615, session-2026-03-17T19-52-7fd6f5af]
---

# Documentation

Patterns: 1

## 1. Audit-Driven Migration to std.log

Purging custom logging remnants to ensure consistent telemetry and standard handler integration in Zig-based Windows applications.

### Steps

1. Automated migration to std.log often leaves residual legacy logging calls (e.g., fileLog) in specialized files like App.zig. Insight: Domain-specific glue code often uses logging patterns that generic search-and-replace tools miss, necessitating a manual 'remnant purge' pass focused on entry points.
2. Migration is considered incomplete until the build-system level 'log-to-file' infrastructure is replaced by std.log handlers that can be redirected by the host environment for unified debugging.

### Examples

```zig
// Legacy pattern identified for purging
// fileLog.info("App init", .{}); 

// Correct standardized pattern
std.log.info("App init", .{});
```


## Source

| Conversation | Excerpt |
|---|---|
| `019cfdf9-fa0a-7492-957d-5f3b53990615` | # AGENTS.md instructions for C:\Users\yuuji\ghostty-win  <INSTRUCTIONS> # AGENTS.md  ## Project Scop... |
| `session-2026-03-17T19-52-7fd6f5af` | Issue #113 更新完了: https://github.com/YuujiKamura/ghostty/issues/113    Issue #113 全4項目... |
| `019cfda9-fc8d-76a2-bcd1-9a7e49ad408c` | # AGENTS.md instructions for C:\Users\yuuji  <INSTRUCTIONS> ## Skills A skill is a set of local inst... |
| `019cfd58-8b67-70e0-a39b-fd16c2551eaa` | # AGENTS.md instructions for C:\Users\yuuji  <INSTRUCTIONS> ## Skills A skill is a set of local inst... |


