---
name: agent-frontmatter-interop
description: "AI & Machine Learning. (Polymorphic Frontmatter for Multi-Agent Skill Compatibility) Use when user mentions: LLM, GPT, Claude, Gemini, prompt, model, training, inference, embedding."
---

# AI & Machine Learning

Patterns: 1

## 1. Polymorphic Frontmatter for Multi-Agent Skill Compatibility

Bridges the gap between different AI agents' discovery requirements by creating a superset of YAML metadata within a single markdown file.

### Steps

1. Implicit vs Explicit Discovery Logic: Claude Code often infers skill identity from folder names, whereas Codex/Gemini may strictly require explicit 'name' and 'description' keys in YAML frontmatter. Standardizing on the stricter requirement ensures universal compatibility.
2. Non-Breaking Metadata Augmentation: Parsers typically ignore unknown keys. Adding tool-specific metadata (e.g., Codex-required fields) to existing Claude SKILL.md files allows a single 'Polyglot' skill file to serve multiple agent environments without breaking the original tool.
3. Automated Migration Patching: When porting libraries between agents, bulk-patching missing metadata (Name/Description) is the most efficient way to clear 'Warning' states in CLI startup and ensure all skills are properly indexed.
4. Frontmatter-First Design: Including core metadata in the YAML block, even when not strictly required by the current primary tool, future-proofs the skill for stricter agent discovery protocols.

### Examples

```markdown
---
name: brainstorming
description: Guide for creative feature exploration and design
---
# Brainstorming Skill
...
```



