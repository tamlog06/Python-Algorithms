# セレブ問題の解法

def celeb(G):
    n = len(G)
    u, v = 0, 1 # 最初の2つ
    for c in range(2, n+1):
        # uがvを知っているなら、uはセレブではないからuを次の候補者cで置き換え
        if G[u][v]:
            u = c
        # uがvを知らないなら、vはセレブではないからvを次の候補者cで置き換え
        else:
            v = c
    if u == n:
        c = v  # uは最後にvを使って置換
    else:
        c = u   # そうでなければuは候補者
    # ここまでで、とりあえずcは一番有力候補となる。後は本当にセレブかどうか確かめる。
    for v in range(n):
        if c == v:
            continue
        if G[c][v]:
            break
        if not G[v][c]:
            break
    else:
        return c
    return None

if __name__ == "__main__":
    from random import randrange
    n = 100
    G = [[randrange(2) for i in range(n)] for i in range(n)]
    c = randrange(n)
    for i in range(n):
        G[i][c] = 1
        G[c][i] = 0
    print(celeb(G))