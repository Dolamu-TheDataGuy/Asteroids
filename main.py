import pygame
from constants import *


def main():
    pygame.init()
    clock = pygame.time.Clock()  # create a clock object
    dt = 0  # variable that stores our delta time
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()
        dt = (
            clock.tick(60) / 1000
        )  # limit frame per second to 60 and gets delta time in seconds


if __name__ == "__main__":
    main()
