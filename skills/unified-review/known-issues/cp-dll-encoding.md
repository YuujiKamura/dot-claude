---
paths:
  - "**/control-plane-server/**"
  - "**/ffi.rs"
  - "**/*control_plane*.zig"
---
# Control Plane DLL FFI Known Issue Patterns

## Zig↔Rust FFI境界のUTF-16/UTF-8混淆
- **検出条件:** `read_buffer`, `send_input`, `from_utf16_lossy` がFFI関数内にある
- **問題:** Rust側が `String::from_utf16_lossy()` でデコードするとGhosttyバッファ(UTF-8)が文字化けする。UIAテストのマーカー文字列が不一致になる
- **正しい対処:** CP DLL FFI境界ではZig文字列を常にUTF-8と見なす。`String::from_utf8_lossy()` に統一
- **発見日:** 2026-03-22
- **発生元:** ghostty-win CP DLL vtable修正時のデバッグ
