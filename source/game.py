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
        
    
        
    def start(self):
        running = True 
        
        while running: 
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
            self.screen.fill("white")
            self.draw()
            pygame.display.flip()
            
        pygame.quit()
        
        
    def draw(self):
        # coordinates to place tiles on screen
        cords = (0, 0)
        
        for row in self.board.get_board():
            for tle in row:
                rect = pygame.Rect(cords, self.tileSize)
                image = self.images["empty-block"]
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
            