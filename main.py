import pygame
from constants import *
from player import *
from circleshape import *

updatable_group = pygame.sprite.Group()
drawable_group = pygame.sprite.Group()
Player.containers = (updatable_group, drawable_group)

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0), rect=None, special_flags=0)
        for player in drawable_group:
            player.draw(screen)
        for player in updatable_group:
            player.update(dt)
        dt = Clock.tick(60) / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
    

 
