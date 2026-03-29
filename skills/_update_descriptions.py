import os

skills_dir = r"C:\Users\yuuji\.claude\skills"

replacements = {
    "dxf-cad": (
        'description: "DXF/CAD\u3002(DXF\u30d5\u30a1\u30a4\u30eb\u69cb\u9020\u306e\u5b8c\u5168\u5316\u3068CAD\u4e92\u63db\u6027\u4fee\u6b63\u3001ezdxf\u30e9\u30a4\u30d6\u30e9\u30ea\u306b\u3088\u308b\u81ea\u52d5\u76e3\u67fb(audit)\u30ef\u30fc\u30af\u30d5\u30ed\u30fc\u3001\u63cf\u753b\u4e2d\u9593\u8868\u73fe(Drawing IR)\u306b\u3088\u308b\u8868\u793a\u30fb\u51fa\u529b\u306e\u540c\u671f\u3001\u80a5\u5927\u5316\u3057\u305f\u30ec\u30a4\u30a2\u30a6\u30c8\u8a08\u7b97\u30ed\u30b8\u30c3\u30af\u306e\u30e2\u30b8\u30e5\u30fc\u30eb\u5206\u5272\u3001\u30c9\u30e1\u30a4\u30f3\u30e2\u30c7\u30eb\u6e96\u62e0\u306eCSV\u2192DXF\u5909\u63dbCLI\u69cb\u7bc9) DXF\u3001CAD\u3001\u6a2a\u65ad\u56f3\u3001\u56f3\u9762\u3068\u8a00\u308f\u308c\u305f\u6642\u306b\u4f7f\u7528\u3002"',
        'description: "DXF\u751f\u6210\u3068CAD\u4e92\u63db\u6027: ezdxf audit, Drawing IR, CSV\u2192DXF CLI\u3002Use when: HEADER/ENTITIES\u69cb\u9020, ezdxf recover, egui preview, SectionStyle, \u6a2a\u65ad\u56f3\u30ec\u30a4\u30a2\u30a6\u30c8"'
    ),
    "folder-watcher": (
        'description: "folder-watcher: \u30d5\u30a9\u30eb\u30c0\u76e3\u8996\u3001\u30c7\u30a3\u30ec\u30af\u30c8\u30ea\u76e3\u8996\u3001\u30d5\u30a1\u30a4\u30eb\u691c\u77e5\u3001notify\u3001watcher\u3001PDF\u76e3\u8996\u3001\u30d3\u30eb\u30c9\u76e3\u8996\u3001\u30db\u30c3\u30c8\u30ea\u30ed\u30fc\u30c9"',
        'description: "Rust FolderWatcher crate: notify-based file event builder. Use when: FolderWatcher::new, with_filter, on_create/modify/delete, WatcherBuilder"'
    ),
    "llm-visual-pairing-testing": (
        'description: "Testing & QA. (Contact Sheet Visual Matching Strategy) Use when user mentions: test, unit test, integration, coverage, mock, assertion, TDD, fixture."',
        'description: "Contact sheet grid matching for before/after photo pairing. Use when: numbered grid, VLM pairing, vanishing point, one-to-many query, attention dispersion"'
    ),
    "module-extraction": (
        'description: \u5de8\u5927Rust\u30d5\u30a1\u30a4\u30eb\u304b\u3089\u30e2\u30b8\u30e5\u30fc\u30eb\u3092\u5206\u96e2\u3059\u308b\u969b\u306e\u30b3\u30f3\u30c6\u30ad\u30b9\u30c8\u7bc0\u7d04\u624b\u6cd5\u3002(1) Read\u30c4\u30fc\u30eb\u306elimit\u5236\u9650\u3001(2) grep\u6d3b\u7528\u3067\u69cb\u9020\u628a\u63e1\u3001(3) \u6bb5\u968e\u7684\u5206\u5272\u624b\u9806\u3002lib.rs\u5206\u5272\u3001\u30e2\u30b8\u30e5\u30fc\u30eb\u5206\u96e2\u3001\u30ea\u30d5\u30a1\u30af\u30bf\u30ea\u30f3\u30b0\u30015000\u884c\u3001\u80a5\u5927\u5316\u3001\u30b3\u30f3\u30c6\u30ad\u30b9\u30c8\u30aa\u30fc\u30d0\u30fc\u3068\u8a00\u308f\u308c\u305f\u6642\u306b\u4f7f\u7528\u3002',
        'description: "5000\u884c\u8d85lib.rs\u306e\u30e2\u30b8\u30e5\u30fc\u30eb\u5206\u96e2\u624b\u6cd5: Read limit=200, grep\u69cb\u9020\u628a\u63e1\u3002Use when: lib.rs\u5206\u5272, \u5de8\u5927\u30d5\u30a1\u30a4\u30eb, \u30b3\u30f3\u30c6\u30ad\u30b9\u30c8\u30aa\u30fc\u30d0\u30fc, cargo check, mod\u5206\u96e2"'
    ),
    "pdf-analysis-embed": (
        'description: "PDF\u306b\u89e3\u6790\u7d50\u679c\u3092\u57cb\u3081\u8fbc\u3080Rust\u30e9\u30a4\u30d6\u30e9\u30ea\u3002(1) AI\u306e\u89e3\u6790\u7d50\u679c\u3092PDF\u306b\u57cb\u3081\u8fbc\u3093\u3067\u4e00\u4f53\u5316\u3001(2) \u57cb\u3081\u8fbc\u307f\u6e08\u307f\u306a\u3089\u518d\u89e3\u6790\u30b9\u30ad\u30c3\u30d7\u3067\u30b3\u30b9\u30c8\u524a\u6e1b\u3002pdf-analysis-embed\u3001PDF\u57cb\u3081\u8fbc\u307f\u3001\u89e3\u6790\u7d50\u679c\u57cb\u3081\u8fbc\u307f\u3001\u518d\u89e3\u6790\u4e0d\u8981\u3001PDF\u30e1\u30bf\u30c7\u30fc\u30bf\u3068\u8a00\u308f\u308c\u305f\u6642\u306b\u4f7f\u7528\u3002"',
        'description: "lopdf+base64\u3067AI\u89e3\u6790\u7d50\u679c\u3092PDF\u306b\u57cb\u3081\u8fbc\u3080Rust crate\u3002Use when: AnalysisResult, with_analyzer, pdf-analysis-embed, \u518d\u89e3\u6790\u30b9\u30ad\u30c3\u30d7, PDF metadata"'
    ),
    "pdf-check": (
        'description: PDF\u66f8\u985e\u306e\u6574\u5408\u6027\u30c1\u30a7\u30c3\u30af\u3002\u53f3\u30af\u30ea\u30c3\u30af\u30e1\u30cb\u30e5\u30fc\u304b\u3089PDF\u3092\u89e3\u6790\u3059\u308b\u6642\u306b\u4f7f\u7528\u3002\u5951\u7d04\u66f8\u3001\u4ea4\u901a\u8a98\u5c0e\u54e1\u914d\u7f6e\u5b9f\u7e3e\u3001\u6e2c\u91cf\u56f3\u9762\u306a\u3069\u306e\u6574\u5408\u6027\u3092\u691c\u8a3c\u3059\u308b\u3002pdf\u3001PDF\u3001\u66f8\u985e\u30c1\u30a7\u30c3\u30af\u3001\u6574\u5408\u6027\u3001\u5951\u7d04\u66f8\u3001\u914d\u7f6e\u5b9f\u7e3e\u3001\u6e2c\u91cf\u3068\u8a00\u308f\u308c\u305f\u6642\u306b\u4f7f\u7528\u3002',
        'description: ".guidelines.json\u30d9\u30fc\u30b9\u306ePDF\u6574\u5408\u6027\u30c1\u30a7\u30c3\u30af\u3002Use when: \u5951\u7d04\u66f8, \u4ea4\u901a\u8a98\u5c0e\u54e1\u914d\u7f6e\u5b9f\u7e3e, \u6e29\u5ea6\u7ba1\u7406, \u5199\u771f\u5e16, ShoruiChecker --headless, \u66f8\u985e\u30bf\u30a4\u30d7\u5224\u5b9a"'
    ),
    "pdf-verification": (
        'description: Codex CLI\u3092\u4f7f\u7528\u3057\u3066PDF\u51fa\u529b\u7d50\u679c\u3092\u691c\u8a3c\u3059\u308b\u3002\u4f7f\u7528\u5834\u9762: (1) PDF\u751f\u6210\u5f8c\u306e\u78ba\u8a8d\u3001(2) \u30ec\u30a4\u30a2\u30a6\u30c8\u691c\u8a3c\u3001(3) \u5199\u771f\u914d\u7f6e\u78ba\u8a8d\u3001(4) \u30d5\u30a9\u30f3\u30c8\u8868\u793a\u78ba\u8a8d\u3001(5) \u67a0\u7dda\u30fb\u4f59\u767d\u78ba\u8a8d\u3002\u30c8\u30ea\u30ac\u30fc: "PDF\u78ba\u8a8d", "PDF\u691c\u8a3c", "\u51fa\u529b\u78ba\u8a8d", "\u30ec\u30a4\u30a2\u30a6\u30c8\u78ba\u8a8d"',
        'description: "Codex CLI\u3067PDF\u51fa\u529b\u3092\u81ea\u52d5\u691c\u8a3c: A4/\u5199\u771f\u67a0/\u660e\u671d\u4f53/\u4f59\u767d\u3002Use when: PDF\u751f\u6210\u5f8c\u78ba\u8a8d, cargo run export, photo-ai-rust, \u30ec\u30a4\u30a2\u30a6\u30c8\u691c\u8a3c, codex exec"'
    ),
    "road-drawing": (
        'description: "road-drawing CLI\u3068crate\u306e\u4f7f\u3044\u65b9\u3002CSV/Excel\u2192DXF\u56f3\u9762\u751f\u6210\u3002\u8def\u7dda\u5c55\u958b\u56f3\u3001\u4e09\u89d2\u5f62\u30ea\u30b9\u30c8\u3001\u6a2a\u65ad\u6b69\u9053\u3002road-drawing\u3001DXF\u3001\u5c55\u958b\u56f3\u3001\u4e09\u89d2\u5f62\u3001\u6a2a\u65ad\u6b69\u9053\u3001\u56f3\u9762\u3068\u8a00\u308f\u308c\u305f\u6642\u306b\u4f7f\u7528\u3002"',
        'description: "road-drawing CLI: CSV/Excel to DXF\u56f3\u9762 (road-section/triangle/marking)\u3002Use when: dxf-engine, excel-parser, triangle-core, --list-sections, \u9762\u7a4d\u8a08\u7b97\u66f8"'
    ),
    "rust-dev": (
        'description: "Rust\u958b\u767a\u3002(\u518d\u5e30\u7684AI\u30b3\u30fc\u30c9\u691c\u8a3c (Self-Verification Loop)\u3001\u30de\u30eb\u30c1\u30a8\u30fc\u30b8\u30a7\u30f3\u30c8\u4e26\u5217\u30bf\u30b9\u30af\u5206\u5272 (Team-based Execution)\u3001CLI\u30a4\u30f3\u30bf\u30fc\u30d5\u30a7\u30fc\u30b9\u5148\u884c\u8abf\u67fb\u3068\u7d71\u5408 (CLI Discovery & Integration)\u3001Python\u30d7\u30ed\u30c8\u30bf\u30a4\u30d7\u304b\u3089\u306eRust\u79fb\u690d (Script-to-Crate Migration)\u3001\u30d3\u30eb\u30c9\u30fb\u30c1\u30a7\u30c3\u30af\u4e3b\u5c0e\u306e\u53cd\u5fa9\u4fee\u6b63 (Build-Driven Refinement)) Rust\u3001\u30af\u30ec\u30fc\u30c8\u3001cargo\u3001\u30d3\u30eb\u30c9\u3001WASM\u3001derive\u3068\u8a00\u308f\u308c\u305f\u6642\u306b\u4f7f\u7528\u3002"',
        'description: "photo-ai Rust\u958b\u767a\u30d1\u30bf\u30fc\u30f3: sub-LLM\u691c\u8a3c, \u30de\u30eb\u30c1\u30a8\u30fc\u30b8\u30a7\u30f3\u30c8\u4e26\u5217, Clap CLI\u8a2d\u8a08, Python\u2192Rust\u79fb\u690d\u3002Use when: cargo check loop, Clap derive, crate\u5206\u5272, photo-ai-rust"'
    ),
    "shorui-checker": (
        'description: "ShoruiChecker\u30d7\u30ed\u30b8\u30a7\u30af\u30c8\u306e\u958b\u767a\u652f\u63f4\u3002(1) PDF\u6574\u5408\u6027\u30c1\u30a7\u30c3\u30af\u6a5f\u80fd\u306e\u958b\u767a\u30fb\u4fee\u6b63\u3001(2) Tauri/Rust \u30d0\u30c3\u30af\u30a8\u30f3\u30c9\u958b\u767a\u3001(3) \u30d5\u30ed\u30f3\u30c8\u30a8\u30f3\u30c9UI\u958b\u767a\u3002ShoruiChecker\u3001\u66f8\u985e\u30c1\u30a7\u30c3\u30ab\u30fc\u3001PDF\u89e3\u6790\u3001\u6574\u5408\u6027\u30c1\u30a7\u30c3\u30af\u3068\u8a00\u308f\u308c\u305f\u6642\u306b\u4f7f\u7528\u3002"',
        'description: "ShoruiChecker: Tauri 2.x + Gemini PDF\u6574\u5408\u6027\u30c1\u30a7\u30c3\u30ab\u30fc\u3002Use when: lopdf, notify\u76e3\u8996, PDF D&D\u89e3\u6790, \u7167\u5408\u89e3\u6790, \u30b7\u30b9\u30c6\u30e0\u30c8\u30ec\u30a4, \u30b3\u30fc\u30c9\u30ec\u30d3\u30e5\u30fc\u6a5f\u80fd"'
    ),
    "text-orientation-coordinate-systems": (
        'description: \u30c6\u30ad\u30b9\u30c8\u63cf\u753b\u306b\u304a\u3051\u308b\u5ea7\u6a19\u7cfb\u306e\u9055\u3044\u3068\u5411\u304d\u306e\u88dc\u6b63\u3002DXF(Y\u4e0a\u5411\u304d)\u3068\u30b9\u30af\u30ea\u30fc\u30f3(Y\u4e0b\u5411\u304d)\u9593\u3067\u306e\u56de\u8ee2\u89d2\u5ea6\u306e\u6271\u3044\u3002BBOX-based text rendering\u5b9f\u88c5\u6642\u306b\u4f7f\u7528\u3002',
        'description: "DXF(Y\u4e0a)\u3068\u30b9\u30af\u30ea\u30fc\u30f3(Y\u4e0b)\u306e\u56de\u8ee2\u89d2\u5ea6\u7b26\u53f7\u53cd\u8ee2\u30eb\u30fc\u30eb\u3002Use when: screen_rotation = -dxf_rotation, BBOX text rendering, \u7e26\u66f8\u304d\u8def\u7dda\u65ad\u9762\u56f3"'
    ),
    "usage-aware-delegation": (
        'description: Claude Code\u6b8b\u91cf\u306b\u5fdc\u3058\u305f\u5916\u6ce8\u5224\u65ad\u3002(1) \u6b8b\u91cf\u30c1\u30a7\u30c3\u30af\u3068\u884c\u52d5\u30ec\u30d9\u30eb\u5224\u5b9a\u3001(2) Codex MCP\u5916\u6ce8\u3001(3) WT Control Plane\u7d4c\u7531\u3067Gemini/Codex/\u5225Claude\u306b\u5916\u6ce8\u3001(4) \u4ed5\u4e8b\u91cf\u3068\u6b8b\u91cf\u306e\u30d0\u30e9\u30f3\u30b9\u3067\u81ea\u52d5\u5224\u65ad\u3002usage\u3001\u6b8b\u91cf\u3001\u5229\u7528\u6599\u3001\u5916\u6ce8\u3001\u30b3\u30b9\u30c8\u3001\u7bc0\u7d04\u3001Codex\u59d4\u8b72\u3001\u30c1\u30fc\u30e0\u3001\u4e26\u5217\u3068\u8a00\u308f\u308c\u305f\u6642\u306b\u4f7f\u7528\u3002',
        'description: "Claude\u6b8b\u91cf\u30ec\u30d9\u30eb\u5225\u306e\u5916\u6ce8\u5224\u65ad: Codex MCP\u76f4\u63a5 or WT CP\u7d4c\u7531Gemini/Codex\u3002Use when: /usage, compact\u767a\u751f, 10+\u30d5\u30a1\u30a4\u30eb\u5909\u66f4, \u6b8b\u91cf\u5c11\u306a\u3044, \u30c1\u30fc\u30e0\u59d4\u8b72"'
    ),
    "win-zig-bindgen": (
        'description: "win-zig-bindgen (WinMD\u2192Zig COM binding\u30b8\u30a7\u30cd\u30ec\u30fc\u30bf) \u306e\u8a2d\u8a08\u77e5\u898b\u3002(1) \u7d71\u5408\u30de\u30c3\u30d7\u306b\u3088\u308b\u578b\u89e3\u6c7a\u3001(2) vtable\u5f62\u72b6\u691c\u8a3c\u3001(3) \u672c\u5bb6windows-rs\u30d1\u30ea\u30c6\u30a3\u3001(4) \u30c6\u30b9\u30c8\u8a2d\u8a08\u3002win-zig-bindgen\u3001\u30b8\u30a7\u30cd\u30ec\u30fc\u30bf\u3001WinMD\u3001bindgen\u3001\u30b3\u30fc\u30c9\u751f\u6210\u3001\u578b\u89e3\u6c7a\u3001\u30d1\u30ea\u30c6\u30a3\u3068\u8a00\u308f\u308c\u305f\u6642\u306b\u4f7f\u7528\u3002"',
        'description: "WinMD\u2192Zig COM vtable generator: unified TypeMap, windows-rs parity. Use when: unified_index.zig, emit.zig, sig_decode.zig, vtable shape validation"'
    ),
    "windows-rs-first": (
        'category: cli-tooling',
        'description: "win-zig-bindgen\u306e\u5b9f\u88c5\u524d\u306bwindows-rs\u672c\u5bb6\u3092\u5fc5\u305a\u78ba\u8a8d\u3059\u308b\u30eb\u30fc\u30eb\u3002Use when: crates/libs/bindgen/, types.rs, winmd/index.rs, emit\u5dee\u7570\u691c\u8a3c"'
    ),
    "zig-winrt-com-binding-refactoring": (
        'description: "Zig COM/WinRT\u30d0\u30a4\u30f3\u30c7\u30a3\u30f3\u30b0\u306e\u30b7\u30f3\u30dc\u30eb\u524a\u9664\u30fb\u30ea\u30d5\u30a1\u30af\u30bf\u30ea\u30f3\u30b0\u6642\u306e\u5f71\u97ff\u5206\u6790\u3002(1) pub const\u518d\u30a8\u30af\u30b9\u30dd\u30fc\u30c8\u306e\u524a\u9664\u306f\u30b0\u30ed\u30fc\u30d0\u30eb\u7834\u58ca\u30ea\u30b9\u30af\u3001(2) Zig\u306elazy evaluation\u304c\u30d3\u30eb\u30c9\u30a8\u30e9\u30fc\u3092\u96a0\u3059\u3001(3) critical-only\u30ec\u30d3\u30e5\u30fc\u6226\u7565\u3002Zig\u3001COM\u3001WinRT\u3001binding\u3001refactoring\u3001ABI\u3001symbol\u3001vtable\u3068\u8a00\u308f\u308c\u305f\u6642\u306b\u4f7f\u7528\u3002"',
        'description: "pub const\u518d\u30a8\u30af\u30b9\u30dd\u30fc\u30c8\u524a\u9664\u306e\u30b0\u30ed\u30fc\u30d0\u30eb\u7834\u58ca\u30ea\u30b9\u30af\u3068Zig lazy evaluation\u7f60\u3002Use when: com.zig bridge, undeclared identifier, symbol grep, critical-only diff review"'
    ),
    "agent-deck-latency-model": (
        'description: "Agent Orchestration. (Watcher Polling Model, IPC Latency, Status Detection Timing) Use when user mentions: agent-deck, latency, performance, slow, polling, watch interval."',
        'description: "agent-deck Watcher 500ms polling + TAIL IPC + SHA-256 hash stable detection. Use when: poll interval tuning, 1.5s stable detection, active-idle transition, pipe load"'
    ),
    "agent-skill-ux-naming": (
        'description: "AI & Machine Learning. (Intent-Based Naming for Boundary Crossings) Use when user mentions: LLM, GPT, Claude, Gemini, prompt, model, training, inference, embedding."',
        'description: "Skill naming: use relay/bridge over worker for AI-to-terminal handoffs. Use when: skill naming, agent-deck skill, wt-ai-worker rename, boundary crossing intent"'
    ),
    "semantic-bridge-naming": (
        'description: "AI & Machine Learning. (Semantic Bridge Naming for AI Tooling) Use when user mentions: LLM, GPT, Claude, Gemini, prompt, model, training, inference, embedding."',
        'description: "Name skills by bridge+actor, match repo names, avoid abstract routing layers. Use when: skill discovery friction, windows-terminal-agent-relay, naming convention"'
    ),
}

for skill_name, (old, new) in replacements.items():
    path = os.path.join(skills_dir, skill_name, "SKILL.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if old in content:
        content = content.replace(old, new, 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"OK: {skill_name}")
    else:
        print(f"SKIP (not found): {skill_name}")
