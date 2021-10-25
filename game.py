import pygame
pygame.init()

from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, K_SPACE, K_ESCAPE)
from constants import WIDTH, HEIGHT, spaceship, spaceman, FPS

screen = pygame.display.set_mode([WIDTH, HEIGHT])
#testing drawing
def spaceship_draw(positionx, positiony):
    screen.blit(spaceship, (positionx, positiony))

def spaceman_draw(positionx, positiony):
    screen.blit(spaceman, (positionx, positiony))

#caption And Icon
pygame.display.set_caption('Space Jump')
pygame.display.set_icon(spaceship)



def main():
    spaceshipcoordX, spaceshipcoordY = 370, 20
    spacemancoordX, spacemancoordY = 370, 480
    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False          
            
                if event.key == K_RIGHT:
                    spacemancoordX = spacemancoordX + 30
            
                if event.key == K_LEFT:
                    spacemancoordX = spacemancoordY - 30

                if event.key == K_UP:
                    spacemancoordY = spacemancoordY - 30
            
                if event.key == K_SPACE:
                    pass
                    #spacemancoordY = spacemancoordY - 30

                if event.key == K_DOWN:
                    spacemancoordY = spacemancoordY + 30

            spaceshipcoordX = spaceshipcoordX + 1


        screen.fill((0,0,0))

        spaceship_draw(spaceshipcoordX, spaceshipcoordY)
        spaceman_draw(spacemancoordX, spacemancoordY)
        pygame.display.update()
        #pygame.display.flip()

    pygame.quit()

main()

