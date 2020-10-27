import unittest
from game import Game
class TestGameMethods(unittest.TestCase):

    def test_Game(self):
        g = Game(10, 1, False)
        for _ in range(0,10):
            g.move(1)
            val = g.getGameStatus()
            self.assertIn(val[0], range(1,11))
    
    def test_CrookedGame(self):
        g = Game(10, 1, True)
        for _ in range(0,10):
            g.move(1)
            val = g.getGameStatus()
            self.assertIn(val[0], range(2,11,2))

if __name__ == '__main__':
    unittest.main()