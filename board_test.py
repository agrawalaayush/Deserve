import unittest
from board import Board
class TestBoardMethods(unittest.TestCase):

    def test_getBoard(self):
        b = Board(10, 1)
        val, _ = b.getBoard()
        self.assertEqual([0], val)
    
    def test_getBoard_multiple_player(self):
        b = Board(10, 2)
        val, _ = b.getBoard()
        self.assertEqual([0,0], val)
    
    def test_addSnakes(self):
        b = Board(10, 1)
        with self.assertRaises(Exception):
            b.add_snakes(1,7)
        _,snakes = b.getBoard()
        self.assertEqual({}, snakes)
        b.add_snakes(7,1)
        val,snakes = b.getBoard()
        self.assertEqual({7:1}, snakes)
        self.assertEqual([0], val)
        b.move(1, 3)
        b.move(1, 4)
        val,_ = b.getBoard()
        self.assertEqual([1], val)
    
    def test_movegetBoard(self):
        b = Board(10, 1)
        b.move(1, 5)
        val,_ = b.getBoard()
        self.assertEqual([5], val)
    
    def test_movegetBoard_multiple_player(self):
        b = Board(10, 2)
        b.move(1, 5)
        b.move(2, 3)
        val,_ = b.getBoard()
        self.assertEqual([5,3], val)

if __name__ == '__main__':
    unittest.main()