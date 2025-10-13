import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0 # delta time

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # return just exits the function main()
            
        pygame.Surface.fill(screen, (0,0,0)) # fills screen variable, then 0,0,0 is the colour
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
