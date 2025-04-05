import unittest
from src.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_start_game(self):
        self.game.start()
        self.assertIsNotNone(self.game.board)

    def test_play_turn(self):
        self.game.start()
        self.game.play_turn(0, 0)  # Player X plays
        self.assertEqual(self.game.board.get_cell(0, 0), 'X')

    def test_is_draw(self):
        self.game.start()
        moves = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        for move in moves:
            self.game.play_turn(*move)
        self.assertTrue(self.game.is_draw())

    def test_reset_game(self):
        self.game.start()
        self.game.play_turn(0, 0)
        self.game.reset()
        self.assertIsNone(self.game.board.get_cell(0, 0))

if __name__ == '__main__':
    unittest.main()