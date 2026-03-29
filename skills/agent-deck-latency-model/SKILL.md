---
name: agent-deck-latency-model
description: "Agent Orchestration. (Watcher Polling Model, IPC Latency, Status Detection Timing) Use when user mentions: agent-deck, latency, performance, slow, polling, watch interval."
project: agent-deck
---

# agent-deck Latency Model

## Single Detection Path: Watcher Polling

No hooks, no event subscription, no 3-source priority. One path:

```
Watcher (500ms) → CapturePane (TAIL) → hash compare → BufferNotification
```

### Timing
| Operation | Latency |
|-----------|---------|
| TAIL IPC RTT | 8-15ms |
| SHA-256 hash | <1ms |
| Poll interval | 500ms (default, configurable) |
| Stable detection | 3 reads = 1.5s |
| Active→idle transition detection | 1.5-2s |

### Why 500ms default
- 1s: missed fast transitions, false idle possible between polls
- 500ms: catches spinner animation changes, 1.5s stable detection
- 200ms: works but 2x pipe load, diminishing returns
- 10 sessions × 2 polls/sec = 20 TAIL/sec, ~200ms total IPC

## What Was Deleted
- Hook file fast path (0 RT) — gone, polling is primary
- CP event subscription (0 RT) — demoted to optional refinement
- eventStatusMaxAge=5s silent degradation — gone
- 3-source implicit priority in UpdateStatus — gone

## send Workflow Latency
| Phase | Typical |
|-------|---------|
| trust dialog dismiss | 0-2s (if present) |
| waitForReady | 0.5-2s |
| Send (RAW_INPUT) | 5-15ms |
| verifyAccepted | 2-5s (active→idle detection) |
| **Total** | **3-10s** |

Honest numbers. No "millisecond latency" claim.

## Configuring
```
agent-deck watch <session> --interval 200ms  # faster
agent-deck watch <session> --interval 2s     # lighter
agent-deck watch <session> --stable 5        # more conservative
```
