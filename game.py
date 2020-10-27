from dice import Dice
from board import Board
class Game():
    def __init__(self, size, noofplayer, crooked):
        self.dice = Dice(crooked)
        self.board = Board(size, noofplayer)
    
    def move(self, player):
        mov = self.dice.throw()
        self.board.move(player, mov)
    
    def getGameStatus(self):
        return self.board.getBoard()

    def add_snake(self, src, dest):
        self.board.add_snakes(src, dest)

    def run(self, noofturn=10):
        player = 1
        turn = 1
        self.add_snake(14,7)
        while turn <= noofturn:
            self.move(player)
            print ("Game Status %s after move %s" %(self.getGameStatus(), turn))
            turn = turn + 1

if __name__ == "__main__":
    g = Game(17, 1, False)
    g.run()

