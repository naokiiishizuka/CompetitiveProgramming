# Codex メモ

## CLIでの文言
CLIではプログラム以外は日本語で回答する

## リポジトリ構成
- `test/1.cpp`: 文字列を読み込み `Hello <name>` を出力するサンプル。
- `atcoder/dp/*.py` / `atcoder/dp/*.cpp`: AtCoder DP 系の練習コード。
- `a.out`: 直近で `g++` を実行した際のデフォルト生成バイナリ。

## 実行メモ
### C++ サンプル (`test/1.cpp`)
```bash
cd /Users/ishidzukanaoki/development/CompetitiveProgramming
g++ -std=c++17 -O2 -Wall -Wextra test/1.cpp -o test/1
./test/1          # 入力文字列を与える
```

### Python の標準入力をファイルから与える
`input.txt` をコードと同じディレクトリに置き、リダイレクトする:
```bash
python3 atcoder/dp/1.py < input.txt
```
`atcoder/dp/2.py` には `input()` を `input.txt` に差し替える処理を記述済み。

## トラブルシュート
- `zsh: bus error ./a.out`  
  C/C++ のメモリアクセス違反。`-g -fsanitize=address,undefined` を付けてビルドし、`lldb`/`gdb` で原因を追跡する。
- `result[i - 1]` 参照時の注意  
  DP 配列の初期条件を満たすように `result[0]` への代入や番兵の導入が必要。

## コーディングメモ
- Python で `n` 個の値を読む: `values = [int(input()) for _ in range(n)]`
- `atcoder/dp/1.py` の初期化で `result = max(...)` とするとリストが整数に置き換わり `TypeError` になるので `result[0] = ...` と書く。
