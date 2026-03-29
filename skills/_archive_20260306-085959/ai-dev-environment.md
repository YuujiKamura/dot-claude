---
name: ai-dev-environment
description: "CLI & Tooling. (Knowledge Synchronization via Junctions) Use when user mentions: CLI, script, automation, tool, plugin, extension, config."
---

# CLI & Tooling

Patterns: 1

## 1. Knowledge Synchronization via Junctions

Maintaining separate skill/prompt directories for different AI agents (Codex, Claude, Gemini) leads to knowledge fragmentation. File-level linking ensures all agents benefit from the same learned patterns instantly.

### Steps

1. Prefer directory junctions over manual copying for agent skills: Syncing `.claude/skills` to `.codex/skills` via `mklink /J` creates a single source of truth. Any 'correction' or 'lesson' taught to one agent is immediately reflected across all AI interfaces without duplication.
2. Standardize YAML frontmatter schemas across shared skill files: Adding mandatory 'name' and 'description' fields to shared SKILL.md files prevents validation errors when switching between more restrictive agent CLI runtimes.

### Examples

```
cmd /c mklink /J "C:\Users\user\.codex\skills\my-skill" "C:\Users\user\.claude\skills\my-skill"
```



