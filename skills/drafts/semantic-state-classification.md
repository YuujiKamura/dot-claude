---
name: semantic-state-classification
description: "AI & Machine Learning. (LLM-based Semantic Status Classification) Use when user mentions: LLM, GPT, Claude, Gemini, prompt, model, training, inference, embedding."
categories: [Agent, Claude, LLM, State Management]
sources: [5466f2b8-2bef-45e5-8f06-029174f01631]
---

# AI & Machine Learning

Patterns: 1

## 1. LLM-based Semantic Status Classification

Replacing rigid keyword matching with LLM semantic classification for terminal-based agent states.

### Steps

1. [INTERVENTION] User: 'それもなんか変だと思う' (That also seems strange) -> Stopped the initial plan to have the LLM maintain and 'correct' mechanical patterns, identifying that anchoring LLM judgment to existing pattern results defeats the purpose of autonomous observation.
2. [INTERVENTION] User: 'LLM判定をパターンと比較するとか機械的に出来るわけがない' (It's impossible to mechanically compare LLM judgments with patterns) -> Reached consensus that string-level comparison between semantic LLM output and literal keyword matches is fundamentally mismatched.
3. [INTERVENTION] User: 'めんどいんでシンプルにLLM判定だけにしたら？' (It's a hassle, why not just use LLM judgment alone?) -> Simplified the architecture by removing pattern-file maintenance and comparison logic, relying entirely on LLM classification from raw buffer context.
4. [INTERVENTION] User: 'キーワード対応で機械判定しないようにする' (Avoid mechanical judgment by keywords) -> Redefined the 'pattern dictionary' as a set of semantic visual descriptions for states rather than substring or regex search terms for the LLM to reference.
5. Gemini Flash (cli-ai-analyzer) was used as the classifier to keep polling costs and latency negligible at a 5-second interval during wait loops.

### Examples

```rust
// The 'patterns' are now just descriptions for the LLM prompt
let prompt = format!(
 "Buffer end:\n{tail_content}\n\n\
 Refer to these state descriptions and classify the current terminal state:\n\
 {patterns_json}\n\
 Return JSON: {\"state\": \"IDLE|WORKING|APPROVAL|READY|STARTING|DONE\"}"
);
```


## Source

| Conversation | Excerpt |
|---|---|
| `5466f2b8-2bef-45e5-8f06-029174f01631` | Implement the following plan:  # 司書オブザーバー: LLMベース状態管理  ## Context  age... |


