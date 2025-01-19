import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from player import Player
from shot import Shot
from constants import * 

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    player = Player(SCREEN_HEIGHT/ 2, SCREEN_WIDTH / 2)
    asteroid_field = AsteroidField()



    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for sprite in updatable:
            sprite.update(dt)
        
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                sys.exit()

            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
    
        dt = clock.tick(60)/1000



    

if __name__ == "__main__":
    main()


