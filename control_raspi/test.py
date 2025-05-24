import maxmin
while True:
    board_input = input("输入棋盘状态: ").strip().replace('N', ' ')
    maxmin.one_step(board_input)