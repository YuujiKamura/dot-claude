---
name: zig-com-interop
description: "CLI & Tooling. (VTable Slot Alignment and Padding) Use when user mentions: CLI, script, automation, tool, plugin, extension, config."
---

# CLI & Tooling

Patterns: 1

## 1. VTable Slot Alignment and Padding

Precise VTable slot mapping is critical when manually implementing WinRT/COM interfaces in Zig; minor version shifts in headers can cause silent segfaults due to method displacement.

### Steps

1. Explicit placeholder padding is mandatory for binary compatibility: When methods shift indices (e.g., moving from slot 10 to 41), all intermediate slots must be filled with explicit placeholder pointers. Jumping indices without padding leads to incorrect function pointer dereferencing.
2. Verify VTable slot indices against specific WinMD versions: Interface inheritance (like IControl) often injects large blocks of methods from parents that must be accounted for. Silent crashes during method calls are a primary indicator of VTable slot misalignment.

### Examples

```
// Adding 30 placeholders to align put_Background to slot 41
_pad10_39: [30]?*const anyremote = undefined,
get_Background: *const anyremote = undefined, // slot 40
put_Background: *const fn (*Self, *IInspectable) callconv(WINAPI) HRESULT, // slot 41
```



