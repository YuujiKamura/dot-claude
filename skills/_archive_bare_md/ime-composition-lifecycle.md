---
name: ime-composition-lifecycle
description: "IME入力のpre-edit→変換→commit遷移管理。ターミナルでの漢字欠落防止、バッファ同期。IME、composition、pre-edit、commit、漢字欠落、ライフサイクル、変換と言われた時に使用。"
---

# IME Composition ライフサイクル

**注意**: TSF全般の知見は `win32-tsf-ime` スキルを参照。本スキルはcomposition状態遷移に特化。

## 状態遷移

```
[idle] --keydown--> [pre-edit: ひらがな表示] --変換--> [候補選択中] --確定--> [commit: 漢字出力] --> [idle]
```

## ターミナルでの実装ポイント

1. **pre-editとcommitは別パスで処理**: 同一ストリームとして扱うと確定時に文字が欠落する
2. **バッファフラッシュのタイミング**: commit時にPTYへ送出するが、pre-editレンダリングのクリアと同期が必要
3. **複数節(clause)の装飾**: 変換中は節ごとに下線種別が異なる（太線=変換対象、細線=未変換）

## よくあるバグ

| 症状 | 原因 | 対処 |
|---|---|---|
| 漢字部分が消える | handleOutputでis_final判定ミス | composition stringとresult stringを分離 |
| 二重入力 | pre-editクリア前にcommitが走る | クリア→commit→再描画の順序を保証 |
| カーソル位置ズレ | composition内のカーソルオフセット未反映 | TSFからclause境界+カーソル位置を取得 |
