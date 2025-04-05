import unittest
from src.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.board.initialize()

    def test_initialize(self):
        self.assertEqual(self.board.display(), " 1 | 2 | 3 \n---|---|---\n 4 | 5 | 6 \n---|---|---\n 7 | 8 | 9 ")

    def test_make_move(self):
        self.board.make_move(1, 'X')
        self.assertEqual(self.board.display(), " X | 2 | 3 \n---|---|---\n 4 | 5 | 6 \n---|---|---\n 7 | 8 | 9 ")

    def test_check_winner(self):
        self.board.make_move(1, 'X')
        self.board.make_move(2, 'X')
        self.board.make_move(3, 'X')
        self.assertTrue(self.board.check_winner('X'))

    def test_draw(self):
        moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(len(moves)):
            self.board.make_move(moves[i], 'X' if i % 2 == 0 else 'O')
        self.assertFalse(self.board.check_winner('X'))
        self.assertFalse(self.board.check_winner('O'))

if __name__ == '__main__':
    unittest.main()