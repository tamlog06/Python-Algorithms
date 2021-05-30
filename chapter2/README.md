# アルゴリズム解析の基礎
この章の主なトピックは漸近記法と、木構造とグラフの表現方法

## 漸近記法
O(n)の記法のこと
listの処理：appendはinsertよりずっと速い
nのリストにappendするO(1)
0位置にinsertするO(n)

### 時間測定にはtimeitを使う
    >>> import timeit  
    >>> timeit.timeit("x=2+2)  
    0.033166457898914814  
    >>> timeit.timeit("x=sum(range(10))")  
    0.3581548340152949  

この関数は中身を何度も繰り返し行うことで時間を表示するので、繰り返しの実行に影響があるものを書くのは避ける


### ボトルネックを見つけるためにプロファイラを用いる
cProfileを用いるとどこに時間がかかっているのか教えてくれる
次のコードは、メイン関数の名前がmainだった時のもの
main内で呼んでる関数とかの時間も出してくれる
    import cProfile
    cProfile.run("main()")

## グラフの実装
木構造は特別な種類のグラフに過ぎないが、木として表せる実用的な構造が多いので、木として洗わせれば大抵のアルゴリズムなどは適用できる
図2-3は次のようなセット構造で書ける(2-1.py)  
セットで書くのか、リストで書くのか、辞書で書くのかは何をしたいかによって決める

    a, b, c, d, e, f, g, h = range(8)
    N = [
        {b, c, d, e, f}, # a
        {c, e},          # b
        {d},             # c
        {e},             # d
        {f},             # e
        {c, g, h},       # f
        {f, h},          # g
        {f, g}           # h
    ]


### インタラクティブにスクリプトを実行したい場合
    python -i 2-1.py
こうすることで、2-1.pyが実行されて、その変数などを全て使える状態で対話モードでpythonを実行できる

### 隣接行列
各ノードが近傍かどうかを示すbooleanやbinaryを全てに格納して書く
重みを付与したい時などは、この値に重みを入れれば簡単に書けることになる

## 木構造の実装
例えばクラスを書いて、二分木を表現できる(2-7.py)


## リストとセット
セット型は重複を無くした配列になるが、その代わりにメリットがいくつもある
まず、メンバーシップの確認が定数時間になる  
    >>> from random import randrange  
    >>> L = [randrange(10000) for i in range(1000)]  
    >>> 42 in L  
    False (O(n)の計算)  
    >>> S = set(L)  
    >>> 42 in S  
    False (O(1)の計算)  

## 浮動小数点
正確な浮動小数点の計算が必要な時の計算の仕方  
1. 大体等しいかどうか確認したい -> unittestモジュールのassertAlmostEaual  

    >>> def almost_equal(x, y, places=7):  
    ....return round(abs(x-y), places) == 0  

    >>> almost_equal(sum(0.1 for i in range(10)), 1.0):  
    True

2. 正確な計算 -> decimalモジュール

    >>> from decimal import *  
    >>> sum(Decilmal("0.1" for i in range(10)) == Decimal("1.0")  
    True
