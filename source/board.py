import random
from tile import Tile

class Board():
    def __init__(self):
        self.width = 9
        self.height = 9
        self.board = self.init_board()

        return
    
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
                # initalize the tiles with value -2 and position
                row.append(Tile(-2, (i, j)))
        
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
    
    def get_tile(self, index):
        """
        Returns the tile at index (x, y)
        """
        if (index[0] >= self.width or index[0] < 0):
            return
        if (index[1] >= self.height or index[1] < 0):
            return
        
        return self.board[index[0]][index[1]]
        
    
    def flag_tile(self, tile):
        tile.flagged = True
    
    def unflag_tile(self, tile):
        tile.flagged = False
        
        
    def set_visible(self, tile):
        """
        Set the tile visible.             
        """
        tile.visible = True
        
        
    def propogate_visible(self, tile):
        """
        In minesweeper, adjacent tiles to the one clicked will also become visible
        if they are not a bomb.
        """
        
        # check all adjacent tiles, if they are not a bomb, make them visible
        adj_tiles = self.get_adjacent_tiles(tile)
        
        for adj_tile in adj_tiles:
            if (adj_tile.bomb == False):
                # set this tile visible and propogate new tile
                if (adj_tile.visible == True):
                    # skip if already visible
                    continue
                
                self.set_visible(adj_tile)
                self.propogate_visible(adj_tile)
        
        
    def get_adjacent_tiles(self, tile):
        """
        Returns a list of all the adjacent tiles.
        Adjacent tiles include diagonal tiles.
        """
        adj = []
        tilepos = [tile.pos[0], tile.pos[1]]
        for i in range(-1, 2, 1):
            
            tilepos[0] = tilepos[0] + i
            
            for j in range(-1, 2, 1):
                if ( i == 0 and j == 0):
                    # skip tile
                    continue
                
                tilepos[1] = tilepos[1] + j
                
                if (self.index_in_scope(tilepos)):
                    # tile in bounds
                    adj.append(self.get_tile(tilepos))
                    
        return adj
                    
                

    def index_in_scope(self, index):
        """
        Checks if a tuple index (x, y) is in the scope of the board
        Returns a boolean value 
        """
        if (index[0] >= self.width or index[0] < 0):
            return False
        if (index[1] >= self.height or index[1] < 0):
            return False
        return True