import unittest
from board import Board
class TestBoardMethods(unittest.TestCase):

    def test_getBoard(self):
        b = Board(10, 1)
        val = b.getBoard()
        self.assertEqual([0], val)
    
    def test_getBoard_multiple_player(self):
        b = Board(10, 2)
        val = b.getBoard()
        self.assertEqual([0,0], val)
    
    def test_movegetBoard(self):
        b = Board(10, 1)
        b.move(1, 5)
        val = b.getBoard()
        self.assertEqual([5], val)
    
    def test_movegetBoard_multiple_player(self):
        b = Board(10, 2)
        b.move(1, 5)
        b.move(2, 3)
        val = b.getBoard()
        self.assertEqual([5,3], val)

if __name__ == '__main__':
    unittest.main()