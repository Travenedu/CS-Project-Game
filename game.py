import pygame
pygame.init()

from constants import WIDTH, HEIGHT


screen = pygame.display.set_mode([WIDTH, HEIGHT])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0,0,0))

    pygame.draw.circle(screen, (0,0,255), (250,250), 75)

    pygame.display.flip()

pygame.quit()
