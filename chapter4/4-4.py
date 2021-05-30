# 最大置換問題の単純な実装
from random import randrange
from time import time
import sys

sys.setrecursionlimit(10**9)

def naive_max_perm(M, A=None):
    # 要素が与えられていなかった場合
    if A is None:
        A = set(range(len(M)))
    # ベースケース
    if len(A) == 1:
        return A 
    # 指定している要素
    B = set(M[i] for i in A)
    # 指定されていない要素
    # 差集合
    C = A - B
    if C:   # 役に立たない要素が1つ以上ある場合
        A.remove(C.pop())
        return naive_max_perm(M, A)
    return A

if __name__ == "__main__":
    size = 10**4
    t1 = time()
    M = [randrange(size) for i in range(size)]
    # M = [2, 2, 0, 5, 3, 5, 7, 4]
    print(naive_max_perm(M))
    t2 = time()
    print(t2-t1)