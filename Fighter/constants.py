import pygame

WIDTH, HEIGHT = 1200,800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
FPS = 60
Gravity = 0.75
#knight_image = pygame.transform.scale(pygame.image.load('assets/Knight.jpg'), (88, 50))
knightX, knightY = 370, 480


background = pygame.image.load('assets/background.png')
back_ground = pygame.transform.scale(background, (int(background.get_width() * 13), int(background.get_height() * 13)))
game_font = pygame.font.Font('assets/04B_19.ttf',40)