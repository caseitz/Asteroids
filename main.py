import pygame
from constants import *
from player import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print(f'''Starting Asteroids!
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}''')
    clock = pygame.time.Clock() 
    dt = 0

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2

    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 1))

        player.draw(screen)

        pygame.display.flip()

        clock.tick(60)

        dt = (clock.tick())/1000

        





if __name__ == "__main__":
    main()