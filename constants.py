import pygame

WIDTH, HEIGHT = 1200,800

FPS = 60

spaceship = pygame.transform.scale(pygame.image.load('assets/tiny_ship.png'), (88, 50))
spaceshipcoordX, spaceshipcoordY = 370, 20

spaceman = pygame.transform.scale(pygame.image.load('assets/Spaceman.png'), (88, 50))
spacemancoordX, spacemancoordY = 370, 480