# Pytori
Pyとり検証用
## Usage
1. クーロン
```
$ git clone git@github.com:hidonmura/Pytori.git
```
2. ファイル修正
```
$ vim siritori.py
```
3. 解析ファイル名指定
```
if __name__ == "__main__":
    target_file = '1_hoge.py'  # 解析対象のPythonファイル名
    builtin_usages = analyze_builtin_functions(target_file)
```
4. 解析実行
```
$ python siritori.py 
ファイル '1_hoge.py' で使用されている組み込み関数:
  行 4: print()
  行 8: sum()
  行 9: print()
```
