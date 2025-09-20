import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

updatable_group = pygame.sprite.Group()
drawable_group = pygame.sprite.Group()
asteroids_group = pygame.sprite.Group()
shots_group = pygame.sprite.Group()

Player.containers = (updatable_group, drawable_group)
Asteroid.containers = (updatable_group, drawable_group, asteroids_group)
AsteroidField.containers = (updatable_group,)
Shot.containers = (updatable_group, drawable_group, shots_group)

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0), rect=None, special_flags=0)
        for sprite in drawable_group:
            sprite.draw(screen)
        for sprite in updatable_group:
            sprite.update(dt)
        for asteroid in asteroids_group:
            if player.collision(asteroid):
                print("Game over!")
                import sys
                sys.exit()
            for bullet in shots_group:
                if asteroid.collision(bullet):
                    bullet.kill()
                    asteroid.split()
        dt = Clock.tick(60) / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
    

 
