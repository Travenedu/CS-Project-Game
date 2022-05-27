import pygame, random
pygame.init()

from Fighter.constants import FPS, screen, WIDTH, back_ground
from Fighter.Drawer import Draw, Knight, Enemy, box_group

#caption And Icon
pygame.display.set_caption('Kings Run')

def main():
    running = True
    clock = pygame.time.Clock()
    
    move_left = False
    move_right = False
    score = 0
    high_score = 0
    floor_x_pos = 0
    game_over = False
    knight1 = Knight(200, 475, 3.5, 4.5)
    
    max_box = 9#10
    enemy_list = [1000, 1010, 600, 1100, 990, 800]
    
    last_enemy = pygame.time.get_ticks()

    while running:
        clock.tick(FPS)
        if game_over == False:
            screen.fill((0,90,0))
            enemy_timer = random.choice(enemy_list)
            #Floor
            floor_x_pos -= 1
            Draw.draw_floor(back_ground, floor_x_pos)
            if floor_x_pos <= -576:
                floor_x_pos = 0

            knight1.update_animation()
            knight1.knight_draw()
            
            box_group.update(knight1)
            if len(box_group) < max_box:
                if pygame.time.get_ticks() - last_enemy > enemy_timer:
                    box = Enemy(1200, 475, 5)
                    box_group.add(box)
                    last_enemy = pygame.time.get_ticks()

            if knight1.alive:
                if knight1.in_air:
                    knight1.update_action(1)#need jump animation
                elif move_left or move_right:
                    knight1.update_action(1)
                else:
                    knight1.update_action(1)
                knight1.moving(move_left, move_right)

            score += 0.10
            if game_over == False:
                Draw.score_display('main_game', score, high_score)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                #Knight Movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        move_left = True
                    if event.key == pygame.K_d:
                        move_right = True
                    if event.key == pygame.K_SPACE and knight1.alive:
                        knight1.jump = True
                    if event.key == pygame.K_ESCAPE:
                        running = False

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        move_left = False
                    if event.key == pygame.K_d:
                        move_right = False
            #Game over Mechanic
            if knight1.health == 0:
                game_over = True

            if game_over == True:
                high_score = Draw.update_score(score, high_score)
                Draw.score_display('game_over', score, high_score)

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        game_over = False
                        box_group.empty()
                        knight1 = Knight(200, 475, 3.5, 4.5)
                        score = 0.5
                        knight1.health = 100

        pygame.display.update()
    pygame.quit()
main()

