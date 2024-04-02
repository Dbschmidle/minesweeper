"""
Tile class 

Tiles can have values, which represents the amount of bombs adjacent to the tile.
(The highest value a tile can have is eight, where the tile is surrounded on all sides 
by bombs).

A tile that contains a bomb will have a value of -1 

These values must be calculated after bomb initalization by the game engine.


"""

class Tile:
    def __init__(self, value):
        
        # we trust that the value argument is correct
        self.value = value
        
        self.visible = False 

        self.flagged = False
        
        self.bomb = False
    

    def __str__(self):
        if (self.value == 0):
            # zero value
            return " "
        
        if (self.value == -1):
            # bomb
            return "B"
        
        if (self.flagged == True):
            return "F"
        return str(self.value)
    
    
    def set_bomb(self):
        self.bomb = True
        #assert(self.value == -2)
        self.value = -1    
        
    
    