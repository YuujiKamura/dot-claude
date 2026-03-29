---
description: テキスト描画における座標系の違いと向きの補正。DXF(Y上向き)とスクリーン(Y下向き)間での回転角度の扱い。BBOX-based text rendering実装時に使用。
project: photo-ai
keywords: テキスト, 回転, 座標系, DXF, BBOX, Y軸, 向き, Canvas2D, 描画
---

# テキスト描画の座標系と向きの補正

## 核心

DXF座標系（Y軸上向き）とスクリーン座標系（Y軸下向き）では、回転角度の解釈が逆になる。

```
DXF: -90度回転 = 反時計回り = 下から上に読む
スクリーン: -90度回転 = 時計回り = 上から下に読む
```

## 補正方法

DXFの回転角度をスクリーン座標系で使う場合、符号を反転する：

```rust
// DXF → スクリーン座標系への変換
let screen_rotation = -dxf_rotation;
```

## 実例：道路断面図

路線が左→右に流れるとき、縦書きテキスト（幅員・測点名）は「上から下」に読めるのが自然。

```rust
// road_section.rs での実装
let entity = TextEntity::new(&text.text, text.x as f32, text.y as f32, text.height as f32)
    .with_rotation(-text.rotation as f32)  // 反転で補正
    .with_alignment(align)
    .with_color(&color);
```

## テキストの「流れ」

テキストは左から右に流れる（"ABC" → A→B→C）。この流れは座標変換後も保持されるべき。

180度回転すると流れが反転して見える（右から左に読むことになる）。これを防ぐ：

```rust
// 逆さま補正（auto_readable）
let angle_rad = rotation.to_radians();
if angle_rad > PI/2 || angle_rad < -PI/2 {
    rotation += 180.0;
}
```

## BBOX-based text rendering

テキストにモデル座標系でのBBOXを持たせ、ビュー変換に追随させる。

1. TextEntity: position, height, rotation, alignment をモデル座標で保持
2. bbox_corners(): 回転を適用した4隅座標を計算
3. transform_text_bbox(): BBOXをスクリーン座標に変換、スクリーン上の高さと回転を計算
4. draw_text_entity(): 変換結果でCanvas 2Dにテキスト描画

## 関連ファイル

- `trianglelist-web/src/render/text.rs` - TextEntity, transform_text_bbox
- `trianglelist-web/src/render/text_canvas2d.rs` - draw_text_entity
- `trianglelist-web/src/render/road_section.rs` - draw_road_section_bbox
