---
name: terminal-architecture-anatomy
description: "Documentation. (Terminal Emulator vs. Process Host Reality) Use when user mentions: README, docs, documentation, tutorial, guide, comment."
categories: [AGENTS.md, AI Integration, Claude Skill, Ghostty, Guide, User Manual]
sources: [d658da03-ff03-4991-9a92-52bd28ea5663, 3e7264ca-8ef5-4b04-9e85-b82c8f015058]
---

# Documentation

Patterns: 1

## 1. Terminal Emulator vs. Process Host Reality

The technical discrepancy between the legacy 'emulator' terminology and the modern role of terminal applications as GPU-accelerated process hosts.

### Steps

1. Modern terminal apps (Ghostty, WT) were found to be primarily GPU renderers, input method hosts, and window managers, where VT100 emulation is a legacy 1% of functionality.
2. The PTY (Pseudo-Terminal) layer in the OS kernel is the only entity that actually performs 'emulation' by deceiving shells into believing they are connected to serial hardware.
3. Ghostty's terminal API priority was identified as 'Xterm compatibility' first, then 'Protocol specifications' to ensure industry-standard behavior.
4. [INTERVENTION] User: 'WTなら、色んな種類のシェルを内部で同時起動できるが、それならシェルをエミュレートしてるというので意味が分からんでもないけど、それだと内挿起動してるだけで、擬似的な意味合いが全く無い' -> AI conceded that terminals are hosts/containers for real shells, not shell emulators.


## Source

| Conversation | Excerpt |
|---|---|
| `d658da03-ff03-4991-9a92-52bd28ea5663` | ゴーストティの公式のドキュメントを読み聞かせて |
| `3e7264ca-8ef5-4b04-9e85-b82c8f015058` | AI and Agents If you're using AI assistance with Ghostty, Ghostty provides an AGENTS.md file read by... |


