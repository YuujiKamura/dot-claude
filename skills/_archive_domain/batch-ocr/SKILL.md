---
name: batch-ocr
description: バッチOCR - フォルダ内画像の文字抽出。(1) フォルダ内画像の文字一括抽出、(2) Gemini Flash Liteでの低コスト大量処理、(3) ocr_results.jsonへの保存。OCR、画像解析、文字抽出、黒板読み取り、領収書、名刺と言われた時に使用。
---

# バッチOCR - フォルダ内画像の文字抽出

## 概要

指定フォルダ内の画像から文字を一括抽出する。Gemini Flash Liteを使用し、低コストで大量処理可能。

## 使用方法

```bash
GEMINI_API_KEY="..." npx tsx scripts/readImages.ts <フォルダパス>
```

## スクリプトテンプレート

```typescript
// バッチOCRスクリプト
// 使い方: GEMINI_API_KEY="..." npx tsx scripts/readImages.ts <フォルダパス>
import { GoogleGenAI } from "@google/genai";
import * as fs from 'fs';
import * as path from 'path';

const BATCH_SIZE = 10;  // 1リクエストあたりの画像数

async function main() {
  const folderPath = process.argv[2];
  if (!folderPath) {
    console.error('使い方: npx tsx scripts/readImages.ts <フォルダパス>');
    process.exit(1);
  }

  if (!fs.existsSync(folderPath)) {
    console.error(`フォルダが見つかりません: ${folderPath}`);
    process.exit(1);
  }

  const apiKey = process.env.GEMINI_API_KEY;
  if (!apiKey) {
    console.error('GEMINI_API_KEY環境変数を設定してください');
    process.exit(1);
  }

  const ai = new GoogleGenAI({ apiKey });

  // 画像ファイルを取得
  const files = fs.readdirSync(folderPath)
    .filter(f => /\.(jpg|jpeg|png|gif|webp)$/i.test(f))
    .map(f => path.join(folderPath, f));

  console.log(`${files.length}枚の画像を処理します`);

  const results: { file: string; text: string }[] = [];

  // バッチ処理
  for (let i = 0; i < files.length; i += BATCH_SIZE) {
    const batch = files.slice(i, i + BATCH_SIZE);
    console.log(`\nバッチ ${Math.floor(i / BATCH_SIZE) + 1}/${Math.ceil(files.length / BATCH_SIZE)}`);

    const imageParts = batch.map(filePath => {
      const data = fs.readFileSync(filePath);
      const ext = path.extname(filePath).toLowerCase();
      const mimeType = ext === '.png' ? 'image/png' : 'image/jpeg';
      return {
        inlineData: { mimeType, data: data.toString('base64') }
      };
    });

    // プロンプトはユースケースに合わせてカスタマイズ
    const prompt = `
これらの画像に写っている文字を読み取ってください。

【出力形式】JSON配列
[
  {"index": 0, "text": "読み取った文字"},
  {"index": 1, "text": "読み取った文字"},
  ...
]

文字が見えない場合は "text": "文字なし" としてください。
`;

    try {
      const response = await ai.models.generateContent({
        model: 'gemini-2.0-flash-lite',  // 低コスト・高速
        contents: {
          parts: [...imageParts, { text: prompt }]
        },
        config: {
          responseMimeType: "application/json",
          temperature: 0.1
        }
      });

      const text = response.text || '[]';
      const parsed = JSON.parse(text) as { index: number; text: string }[];

      parsed.forEach((item) => {
        const fileName = path.basename(batch[item.index] || '');
        results.push({ file: fileName, text: item.text });
        console.log(`  ${fileName}: ${item.text.substring(0, 50)}...`);
      });

    } catch (err: any) {
      console.error(`エラー: ${err.message}`);
      batch.forEach(f => {
        results.push({ file: path.basename(f), text: 'エラー' });
      });
    }

    // レート制限対策
    if (i + BATCH_SIZE < files.length) {
      await new Promise(r => setTimeout(r, 1000));
    }
  }

  // 結果を保存
  const outputPath = path.join(folderPath, 'ocr_results.json');
  fs.writeFileSync(outputPath, JSON.stringify(results, null, 2), 'utf-8');
  console.log(`\n結果を保存: ${outputPath}`);
}

main().catch(console.error);
```

## コスト目安

| モデル | 入力 | 出力 | 100枚あたり |
|--------|------|------|-------------|
| gemini-2.0-flash-lite | 無料枠大 | 無料枠大 | ほぼ無料 |
| gemini-2.0-flash | $0.10/1M | $0.40/1M | 約$0.01 |

## カスタマイズ例

### 工事写真の黒板読み取り
```typescript
const prompt = `
工事写真に写っている黒板（工事看板）の文字を読み取ってください。
工事名、工種、測点、寸法などを抽出してください。
`;
```

### 領収書の金額抽出
```typescript
const prompt = `
領収書から以下を抽出してください：
- 日付
- 店舗名
- 合計金額
- 内訳（あれば）
`;
```

### 名刺の情報抽出
```typescript
const prompt = `
名刺から以下を抽出してください：
- 氏名
- 会社名
- 部署・役職
- 電話番号
- メールアドレス
`;
```

## 依存パッケージ

```bash
npm install @google/genai
npm install -D tsx
```
