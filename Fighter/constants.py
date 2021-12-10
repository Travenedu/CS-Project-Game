import pygame

WIDTH, HEIGHT = 1200,800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
FPS = 60
Gravity = 0.75
#knight_image = pygame.transform.scale(pygame.image.load('assets/Knight.jpg'), (88, 50))
knightX, knightY = 370, 480

castle = pygame.image.load('assets/Castlevania_Harmony_of_Dissonance.jpg')
