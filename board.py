class Board():
    def __init__(self, size, noofplayers):
        self.size = size
        self.player_positions = [0]*noofplayers
        self.snakes = {}

    def getBoard(self):
        return self.player_positions, self.snakes

    def add_snakes(self, src, dest):
        if src<self.size and dest<self.size and src>dest:
            self.snakes[src] = dest
            return 
        raise Exception("Incorrect Value for src and dest")   
    
    def move(self, player, move):
        prev = self.player_positions[player-1]
        if (prev + move) < self.size:
            if (prev+move) in self.snakes.keys():
                self.player_positions[player-1] = self.snakes[prev+move]
                return
            self.player_positions[player-1] = prev + move

