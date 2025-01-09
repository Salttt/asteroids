import pygame
from player import Player
from constants import * 

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    player = Player(SCREEN_HEIGHT/ 2, SCREEN_WIDTH / 2)

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        player.draw(screen)

        pygame.display.flip()
    
        dt = clock.tick()/1000
        
    

if __name__ == "__main__":
    main()


