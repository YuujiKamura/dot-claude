---
name: sequential-ui-bootstrapping
description: "UIスモークテストのP0→P1→P2順序制約。Use when: smoke test bootstrap, debug harness, app ready-to-test, environment race condition, WinUI3 test order"
project: ghostty-win
---

# Testing & QA

Patterns: 1

## 1. Sequential Bootstrapping for UI Smoke Tests

Smoke tests for complex UI apps must follow a strict sequential logic: Infrastructure (P0) -> Harness Control (P1) -> Runner (P1) -> Test Cases (P2). Jumping to test cases too early results in brittle tests that fail due to environment instability.

### Steps

1. Develop a debug harness as a P0/P1 bridge to provide a stable API for inspecting internal app state (Surface/App) before the smoke test runner is even conceived.
2. Validate environment readiness via a dedicated smoke test runner as a distinct gate after infrastructure is complete but before writing specific feature tests (like tab/resize).
3. Treat 'test control' as a sequential prerequisite to ensure the harness can reliably transition the app from startup to a 'ready-to-test' state without race conditions.



