import unittest
from dice import Dice
class TestDiceMethods(unittest.TestCase):

    def test_non_crooked(self):
        d = Dice()
        val = d.throw()
        self.assertIn(val, [1,2,3,4,5,6])

    def test_crooked(self):
        d = Dice(crooked=True)
        val = d.throw()
        self.assertIn(val, [2,4,6])
        
if __name__ == '__main__':
    unittest.main()