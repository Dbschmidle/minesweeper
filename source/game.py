"""
Game class.

"""
import pygame
import os
from board import Board
from tile import Tile

class Game:
    def __init__(self):
        self.board = Board()
        pygame.init()
        self.screen = pygame.display.set_mode((500,500))
        # size of the tiles equal to size of screen / # tiles
        self.tileSize = (500 // self.board.height, 500 // self.board.width)
        self.load_images()
        
        self.first_click = False
    
        
    def start(self):
        running = True 
        
        while running: 
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    # get state of mouse buttons 
                    rightclick = pygame.mouse.get_pressed(num_buttons=3)[2]    
                    self.handle_click(pygame.mouse.get_pos(), rightclick)
            
            self.screen.fill("white")
            self.draw()
            pygame.display.flip()
            
        pygame.quit()
        
        
    def draw(self):
        """
        Draw the current board.
        """
        
        # coordinates to place tiles on screen
        cords = (0, 0)
        
        for row in self.board.get_board():
            for tle in row:
                rect = pygame.Rect(cords, self.tileSize)
                image = self.find_image(tle)
                self.screen.blit(image, cords)
                cords = cords[0] + self.tileSize[0], cords[1]
                
            cords = (0, cords[1] + self.tileSize[1])
            
            
    def load_images(self):
        """
        All images must be preloaded by pygame before using 
        """
        self.images = {}
        
        dir = os.listdir("source/images")
        
        for filename in dir:
            img = pygame.image.load(r"source/images/"+filename)
            img = pygame.transform.scale(img, self.tileSize)
            self.images[filename.split(".")[0]] = img
            
        print(self.images)
            
            
    def find_image(self, tile):
        """
        Return the image associated with the tile from self.images
        """
        tilestr = str(tile)

        if (tile.flagged == True):
            return self.images["flag"]

        if (tile.visible == False):
            # tile not visible to user yet
            return self.images["empty-block"]
        
        if (tilestr == "B"):
            return self.images["bomb-at-clicked-block"]    
        
        if (tilestr == " "):
            return self.images["0"]
            
        # return the number
        return self.images[tilestr]
        
        
    def handle_click(self, pos, rightclick):
        """
        Converts position into index on board.
        If rightclick is true, set the tile to a flag 
        """
        index = ( pos[1] // self.tileSize[1], pos[0] // self.tileSize[0] )
        
        tile = self.board.get_tile(index)
        
        if (rightclick):
            
            # user cannot flag visible tiles 
            if (tile.visible == True):
                return
            
            if (tile.flagged == True):
                # tile already flagged, unflag it
                self.board.unflag_tile(tile)
            else:
                self.board.flag_tile(tile)
        
        else:
            # leftclick
            if (tile.bomb == True):
                
                if(self.first_click == False):
                    # user has not clicked, this cannot be a bomb
                    # reset the board
                    self.board = Board()
                    return
                
                self.board.set_visible(tile)
                self.game_lost()
            
            
            self.first_click = True
            
            self.board.set_visible(tile)
            self.board.propogate_visible(tile)
            
            
    def game_lost(self):
        # set all the bombs visible
        for row in self.board.get_board():
            for tle in row:
                if (tle.bomb == True):
                    self.board.set_visible(tle)
        