import pygame, numpy as np
import game_module as gm
import plate, player

class Plates(pygame.sprite.Sprite):
    def __init__(self, black, scale, road):
        super().__init__()
        self.black = black
        self.rect = self.black
        self.scale = scale
        self.road = road
        self.player_index = (0,1)
        self.plate_box = np.array([
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#0
            [0,0,0,0,1,0,1,1,1,0,0,0,0,1,0,0,0,1],#1
            [1,1,1,0,1,0,0,0,0,0,1,1,0,1,1,1,0,1],#2
            [1,1,1,0,0,0,1,1,1,0,0,1,0,0,0,0,0,1],#3
            [1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1],#4
            [1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1],#5
            [1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,0,1],#6
            [1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1],#7
            [1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1],#8
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1] #9
        ])
        self.plates = np.empty_like(self.plate_box,plate.Plate)

        k = 0
        for i in range(420, 1500, 60):
            w = 0
            for j in range(180, 780, 60):
                if(self.plate_box[w,k]==1):
                    self.plates[w,k] = plate.Plate("black", i, j)
                else:
                    self.plates[w,k] = plate.Plate("yellow", i, j)
                w = w + 1
            k = k + 1

    def update(self):
        player.rect.x = self.plates[self.player_index].x
        player.rect.y = self.plates[self.player_index].y


    def draw(self, surface):
        for i in range(10):
            for j in range(18):
                self.plates[i][j].draw(surface)



