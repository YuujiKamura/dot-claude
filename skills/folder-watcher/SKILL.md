---
description: "folder-watcher: フォルダ監視、ディレクトリ監視、ファイル検知、notify、watcher、PDF監視、ビルド監視、ホットリロード"
project: photo-ai
---

# folder-watcher

Rust用の汎用フォルダ監視ライブラリ。ビルダーパターンとコールバックベースでファイルシステムイベントを処理。

## プロジェクト情報

- **リポジトリ**: `~/folder-watcher`
- **GitHub**: https://github.com/YuujiKamura/folder-watcher
- **言語**: Rust
- **依存クレート**: notify, thiserror, log

## 主な機能

- ファイルシステムイベント監視（create, modify, delete, rename）
- 拡張子フィルタ（PDF、TXTなど特定ファイルのみ監視）
- ビルダーパターンで直感的な設定
- 再帰/非再帰監視の切り替え
- スレッドセーフなコールバック

## API

### FolderWatcher

```rust
use folder_watcher::FolderWatcher;
use std::path::Path;

let watcher = FolderWatcher::new(Path::new("/path/to/watch"))
    .unwrap()
    .with_filter(&["pdf", "txt"])  // 拡張子フィルタ（ドット不要）
    .recursive(true)                // サブディレクトリも監視
    .on_create(|path| { /* ファイル作成時 */ })
    .on_modify(|path| { /* ファイル変更時 */ })
    .on_delete(|path| { /* ファイル削除時 */ })
    .on_rename(|path| { /* ファイルリネーム時 */ })
    .on_any(|path| { /* 全イベント */ });

watcher.start().unwrap();  // 監視開始
watcher.stop().unwrap();   // 監視停止
watcher.is_running();      // 実行中か確認
```

### WatcherBuilder

```rust
use folder_watcher::WatcherBuilder;

let watcher = WatcherBuilder::new(Path::new("/path"))
    .unwrap()
    .with_filter(&["pdf"])
    .recursive(true)
    .on_create(|path| println!("Created: {:?}", path))
    .build();
```

## ユースケース

### PDF監視（ShoruiCheckerスタイル）

```rust
let watcher = FolderWatcher::new(Path::new("/downloads"))
    .unwrap()
    .with_filter(&["pdf"])
    .on_create(|path| {
        let name = path.file_name()
            .map(|n| n.to_string_lossy().to_string())
            .unwrap_or_default();
        println!("新しいPDF: {}", name);
    });

watcher.start().unwrap();
```

### Tauri連携

```rust
let app_clone = app.clone();
let watcher = FolderWatcher::new(&folder_path)
    .map_err(|e| e.to_string())?
    .with_filter(&["pdf"])
    .on_create(move |path| {
        let _ = app_clone.emit("pdf-detected", serde_json::json!({
            "path": path.to_string_lossy(),
            "name": path.file_name().map(|n| n.to_string_lossy()).unwrap_or_default()
        }));
    });

watcher.start().map_err(|e| e.to_string())?;
```

## 使い方

### 依存関係追加

```toml
[dependencies]
folder-watcher = { path = "../folder-watcher" }
```

### サンプル実行

```bash
# 基本サンプル
cargo run --example basic -- /path/to/watch

# PDF監視サンプル
cargo run --example pdf_monitor -- /path/to/watch
```

## エラー型

```rust
pub enum WatcherError {
    PathNotFound(PathBuf),      // パスが存在しない
    NotADirectory(PathBuf),     // ディレクトリではない
    NotifyError(notify::Error), // notifyのエラー
    NotRunning,                 // 監視が開始されていない
    AlreadyRunning,             // 既に監視中
    LockError(String),          // ロック取得エラー
    ChannelError(String),       // チャネルエラー
}
```

## ファイル構成

```
folder-watcher/
├── Cargo.toml
├── README.md
├── src/
│   ├── lib.rs       # クレートエントリポイント、テスト
│   ├── watcher.rs   # FolderWatcher, WatcherBuilder実装
│   └── error.rs     # WatcherError定義
└── examples/
    ├── basic.rs           # 基本サンプル
    ├── pdf_monitor.rs     # PDF監視サンプル
    └── tauri_integration.rs  # Tauri連携例
```
