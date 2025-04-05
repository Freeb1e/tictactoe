class Player:
    def __init__(self, name):
        self.name = name

    def make_move(self):
        position = input(f"{self.name}, 请选择下棋的位置 (1-9): ")
        return int(position) - 1  # 转换为0索引