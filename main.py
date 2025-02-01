import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  # create a clock object

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0  # variable that stores our delta time

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for asteroid in asteroids:
            # print(f"Checking collision with asteroid at {asteroid.position}")
            if player.check_collision(asteroid):
                # print(f"Collision dectected! Player at {player.position}, asteroid at {asteroid.position}")
                print("Game over!")
                sys.exit()
        screen.fill((0, 0, 0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = (clock.tick(60) / 1000)  # limit frame per second to 60 and gets delta time in seconds


if __name__ == "__main__":
    main()
