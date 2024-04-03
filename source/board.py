import random
from tile import Tile

class Board():
    def __init__(self):
        self.width = 9
        self.height = 9
        self.board = self.init_board()

        return
    
    def __str__(self):
        for row in self.board:
            for tle in row:                
                print(tle, end=" ")
            print()
        return ""
    
    
    def init_board(self, n=9, m=9):
        """
        Fill an n x m board with mines. Default 9x9 board.
        Amount of mines is proportional to board size. 
        Returns the board.
        """
        
        arr = []
        for i in range(n):
            row = []
            for j in range(m):
                # initalize the tiles with value -2
                row.append(Tile(-2))
        
            arr.append(row)        
        
        # populate with mines
        board = Board.init_mines(arr)
        self.board = board
        
        # calculate values for non-mine tiles
        for i in range(self.width):
            for j in range(self.height):
                self.board[i][j].value = self.calc_tile_value(i, j)
                
        
        return board
        
        
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
            
            
    def calc_tile_value(self, posx, posy):
        """
        Return the number of bombs adjacent to this tile 
        given the x, y of the tile
        
        If the tile is a bomb we will return -1
        """
        assert(posx < self.width)
        assert(posy < self.height)
        
        tile = self.board[posx][posy]
        
        if (tile.bomb == True):
            return -1
        else:
            bcount = 0
            
            # check the eight tiles around this tile
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    
                    # indicies of the tile we are checking
                    checkx = posx + i
                    checky = posy + j
                    # skip out-of-bounds
                    if (checkx < 0 or checky < 0):
                        continue
                    if (checkx >= self.width or checky >= self.width):
                        continue
                    
                    # check for bomb here
                    if (self.board[checkx][checky].bomb == True):
                        bcount += 1
            
            return bcount
        
    def get_board(self):
        return self.board