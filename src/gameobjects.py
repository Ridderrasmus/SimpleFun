import pygame

class Button:
    x = 0
    y = 0
    width = 0
    height = 0
    
    
    def __init__(self, pos=(), size=(), colour=(255, 0, 0)):
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]
        self.height = size[1]
        self.colour = colour
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))