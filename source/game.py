"""
Board class.

"""
import random
from tile import Tile

class Game:
    def __init__(self):
        self.board = Game.init_board()
        
        return
    
    def __str__(self):
        for row in self.board:
            for tle in row:
                print(tle, end="")
            print()
    
    
    def init_board(n, m):
        """
        Fill an n x m board with mines.
        Amount of mines is proportional to board size. 
        Returns the board.
        """
        
        arr = []
        row = []
        for i in range(n):
            for j in range(m):
                # initalize the tiles with value -2
                row[j] = Tile(-2)
        
            arr.append(row)        
        
        
        board = Game.init_mines(arr)
        
        
    def init_mines(arr):
        """
        Place the mines in the 2d array randomly.
        The number of mines in a game is ~15% of tiles
        """
        
        # approximate 15% of the number of tiles 
        mine_count = round ( ( len(arr) * len(arr[0]) ) / 15 )
        
        # populate the board with mines 
        
        for row in arr:
            for tle in row:
                if (random.randint(0, 100) <= 15):
                    # make this tile a bomb
                    tle.set_bomb()
                    
        return arr
            
            
        
        
        
    