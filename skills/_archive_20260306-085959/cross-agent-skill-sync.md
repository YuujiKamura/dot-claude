---
name: cross-agent-skill-sync
description: "AI & Machine Learning. (Live-Syncing Skills Across AI Agents using NTFS Junctions) Use when user mentions: LLM, GPT, Claude, Gemini, prompt, model, training, inference, embedding."
---

# AI & Machine Learning

Patterns: 1

## 1. Live-Syncing Skills Across AI Agents using NTFS Junctions

Prevents skill divergence and manual update toil when using multiple AI CLI environments (Claude Code, Codex, Gemini) by using directory-level aliases instead of file copies.

### Steps

1. Master-Slave Architecture: Designate one agent's skill directory (e.g., ~/.claude/skills) as the 'Source of Truth' to prevent version fragmentation and conflicting logic updates across different tools.
2. Junction vs Copy Trade-off: Manual copying is error-prone during active development. Junctions provide zero-latency synchronization for file edits across all tools, ensuring that an improvement to a prompt in one agent is immediately available in all others.
3. Discovery Lifecycle Management: Distinguish between 'Content Sync' and 'Discovery Sync'. While file edits sync instantly via junctions, adding a brand new skill still requires a structural registration (creating a new junction), shifting the operational burden from daily updates to one-time setup.
4. Permission-Safe Aliasing on Windows: Prefer NTFS Junctions over Symlinks for agent skill folders to avoid permission friction or absolute path resolution issues often encountered in CLI tools running in different shells (PowerShell vs CMD).

### Examples

```
cmd /c mklink /j "C:\Users\user\.codex\skills\my-skill" "C:\Users\user\.claude\skills\my-skill"
```



