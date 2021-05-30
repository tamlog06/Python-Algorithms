# セレブ問題に対する単純な解法
def native_celeb(G):
    n = len(G)
    for u in range(n): # 候補者
        for v in range(n): # 候補者以外の全員
            if u == v:
                continue
            # 候補者が知ってたら飛ばす
            if G[u][v]:
                break
            # 知らなかったら飛ばす
            if not G[v][u]:
                break
        else:
            return u
    return None

if __name__ == "__main__":
    from random import randrange
    n = 100
    G = [[randrange(2) for i in range(n)] for i in range(n)]
    c = randrange(n)
    for i in range(n):
        G[i][c] = 1
        G[c][i] = 0
    print(native_celeb(G))