import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, player_image):
        super().__init__()
        self.image = player_image
        self.x = 0
        self.y = 0
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect)