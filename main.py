import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # return just exits the function main()
        pygame.Surface.fill(screen, (0,0,0)) # fills screen variable, then 0,0,0 is the colour
        pygame.display.flip()


if __name__ == "__main__":
    main()
