---
name: win32-tsf-ime
description: "TSF (Text Services Framework) による日本語IME実装の知見。CJK入力でTSFが必須な理由、pre-edit/commit遷移、漢字欠落デバッグ、TSF vs TextBox判断基準。TSF、IME、日本語入力、漢字欠落、pre-edit、composition、ghostty、ターミナルと言われた時に使用。"
---

# Win32 TSF IME 実装知見

## 1. TSFが必須な理由

標準TextBoxやIMM32(レガシー)ではCJK入力の未確定状態を正確に扱えない。TSFが必要。

- TextBoxは節(clause)レベルの装飾（変換中セグメントの下線種別）を隠蔽する
- TSFはcommitted/uncommitted境界の正確な位置を提供する
- ターミナルはグリッド内にpre-edit状態をネイティブ描画する必要があり、UIコントロールの差分検出では精度不足

| | IMM32（旧） | TSF（現行） |
|---|---|---|
| 時代 | Win95〜 | WinXP〜 |
| 方式 | WM_IME_* メッセージ | COMインターフェース |
| 節境界 | 取得不可 | clause start/end取得可 |
| 柔軟性 | IME専用 | 音声入力・手書き等も統合 |

## 2. IME Pre-edit vs. Commit ライフサイクル

日本語入力は3段階の状態遷移:
1. **Pre-edit（未確定）**: キー入力 → ひらがな表示（下線付き）
2. **変換中**: 変換キー → 漢字候補リスト
3. **Commit（確定）**: 確定 → アプリにテキスト挿入

### 漢字欠落バグのパターン
- `handleOutput`でpre-edit→commit遷移時にバッファフラッシュとターミナル描画ループが同期していない
- compositionとresult stringを同時に扱う必要がある（単純なストリームではない）
- 修正: pre-editレンダリングとcommit出力を明示的に分離

```zig
// handleOutput must handle the delta between composition and commit
fn handleOutput(self: *Self, text: []const u8, is_final: bool) !void {
    if (is_final) {
        // commit: flush to PTY
    } else {
        // pre-edit: render inline with decorations
    }
}
```

## 3. デバッグ手法

- `GHOSTTY_CONTROL_PLANE=1` でIME状態遷移を他UIイベントから隔離テスト
- Base64エンコードでマルチバイト文字をプロセス境界越しに注入（パイプでの文字化け防止）
- WM_USER+7 カスタムメッセージでXAML IMEパスをシミュレート

## 4. ghostty-win固有の注意点

- WTのTSF書き直し(PR#17067)を1:1移植中
- Zig + 手書きCOM vtableでTSFインターフェースを実装（C++/WinRT不使用）
- win-zig-bindgenでTSFインターフェースが未生成の場合、手動実装はメンテナンストラップ → ジェネレータ対応を優先
