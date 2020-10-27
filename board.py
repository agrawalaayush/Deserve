class Board():
    def __init__(self, size, noofplayers):
        self.size = size
        self.player_positions = [0]*noofplayers

    def getBoard(self):
        return self.player_positions
    
    def move(self, player, move):
        prev = self.player_positions[player-1]
        if (prev + move) < self.size:
            self.player_positions[player-1] = prev + move

