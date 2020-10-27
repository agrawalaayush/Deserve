import unittest
from game import Game
class TestGameMethods(unittest.TestCase):

    def test_Game(self):
        g = Game(10, 1, False)
        for _ in range(0,10):
            g.move(1)
            val, _ = g.getGameStatus()
            self.assertIn(val[0], range(1,11))
    
    def test_Game_snakes(self):
        g = Game(10, 1, False)
        g.add_snake(8,2)
        for _ in range(0,10):
            g.move(1)
            val, snake = g.getGameStatus()
            self.assertEqual({8:2}, snake)
            self.assertIn(val[0], range(1,11))
    
    def test_CrookedGame(self):
        g = Game(10, 1, True)
        for _ in range(0,10):
            g.move(1)
            val,_ = g.getGameStatus()
            self.assertIn(val[0], range(2,11,2))

if __name__ == '__main__':
    unittest.main()