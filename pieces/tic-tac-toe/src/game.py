class Game:
    def __init__(self):
        self.board = None
        self.current_player = None

    def start(self, player1, player2):
        from board import Board
        self.board = Board()
        self.current_player = player1
        self.board.initialize()
        self.play_turn()

    def play_turn(self):
        while True:
            move = self.current_player.make_move()
            if self.board.make_move(move, self.current_player):
                if self.board.check_winner(self.current_player):
                    print(f"{self.current_player.name} wins!")
                    break
                elif self.is_draw():
                    print("It's a draw!")
                    break
                self.current_player = self.current_player.opponent
            else:
                print("Invalid move, try again.")

    def is_draw(self):
        return all(cell is not None for row in self.board.grid for cell in row)

    def reset(self):
        self.board.initialize()
        self.current_player = None