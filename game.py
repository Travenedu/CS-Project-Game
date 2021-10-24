import pygame
pygame.init()

from constants import WIDTH, HEIGHT, spaceship, FPS

screen = pygame.display.set_mode([WIDTH, HEIGHT])

#testing drawing
def spaceship_draw():
    screen.blit(spaceship, (370, 480))

#caption And Icon
pygame.display.set_caption('Space Jump')
pygame.display.set_icon(spaceship)

def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0,0,0))

        spaceship_draw()

        pygame.display.flip()

    pygame.quit()

main()