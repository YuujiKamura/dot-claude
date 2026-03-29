---
name: winui3-zig-portability
description: "AI & Machine Learning. (WinAppSDK Path Normalization in Zig) Use when user mentions: LLM, GPT, Claude, Gemini, prompt, model, training, inference, embedding."
categories: [AGENTS.md, AI agents, Claude, DevOps, Gemini, LLM, Rust, agent, ai, automation, classification, claude, context, extraction, gemini, history analysis, llm, machine-learning, metadata-extraction, prompt, prompt engineering, rust, session-analysis, state-management, summaries, summarization, summary]
sources: [session-2026-03-18T09-17-46dafada, session-2026-03-18T06-03-07a18646, session-2026-03-18T09-09-b4883f9e, session-2026-03-18T10-05-b4d50724, session-2026-03-18T14-18-0ec43405, 3e7264ca-8ef5-4b04-9e85-b82c8f015058, session-2026-03-18T09-39-48fb21a6, session-2026-03-18T09-07-37d624e8, session-2026-03-18T09-11-6204afcb, session-2026-03-18T09-16-869cc189, session-2026-03-18T05-53-d105a240, session-2026-03-19T02-25-953cd644, session-2026-03-18T09-12-6728656d, session-2026-03-18T09-14-05dcafdf, session-2026-03-18T06-35-f77aca6a, session-2026-03-18T05-55-7212facd, session-2026-03-18T23-51-99db0c65, session-2026-03-18T09-31-aef34d29, session-2026-03-19T05-56-c2c2a003, session-2026-03-18T10-10-0c837334, session-2026-03-18T14-30-ee07f832, session-2026-03-18T02-04-640c1a94, session-2026-03-18T09-12-a875edb7, session-2026-03-18T09-09-5b2fb838, 5466f2b8-2bef-45e5-8f06-029174f01631, session-2026-03-18T09-20-d1c2c70a, session-2026-03-18T08-46-c3fc39b6, session-2026-03-18T01-40-df21365f, session-2026-03-18T09-15-1d57617c, session-2026-03-18T09-05-9d06f1be, session-2026-03-18T09-16-851692ee, session-2026-03-18T10-18-33555aef, session-2026-03-18T09-30-a70fa17c, session-2026-03-18T09-09-6e8af740, session-2026-03-18T09-03-d142e2ac, session-2026-03-18T08-49-07e985a4, session-2026-03-18T08-46-c036c09c, session-2026-03-18T09-14-212690a5, session-2026-03-18T06-34-f678cece, session-2026-03-18T05-51-97622537, session-2026-03-19T03-10-df63abff, session-2026-03-18T10-04-0f412f3a, session-2026-03-18T10-10-e3fe56f2, session-2026-03-18T09-19-bc89d9f2, session-2026-03-18T05-54-0dcbcf5e, session-2026-03-18T08-48-f15e5c7c, session-2026-03-18T09-15-53c34650, session-2026-03-19T01-59-97861f15, session-2026-03-18T09-15-4b5477f7, session-2026-03-18T09-40-3cf673b9]
---

# AI & Machine Learning

Patterns: 1

## 1. WinAppSDK Path Normalization in Zig

Hardcoded environment paths and SDK versions in build scripts are primary blockers for reproducible WinUI3 builds across different developer machines.

### Steps

1. Avoid hardcoding `C:\Users\<name>` paths in `build.zig`; use the `USERPROFILE` environment variable to locate NuGet packages dynamically.
2. Expose bootstrap DLL locations as command-line overrides (e.g., `--winappsdk-bootstrap-dll`) so developers aren't locked into a specific directory structure.
3. Hardcoded SDK versions (e.g., 1.4.230822000) remain 'Blockers' even after path fixes, as they prevent the project from advancing with the platform.

### Examples

```
const sdk_path = std.process.getEnvVarOwned(allocator, "USERPROFILE") catch ...;
```

```
zig build -- --winappsdk-bootstrap-dll C:\path\to\Microsoft.WindowsAppRuntime.Bootstrap.dll
```


## Source

| Conversation | Excerpt |
|---|---|
| `3e7264ca-8ef5-4b04-9e85-b82c8f015058` | AI and Agents If you're using AI assistance with Ghostty, Ghostty provides an AGENTS.md file read by... |
| `session-2026-03-18T14-30-ee07f832` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T14-18-0ec43405` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T10-18-33555aef` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `session-2026-03-18T10-10-e3fe56f2` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `session-2026-03-18T10-10-0c837334` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T10-05-b4d50724` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T10-04-0f412f3a` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `session-2026-03-18T09-39-48fb21a6` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `session-2026-03-18T09-40-3cf673b9` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T09-30-a70fa17c` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `session-2026-03-18T09-31-aef34d29` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T09-20-d1c2c70a` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `session-2026-03-18T09-19-bc89d9f2` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T09-17-46dafada` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `session-2026-03-18T09-16-869cc189` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T09-16-851692ee` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T09-15-53c34650` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `session-2026-03-18T09-15-1d57617c` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T09-15-4b5477f7` | ﻿Below is a list of Claude Code chat conversations. Classify each conversation into the most appro... |
| `session-2026-03-18T09-14-05dcafdf` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `session-2026-03-18T09-14-212690a5` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T09-12-a875edb7` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `session-2026-03-18T09-12-6728656d` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `session-2026-03-18T09-11-6204afcb` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T09-09-b4883f9e` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T09-09-6e8af740` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T09-09-5b2fb838` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `session-2026-03-18T09-07-37d624e8` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `session-2026-03-18T09-05-9d06f1be` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T09-03-d142e2ac` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `session-2026-03-18T08-49-07e985a4` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `session-2026-03-18T08-48-f15e5c7c` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T08-46-c036c09c` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `session-2026-03-18T08-46-c3fc39b6` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T06-34-f678cece` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T06-35-f77aca6a` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `session-2026-03-18T06-03-07a18646` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T05-55-7212facd` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `session-2026-03-18T05-54-0dcbcf5e` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T05-53-d105a240` | ﻿Below is a list of Claude Code chat conversations. Classify each conversation into the most appro... |
| `session-2026-03-18T05-51-97622537` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T02-04-640c1a94` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T01-40-df21365f` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `session-2026-03-18T23-51-99db0c65` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `session-2026-03-19T01-59-97861f15` | ﻿Below is a list of Claude Code chat conversations. Classify each conversation into the most appro... |
| `session-2026-03-19T02-25-953cd644` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `session-2026-03-19T03-10-df63abff` | ﻿Below are summaries from Claude Code conversations in the "DevOps & Infrastructure" domain.  Each... |
| `session-2026-03-19T05-56-c2c2a003` | ﻿Below are summaries from Claude Code conversations in the "AI & Machine Learning" domain.  Each c... |
| `5466f2b8-2bef-45e5-8f06-029174f01631` | Implement the following plan:  # 司書オブザーバー: LLMベース状態管理  ## Context  age... |


