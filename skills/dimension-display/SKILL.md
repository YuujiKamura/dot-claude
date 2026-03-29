---
description: "trianglelist寸法表示: Dims.kt/DimOnPath.kt/MyView.kt 3層構造。Use when: OUTER/INNER配置, HABAYOSE, A辺接続, 寸法線描画, offsetV/offsetH"
project: photo-ai
---

# 三角形リスト 寸法表示仕様

## 概要

Android版trianglelistの寸法表示システムは3層構造：
1. **データモデル層** (`Dims.kt`): 配置設定を保持
2. **経路計算層** (`DimOnPath.kt`): 表示位置を計算
3. **描画層** (`MyView.kt`): Canvas/DXFに描画

## 1. 配置オプション

### 1.1 垂直配置 (vertical)
| 値 | 定数 | 意味 |
|----|------|------|
| 1 | OUTER | 辺の外側 |
| 3 | INNER | 辺の内側 |

### 1.2 水平配置 (horizontal)
| 値 | 定数 | 意味 | 寸法線 |
|----|------|------|--------|
| 0 | CENTER | 中央 | なし |
| 1 | INRIGHT | 内側・右寄せ | なし |
| 2 | INLEFT | 内側・左寄せ | なし |
| 3 | OUTERRIGHT | 外側・右寄せ | あり |
| 4 | OUTERLEFT | 外側・左寄せ | あり |

**重要**: 寸法線は `horizontal > 2` の場合のみ描画

## 2. オフセット計算

### 2.1 垂直オフセット (offsetV)
```
offsetUpper = -dimheight × 0.2  (上側配置)
offsetLower =  dimheight × 0.9  (下側配置)
```

### 2.2 水平オフセット (offsetH)
```
HABAYOSE = lineLength × 0.1  (辺の長さの10%)
```

### 2.3 外側配置の詳細
```
SUKIMA = 0.5 × scale      (辺からの距離)
HATAAGE = -3 × scale      (引出線の高さ)
HABAYOSE = -lineLength × 0.05  (テキスト位置補正)
```

## 3. テキスト方向の自動調整

```kotlin
if (pointA.x >= pointB.x) {
    // 反時計回りに変更
    clockwise = "A"
    offsetH = -offsetH
    // 始点・終点を交換
    swap(pointA, pointB)
    // 垂直オフセットも反転
}
```

**目的**: テキストが常に左から右へ読めるように自動調整

## 4. 接続辺（A辺）の特別な扱い

### 4.1 A辺の寸法表示条件
```
表示する = (mynumber == 1) OR (connectionSide > 2) OR (cParam_.type != 0)
```
- 最初の三角形: 常に表示
- 未接続: 表示
- 特殊接続モード: 表示
- **通常の接続辺: 非表示**（親と共有しているため二重表示を避ける）

### 4.2 A辺の垂直配置
```
if (接続辺 AND ユーザー操作なし):
    return OUTER  (外側)
else:
    return INNER  (内側)
```

## 5. B/C辺の自動配置（面積比較）

```kotlin
fun autoDimVerticalByAreaCompare(node: Triangle?): Int {
    if (node == null) return OUTER
    return if (node.getArea() > triangle.getArea() && node.connectionSide < 3)
        OUTER else INNER
}
```

**ロジック**:
- 子ノードがない → 外側
- 子の面積 > 自分の面積 かつ 子が接続中 → 外側
- それ以外 → 内側

## 6. フォントサイズ

### 6.1 範囲制限
```
最小値: 8f
最大値: 80f
```

### 6.2 テキスト間隔
```
textSpacer = textSize × 0.2  (フォントサイズの20%)
```

### 6.3 文字配置（複数桁）
```kotlin
// 5文字を想定した中央揃え
position[i] = offsetH + (i - 2) × onecharsize
onecharsize = textSize × 0.5
```

## 7. 色設定

| 状態 | 色 | ARGB |
|------|-----|------|
| 通常 | 白 | (255,255,255,255) |
| 選択中 | 薄黄 | (255,255,255,100) |
| グレイアウト | 黄 | (150,255,255,0) |

## 8. 描画方式

**重要**: 引出線・寸法補助線は存在しない

### 描画方法
- `Canvas.drawTextOnPath()` で辺に沿ってテキストを直接描画
- テキストは辺のパスに沿って配置される
- オフセット(offsetV/offsetH)で辺からの距離を調整

### 外側配置時の引出線（horizontal > 2）
- 辺の外側に配置する場合のみ、短い接続線を描画
- これは寸法補助線ではなく、テキスト位置を示す参照線
- 矢印なし、シンプルな直線

## 9. ズーム時の振る舞い

### 9.1 テキストスペーサー調整
```
printScale > 5.0 → spacer = 0.2f
printScale > 3.0 → spacer = 0.5f
else             → spacer = 2.0f
```

### 9.2 再計算トリガー
ズーム変更時に `setDimPath()` を呼び出して全座標を再計算

## 10. 実装チェックリスト

Web版実装時の確認項目:

- [ ] 垂直配置（内側/外側）の切り替え
- [ ] 水平配置（5段階）の対応
- [ ] テキスト方向の自動調整（左→右）
- [ ] A辺（接続辺）の非表示処理
- [ ] B/C辺の面積比較による自動配置
- [ ] 寸法線の条件付き描画（horizontal > 2）
- [ ] フォントサイズ制限（8-80）
- [ ] 複数桁の中央揃え配置
- [ ] ズーム追従

## 関連ファイル

- `app/src/main/java/com/jpaver/trianglelist/Dims.kt`
- `app/src/main/java/com/jpaver/trianglelist/DimOnPath.kt`
- `app/src/main/java/com/jpaver/trianglelist/MyView.kt`
- `app/src/test/java/com/jpaver/trianglelist/TriListDimTest.kt`
