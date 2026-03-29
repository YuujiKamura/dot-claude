---
paths:
  - "src/apprt/winui3/**"
  - "src/apprt/win32/**"
  - "src/renderer/D3D11.zig"
  - "**/*com*.zig"
  - "**/*vtable*.zig"
  - "**/*winrt*.zig"
  - "**/*xaml*.zig"
  - "**/*tsf*.zig"
---
# Zig COM/WinRT Known Issue Patterns

## vtable スロットずれ
- **検出条件:** `VTable` struct定義で `fn` の並び順が変更された、または新しいメソッドが追加された
- **問題:** DLL側とZig側でvtable ABIが不整合になりSEGFAULT。全UIAテストが崩壊する
- **正しい対処:** DLL側にメソッドを追加したらZig側のVTable structも同じ順序で追従。スロット番号をコメントで明記
- **発見日:** 2026-03-22
- **発生元:** ghostty-win CP DLL vtable修正 (control-plane-server DLLが`read_buffer_for_tab`+`send_input_to_tab`追加→Zig側未追従)

## comptime条件でReleaseFastパスが消える
- **検出条件:** `comptime` + `Debug` or `builtin.mode` でゲートされたコードブロック
- **問題:** Release buildで必要なコードパス（IXamlMetadataProvider等）が消えてクラッシュ
- **正しい対処:** comptime条件を削除するか、Debug/Release両方で必要なパスは条件外に出す
- **発見日:** 2026-03-19
- **発生元:** Issue #122 ReleaseFastクラッシュ (activateXamlType()のcomptime Debugゲート)

## `*?*anyopaque` vs `?*anyopaque` ポインタ型混同
- **検出条件:** `anyopaque` を含むポインタ型宣言、特に `*?*anyopaque`
- **問題:** WinRT APIのバインディングでポインタの間接参照レベルを間違えると、GetText等でlen=0が返る
- **正しい対処:** WTソースの対応する型定義と1:1で比較。`?*anyopaque`（nullable pointer to opaque）が正しいケースが多い
- **発見日:** 2026-03-19
- **発生元:** Issue #123 TSF IME ShiftEndバインディングバグ

## WinUI3 PRI初期化なしでXamlControlsResources使用
- **検出条件:** `XamlControlsResources` or `AcrylicBackgroundFillColorDefaultBrush` がコード内にある
- **問題:** App.xaml + XAMLコンパイラなしでは PRI リソースが解決できずランタイムエラー
- **正しい対処:** MRT Core手動初期化 or ResourceDictionary.Source直接設定
- **発見日:** 2026-02
- **発生元:** winui3-baseline スキル記載

## IXamlType スロット番号のUWP/WinUI3差異
- **検出条件:** `IXamlType` vtable アクセス、特に `ActivateInstance` or `BoxedType`
- **問題:** UWPとWinUI3でget_BoxedType(slot 17)の有無が違う。ActivateInstanceはWinUI3でslot 19
- **正しい対処:** WinUI3のメタデータ(.winmd)からスロット番号を確認。UWPの前提で書かない
- **発見日:** 2026-02
- **発生元:** MEMORY.md IXamlType注意事項
