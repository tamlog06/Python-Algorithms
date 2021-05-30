# チェックボードの問題

def cover(board, lab=1, top=0, left=0, side=None):
    if side is None:
        side = len(board)
    
    # 部分ボードのへんの長さ
    s = side // 2

    # 部分ボードの外側と内側にある四角のオフセット
    offsets = (0, -1), (side-1, 0)

    for dy_outer, dy_inner in offsets:
        for dx_outer, dx_inner in offsets:
            # 外側の角に何もおかれていない場合
            if not board[top+dy_outer][left+dx_outer]:
                # 中心側の角にラベルをつける
                board[top+s+dy_inner][left+s+dx_inner] = lab

    # 次のラベル
    lab += 1 
    if s > 1:
        for dy in [0, s]:
            for dx in [0, s]:
                # sが２以上の場合、再帰呼び出し
                lab = cover(board, lab, top+dy, left+dx, s)

    # 次に使うことのできるラベルを返す
    return lab

if __name__ == "__main__":
    board = [[0]*8 for i in range(8)] 
    board[7][7] = -1 #　欠けている角 
    cover(board)
    for row in board:
        print((" %2i"*8) % tuple(row))
