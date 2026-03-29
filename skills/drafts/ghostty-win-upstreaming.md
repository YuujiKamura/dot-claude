---
name: ghostty-win-upstreaming
description: "Documentation. (Upstreaming Blockers for Native Windows Ports) Use when user mentions: README, docs, documentation, tutorial, guide, comment."
categories: [AGENTS.md, AI Integration, Claude Skill, Ghostty, Guide, User Manual]
sources: [d658da03-ff03-4991-9a92-52bd28ea5663, 3e7264ca-8ef5-4b04-9e85-b82c8f015058]
---

# Documentation

Patterns: 1

## 1. Upstreaming Blockers for Native Windows Ports

Technical constraints preventing the merge of a major Windows fork back to a core-centric repository.

### Steps

1. Rust-based DLLs (like the Control Plane) are a hard blocker for upstreaming because they require a second toolchain (cargo); upstream mandates a single `zig build` entry point.
2. NuGet package path resolution in `build.zig` was found to be only partially dynamic, still failing due to hardcoded version strings (`1.4.230822000`) and target architectures (`win10-x64`).
3. `debug_harness` was found deeply integrated into `App.zig` (40+ locations), using environment variables to toggle TabView logic, which must be abstracted before PR.
4. `OutputDebugStringA` was identified as dead code in `os.zig`, being declared but never called.
5. [INTERVENTION] User: 'デメリットはないかな。DLLだろうが、Zigコードだろうが、コンパイルをどっちでやるかだけで大して変わらんか、も、' -> AI clarified the tradeoffs: Rust DLLs provide fault isolation and a mature async ecosystem, whereas Zig rewrites only serve to satisfy upstream build requirements.

### Examples

```zig
// build.zig snippet identified as a blocker
const default_bootstrap_path = std.fs.path.join(b.allocator, &.{ 
 default_user_profile, ".nuget", "packages", "microsoft.windowsappsdk", 
 "1.4.230822000", // Hardcoded version
 "runtimes", "win10-x64", "native", "..."
});
```


## Source

| Conversation | Excerpt |
|---|---|
| `d658da03-ff03-4991-9a92-52bd28ea5663` | ゴーストティの公式のドキュメントを読み聞かせて |
| `3e7264ca-8ef5-4b04-9e85-b82c8f015058` | AI and Agents If you're using AI assistance with Ghostty, Ghostty provides an AGENTS.md file read by... |


