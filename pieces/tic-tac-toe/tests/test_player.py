import unittest
from src.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Alice")

    def test_player_name(self):
        self.assertEqual(self.player.name, "Alice")

    def test_make_move(self):
        move = (0, 0)
        self.player.make_move(move)
        self.assertEqual(self.player.move, move)

if __name__ == '__main__':
    unittest.main()