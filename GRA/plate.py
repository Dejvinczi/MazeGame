import pygame, game_module as gm

class Plate(pygame.sprite.Sprite):
    def __init__(self,type,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.type = type

    def draw(self, surface):
        if(self.type == "black"):
            surface.blit(gm.BLACK, (self.x, self.y))
        elif(self.type == "yellow"):
            surface.blit(gm.ROAD, (self.x, self.y))
