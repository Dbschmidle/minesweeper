"""
Game class.

"""
import pygame
from board import Board
from tile import Tile

class Game:
    def __init__(self):
        self.board = Board()
        
        
    def start(self):
        pygame.init()
        
        running = True 
        screen = pygame.display.set_mode((800,800))
        
        while running: 
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
            self.draw()
            pygame.display.flip()
            
        pygame.quit()
        
        
    def draw(self):
        # coordinates to place tiles on screen
        cords = (0, 0)
        
        for row in self.board:
            for tle in row:
                rect = pygame.Rect(cords, (50,50))
                cords = cords[0] + 50, cords[1]
                
            cords = (0, cords[1] + 50)