import pygame, os
import game_module as gm
import player, plates

class Game():
# ustawienia ekranu i gry
    pygame.display.set_caption('Dedal Maze')
    screen = pygame.display.set_mode(gm.SIZESCREEN, pygame.FULLSCREEN)
    screen.blit(gm.BACKGROUND, (0, 0))
    clock = pygame.time.Clock()

# centrowanie okna
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()

# konkretyzacja obiektów
    player = player.Player(gm.STAND_D)
    plate = plates.Plates(gm.BLACK, gm.SCALE, gm.ROAD)

# głowna pętla gry
    window_open = True
    while window_open:
        # pętla zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    window_open = False
            elif event.type == pygame.QUIT:
                window_open = False

    # rysowanie i aktualizacja obiektów
        plate.draw(screen)
        player.draw(screen)

    # aktualizacja okna pygame
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()