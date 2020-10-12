from __future__ import annotations
from numpy import empty



class Point:
    def __init__( self, x:int, y:int ): self.x, self.y = x,y
    def __repr__( self ): return f'Point({self.x},{self.y})'
    def __eq__( self, other: Point ): return self.x==other.x and self.y==other.y
    def __ne__( self, other: Point ): return not self.x==other.x and self.y==other.y
    def __hash__( self ): return hash(self.__repr__())



class Tile(Point):

    def __init__(self, x:int, y:int):
        super().__init__(x,y)
        self.state = "#"
    
    def set_state(self, state: str):
        self.state = state




class Game:

    WIDTH = 1
    HEIGHT = 1






    # Helper functions
    def find_neighbors(self):
        for tile in self.board.flatten():
            if tile.state  != "#":              # Finding neighbors from only valid tiles
                output = []
                for point in [(tile.x+1, tile.y),(tile.x-1, tile.y),(tile.x, tile.y+1),(tile.x, tile.y-1)]:
                    try:
                        assert 0 <= point[0] <= Game.WIDTH and 0 <= point[1] <= Game.HEIGHT
                        assert self.board[point[1], point[0]].state != "#"
                        output.append(self.board[point[1], point[0]])
                    except AssertionError:
                        pass
                self.neighbors[tile] = output


    def get_neighbors(self, point):
        return self.neighbors[point]

    
    def bfs(self, start):
        queue = [start]
        seen = {start}
        paths = {start:[start]}

        while len(queue)>0:
            current = queue.pop(0)
            currlist = paths[current]

            for neighbor in self.get_neighbors(current):
                if neighbor not in seen:
                    seen.add(neighbor)
                    paths[neighbor] = currlist + [neighbor]
                    queue.append(neighbor)
        
        return paths






    # Initial values for the game
    def __init__(self):
        self.neighbors = {}

        self.board = empty(shape=(Game.HEIGHT, Game.WIDTH), dtype=Tile)
        self.board.flat = [Tile( tile % Game.HEIGHT, tile // Game.WIDTH) for tile in range(Game.TILE_COUNT)]        






    # Handle inputs for the game
    def game_input(self):

        for y in range(Game.HEIGHT):          # reading game board
            for x, state in enumerate(input()):
                self.board[y,x].set_state(state)
        
        self.find_neighbors()           # find all valid neighbors from a cell






    # Add the logic to move your bots here
    def game_move(self):
        pass






    # Print the outputs
    def game_output(self):
        pass

    




game = Game()

while True:
    game.game_input()
    game.game_move()
    game.game_output()