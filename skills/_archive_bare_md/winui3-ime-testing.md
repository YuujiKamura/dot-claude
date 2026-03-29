---
name: winui3-ime-testing
description: "WinUI3/XAML IslandsでのIMEテスト手法。SendInputではXAML IMEパスが発火しないため、WM_USER+7内部注入とBase64プロトコルを使う。IMEテスト、入力テスト、Base64注入、WM_USER、composition、XAML Islandsと言われた時に使用。"
---

# WinUI3 IME テスト手法

## 1. 問題: 標準的な自動入力ではIMEパスが通らない

SendInputやPostMessage/WM_CHARはXAMLの高レベルイベント（CompositionStarted, TextChanged, flushImeTextBoxCommittedDelta）を発火しない。IMEバグの再現には専用の注入アーキテクチャが必要。

## 2. 内部注入アーキテクチャ

カスタムウィンドウメッセージ経由でUIスレッドにテキストを渡し、SetTextを**internalフラグなしで**呼ぶことで、フレームワークにデルタ変更として認識させる。

```zig
// カスタムメッセージ定義
const WM_APP_IME_INJECT = win.WM_USER + 7;

// App.zig: メッセージハンドラ
fn onImeInject(self: *App, payload: []const u16) void {
    const hstr = try winrt.hstringRuntime(payload);
    // internalフラグなし → TextChangedイベントが正しく発火
    self.textbox.SetText(hstr);
}
```

## 3. Base64プロトコル（マルチバイト安全）

コントロールプレーン→アプリ間のプロセス境界でUTF-8文字列がパイプ経由で壊れる問題を回避。

```zig
// コントロールプレーン側でBase64デコード → UTF-16変換 → メッセージループにPost
const decoded_bytes = try base64.Decoder.decode(allocator, b64_payload);
const utf16_payload = try std.unicode.utf8ToUtf16LeAlloc(allocator, decoded_bytes);
PostMessageW(hwnd, WM_APP_IME_INJECT, ...);
```

## 4. 注意点

- **pending_ime_injects キュー**: 非同期コントロールプレーンスレッドとUIメッセージループ間のハンドオーバーにキューが必要（レース条件防止）
- **マウス操作禁止**: CLAUDE.mdルールにより、テストでマウスポインタを奪うSendInput(マウス)は使用不可
- キーボード入力テストはSendInput（キーボードのみ）を使用
