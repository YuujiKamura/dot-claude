---
name: agent-to-agent-orchestration
description: "Documentation. (Terminal-based Agent Relay Constraints) Use when user mentions: README, docs, documentation, tutorial, guide, comment."
categories: [AGENTS.md, AI Integration, Claude Skill, Ghostty, Guide, User Manual]
sources: [d658da03-ff03-4991-9a92-52bd28ea5663, 3e7264ca-8ef5-4b04-9e85-b82c8f015058]
---

# Documentation

Patterns: 1

## 1. Terminal-based Agent Relay Constraints

Using CLI loops as a bridging protocol for autonomous agent communication and its scaling limits.

### Steps

1. Agents currently rely on terminals for communication because their 'autonomous' capabilities (tool use, file manipulation) are exclusively implemented in CLI versions, not raw APIs.
2. Agent-to-agent communication via PTY (Phase 3) acts as a human-visible IPC, where agents 'talk' by sending keys and capturing pane output.
3. Bidirectional dialogue (e.g., Claude asking Gemini for a second opinion) was found to be a niche requirement that usually collapses into simple serial or 2-way branch patterns.
4. The 'N-body problem' was identified as a hard limit for agent-to-agent chat; scaling beyond 2-3 agents leads to context window exhaustion and state management failure.
5. Terminals were redefined as 'observation windows' for humans to monitor agent-to-agent IPC, which remains necessary even if agents move to direct protocols.


## Source

| Conversation | Excerpt |
|---|---|
| `d658da03-ff03-4991-9a92-52bd28ea5663` | ゴーストティの公式のドキュメントを読み聞かせて |
| `3e7264ca-8ef5-4b04-9e85-b82c8f015058` | AI and Agents If you're using AI assistance with Ghostty, Ghostty provides an AGENTS.md file read by... |


