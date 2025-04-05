class Board:
    def __init__(self):
        self.board = []
        self.initialize()

    def initialize(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def make_move(self, row, col, player):
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False

    def check_winner(self):
        # 检查行
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        # 检查列
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        # 检查对角线
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return None