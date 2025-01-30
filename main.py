import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  # create a clock object

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0  # variable that stores our delta time

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        screen.fill((0, 0, 0))
        
        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)  # limit frame per second to 60 and gets delta time in seconds


if __name__ == "__main__":
    main()
