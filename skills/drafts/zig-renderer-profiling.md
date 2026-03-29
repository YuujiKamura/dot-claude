---
name: zig-renderer-profiling
description: "Miscellaneous. (Windowed Frame-Time Statistical Profiling) Use when user mentions: ."
categories: [D3D11, WinUI3, Zig, classification, meta-task, renderer, systems programming]
sources: [session-2026-03-19T07-36-2047e521, 4f0bf9e1-1658-4ef3-bdfe-0c1389b9564b]
---

# Miscellaneous

Patterns: 1

## 1. Windowed Frame-Time Statistical Profiling

Implementing non-intrusive performance monitoring in graphics renderers using statistical windowing to identify jitter.

### Steps

1. Raw frame-to-frame logging creates excessive I/O overhead and noise. Aggregating stats over a 120-frame window (approx. 2 seconds at 60fps) provides a representative sample of avg/min/max latency without performance degradation.
2. Using std.time.nanoTimestamp() is necessary for sub-millisecond precision required to detect micro-stutter in terminal rendering that millisecond-level timers might miss.
3. Tracking the 'max' frame time is more critical for UX than 'avg', as it identifies frame drops and jitter that disrupt the visual experience even if the average FPS remains high.

### Examples

```zig
const delta = std.time.nanoTimestamp() - last_frame_ns;
self.frame_times_sum_ns += delta;
self.frame_time_max_ns = @max(self.frame_time_max_ns, delta);
if (self.frame_count % 120 == 0) {
 log.info("frame-profile: avg={d:.2}ms max={d:.2}ms", .{avg_ms, max_ms});
}
```


## Source

| Conversation | Excerpt |
|---|---|
| `4f0bf9e1-1658-4ef3-bdfe-0c1389b9564b` | https://github.com/YuujiKamura/ghostty/issues/116 これにとりくんで |
| `session-2026-03-19T07-36-2047e521` | ﻿Below is a list of Claude Code chat conversations. Classify each conversation into the most appro... |


