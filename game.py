import pygame
pygame.init()

from Fighter.constants import FPS, screen, WIDTH
from Fighter.Drawer import Draw, Knight


#caption And Icon
pygame.display.set_caption('Kings Fight')

def main():
    running = True
    clock = pygame.time.Clock()
    move_left = False
    move_right = False

    knight1 =  Knight(200, 200, 3, 5)



    while running:
        clock.tick(FPS)

        screen.fill((0,0,0))
        pygame.draw.line(screen, (255,0,0), (0, 300), (WIDTH, 300))

        knight1.update_animation()
        knight1.knight_draw()

        if knight1.alive:
            if knight1.in_air:
                knight1.update_action(1)#need jump animation
            elif move_left or move_right:
                knight1.update_action(1)
            else:
                knight1.update_action(0)
            knight1.moving(move_left, move_right)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    move_left = True
                if event.key == pygame.K_d:
                    move_right = True
                if event.key == pygame.K_w and knight1.alive:
                    knight1.jump = True
                if event.key == pygame.K_ESCAPE:
                    running = False      

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    move_left = False
                if event.key == pygame.K_d:
                    move_right = False




        #Draw.castle_draw()
        #Knight.knight_draw(knightX, knightY)

        pygame.display.update()

    pygame.quit()

main()

