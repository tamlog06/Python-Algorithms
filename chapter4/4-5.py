from random import randrange
from time import time

def max_perm(M):
    n = len(M)
    A = set(range(n))
    count = [0]*n
    for i in M:
        count[i] += 1
    # 役に立たない要素
    Q = [i for i in A if count[i] == 0]
    while Q:
        i = Q.pop()
        A.remove(i)
        j = M[i]
        count[j] -= 1
        if count[j] == 0:
            Q.append(j)
    return A

if __name__ == "__main__":
    size = 10**4
    t1 = time()
    M = [randrange(size) for i in range(size)]
    # M = [2, 2, 0, 5, 3, 5, 7, 4]
    print(max_perm(M))
    t2 = time()
    print(t2-t1)