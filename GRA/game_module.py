import pygame, os

# okno główne
SIZESCREEN = WIDTH, HEIGHT = 1920, 1080
BACKGROUND = pygame.image.load(os.path.join('png', 'maze.png'))

# grafika postać
STAND_R = pygame.image.load(os.path.join('png', 'RIGHT.png'))
STAND_L = pygame.image.load(os.path.join('png', 'LEFT.png'))
STAND_U = pygame.image.load(os.path.join('png', 'UP.png'))
STAND_D = pygame.image.load(os.path.join('png', 'DOWN.png'))

# grafika platformy
SCALE = pygame.image.load(os.path.join('png', 'scale.png'))
ROAD = pygame.image.load(os.path.join('png', 'road.png'))
BLACK = pygame.image.load(os.path.join('png', 'black.png'))

