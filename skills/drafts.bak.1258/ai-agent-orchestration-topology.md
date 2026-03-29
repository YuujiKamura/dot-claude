---
name: ai-agent-orchestration-topology
description: "Documentation. (Hub-and-Spoke Agent Scaling) Use when user mentions: README, docs, documentation, tutorial, guide, comment."
categories: [AGENTS.md, Ghostty, code-explanation, configuration, documentation, ghostty-win, project-scope, terminal, winui3, zig]
sources: [019d0487-f3a6-7991-ada0-a0f220ee43c2, d658da03-ff03-4991-9a92-52bd28ea5663, 019d0459-74ac-75d1-8b91-d0ab99812e42, 019d0444-29fb-7523-9bc0-9433013476e5, 019d044e-a335-7271-9c12-67df66b02ece, 019d043b-dc26-7db2-911a-f41764a0f67e, session-2026-03-19T07-39-db08116b]
---

# Documentation

Patterns: 1

## 1. Hub-and-Spoke Agent Scaling

Direct Peer-to-Peer (P2P) agent communication suffers from an 'N-body problem' where context windows degrade as agent counts increase. A Hub-and-Spoke model using tmux and git worktrees provides the persistence and file isolation necessary for multi-agent workflows.

### Steps

1. Limit P2P agent communication to 2 agents (e.g., 'second opinion' pattern); beyond this, the architecture must pivot to a central hub to manage state.
2. Utilize 'git worktree' to isolate file-editing agents, preventing race conditions and ensuring that one agent's workspace doesn't pollute the context of another.
3. Identify the 'unique value proposition' (e.g., Windows Terminal Control Plane integration) of the orchestration tool rather than over-engineering general-purpose communication protocols.
4. Leverage tmux for persistent background sessions, allowing agents to survive terminal disconnects and maintain long-running diagnostic processes.

### Examples

```
git worktree add ../agent-feature-branch feature-branch
```

```
tmux new-session -d -s agent-relay-worker
```


## Source

| Conversation | Excerpt |
|---|---|
| `d658da03-ff03-4991-9a92-52bd28ea5663` | ゴーストティの公式のドキュメントを読み聞かせて |
| `019d0487-f3a6-7991-ada0-a0f220ee43c2` | # AGENTS.md instructions for C:\Users\yuuji\ghostty-win  <INSTRUCTIONS> # AGENTS.md  ## Project Scop... |
| `019d0459-74ac-75d1-8b91-d0ab99812e42` | # AGENTS.md instructions for C:\Users\yuuji\ghostty-win  <INSTRUCTIONS> # AGENTS.md  ## Project Scop... |
| `019d044e-a335-7271-9c12-67df66b02ece` | # AGENTS.md instructions for C:\Users\yuuji\ghostty-win  <INSTRUCTIONS> # AGENTS.md  ## Project Scop... |
| `019d0444-29fb-7523-9bc0-9433013476e5` | # AGENTS.md instructions for C:\Users\yuuji\ghostty-win  <INSTRUCTIONS> # AGENTS.md  ## Project Scop... |
| `019d043b-dc26-7db2-911a-f41764a0f67e` | # AGENTS.md instructions for C:\Users\yuuji\ghostty-win  <INSTRUCTIONS> # AGENTS.md  ## Project Scop... |
| `session-2026-03-19T07-39-db08116b` | C:\Users\yuuji\ghostty-win\src\apprt\winui3\App.zig を読んで、initXaml関数の処理ステッ... |


