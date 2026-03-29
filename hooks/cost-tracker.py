#!/usr/bin/env python3
"""Cost Tracker Hook for Claude Code.

Stopイベントで呼ばれ、トークン使用量とコスト概算を
~/.claude/metrics/costs.jsonl に追記する。

settings.json の hooks.Stop に登録して使う。
"""

import json
import os
import sys
from datetime import datetime

MAX_STDIN = 1024 * 1024

def estimate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    """Per-1M-token approximate rates."""
    rates = {
        "haiku": {"in": 0.8, "out": 4.0},
        "sonnet": {"in": 3.0, "out": 15.0},
        "opus": {"in": 15.0, "out": 75.0},
    }
    model_lower = model.lower()
    if "haiku" in model_lower:
        tier = "haiku"
    elif "opus" in model_lower:
        tier = "opus"
    else:
        tier = "sonnet"

    r = rates[tier]
    cost = (input_tokens / 1_000_000) * r["in"] + (output_tokens / 1_000_000) * r["out"]
    return round(cost, 6)


def main():
    raw = sys.stdin.read(MAX_STDIN)

    try:
        data = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        data = {}

    usage = data.get("usage", data.get("token_usage", {}))
    input_tokens = int(usage.get("input_tokens", usage.get("prompt_tokens", 0)))
    output_tokens = int(usage.get("output_tokens", usage.get("completion_tokens", 0)))

    model = str(data.get("model", os.environ.get("CLAUDE_MODEL", "unknown")))
    session_id = os.environ.get("CLAUDE_SESSION_ID", "default")

    metrics_dir = os.path.expanduser("~/.claude/metrics")
    os.makedirs(metrics_dir, exist_ok=True)

    row = {
        "timestamp": datetime.now().isoformat(),
        "session_id": session_id,
        "model": model,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "estimated_cost_usd": estimate_cost(model, input_tokens, output_tokens),
    }

    costs_path = os.path.join(metrics_dir, "costs.jsonl")
    with open(costs_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(row) + "\n")

    # Pass through stdin
    sys.stdout.write(raw)


if __name__ == "__main__":
    main()
