---
name: locality-of-behavior
description: コードの振る舞いの局所化 (LoB)。認知負荷を下げるために、コードのある部分だけを見てその振る舞いが分かるようにする。DRY原則でコードを分割した後に「脳が滑る」「読んでも頭に入らない」コードになっていないかチェック。リファクタリング、コードレビュー、読みづらい、認知負荷、理解しにくい、脳が滑ると言われた時に使用。
category: rust-patterns
---

# Locality of Behavior (振る舞いの局所化)

## 原則

> "The behaviour of a unit of code should be as obvious as possible by looking only at that unit of code."
> （コードの構成単位の振る舞いは、その部分だけを見ることで可能な限り特定できるべきである）

出典: [htmx - Locality of Behaviour](https://htmx.org/essays/locality-of-behaviour/)
原典: Richard P. Gabriel. *Patterns of Software*, 1996

## 問題パターン: 未解決スタック

DRY原則でコードを分割するとき、**「理解の保留」が必要なスタイル**になっていないか。

```
// ❌ 悪い例: ExecuteAsyncの理解を保留したまま、複数の引数の中身を読み解く
return await PaymentApiHelper.ExecuteAsync(
    request,
    onSuccess: response => response.TransactionId,
    onUserNotFound: problem => PaymentUserException.Create(
        domain: DomainName,
        operation: ChargeOperation,
        targetUserId: request.UserId,
        problem),
    // ... まだ続く。脳が滑る
);
```

→ 視点移動が多い。ExecuteAsyncの意味を保持しながら各引数のラムダを読む = ワーキングメモリ圧迫

## 解決パターン: 先に宣言、後で組み立て

```
// ✅ 良い例: 処理を先に宣言してから組み立てる
Exception OnUserNotFound(PaymentProblem problem)
    => PaymentUserException.Create(DomainName, ChargeOperation, request.UserId, problem);

Exception OnInsufficientFunds(PaymentProblem problem)
    => PaymentBalanceException.Create(DomainName, ChargeOperation, request.Amount, problem);

return await PaymentApiHelper.ExecuteAsync(
    request,
    onSuccess: response => response.TransactionId,
    onUserNotFound: OnUserNotFound,
    onInsufficientFunds: OnInsufficientFunds,
    onError: OnError,
    token
);
```

→ ExecuteAsyncを読む時点で、各処理の名前から意味がわかる。中身は上で宣言済み。スタックなし。

## チェックリスト

コードレビュー・リファクタリング時に確認:

1. **この部分だけ見て何をしているか分かるか？** 他のファイルにジャンプしないと理解できないなら局所性が低い
2. **未解決スタックを積んでいないか？** 関数呼び出しの中にラムダやコールバックがネストして、外側の文脈を保持しながら内側を読む必要があるなら認知負荷が高い
3. **DRY原則が読みやすさを犠牲にしていないか？** 重複除去は価値があるが、それによって「情報の距離」が離れすぎていないか
4. **俯瞰しても詳細を見ても分かるか？** 大きな構造を見て全体像が掴め、小さな部分を見て詳細が分かる、両方が成立しているか

## 適用タイミング

- コードレビューで「読みづらい」と感じたとき
- リファクタリング後に「DRYにしたのに逆に分かりにくくなった」とき
- コールバック・ラムダ・高階関数が3段以上ネストしているとき
- メソッドの引数が5個以上で、それぞれが複雑な式のとき
