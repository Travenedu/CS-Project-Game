import pygame
from .constants import screen, Gravity, game_font, WIDTH


class Draw:
    def __init__(self, postionx, positiony):
        self.postionX = postionx
        self.postionY = positiony

    def draw_floor(back_ground, floor_x_pos):
        screen.blit(back_ground, (floor_x_pos, -23))
        screen.blit(back_ground, (floor_x_pos + 576, -23))

    def score_display(game_state, score, high_score):
        if game_state == 'main_game':
            score_surface = game_font.render(str(int(score)),True,(255,255,255))
            score_rect = score_surface.get_rect(center = (970, 50))
            screen.blit(score_surface, score_rect)
        if game_state == 'game_over':
            score_surface = game_font.render(f'Score: {int(score)}',True,(255,255,255))
            score_rect = score_surface.get_rect(center = (900, 50))
            screen.blit(score_surface, score_rect)

            high_score_surface = game_font.render(f'High score: {int(high_score)}',True,(255,255,255))
            high_score_rect = high_score_surface.get_rect(center = (300, 50))
            Again_score_surface = game_font.render('Press A to Restart', True, (255,255,255))
            Again_score_rect = high_score_surface.get_rect(center = (550, 100))
            
            screen.blit(high_score_surface, high_score_rect)
            screen.blit(Again_score_surface, Again_score_rect)

    def update_score(score, high_score):
        if score > high_score:
            high_score = score
        return high_score 

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.Enemy_image =  pygame.image.load('assets/box.png')
        self.rect = self.Enemy_image.get_rect()
        self.rect.center = (x, y)

    def moving(self):
        changeinX = 0
        changeinY = 0
        changeinX = -self.speed
        self.flip = True
        self.direction = -1
    
        #might have to moved
        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

        self.rect.x += changeinX
        self.rect.y += changeinY

    def update(self, knight):
        self.moving()

        if pygame.sprite.spritecollide(knight, box_group, False):
            if knight.alive:
                knight.health = 0
        screen.blit(self.Enemy_image, self.rect)


box_group = pygame.sprite.Group()
class Knight(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.speed = speed
        self.direction = 1
        self.health = 100
        self.velocity_y = 0
        self.jump = False
        self.in_air = True
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        animation_types = ['Idle_stance', 'Staff_Fast_Run', "Dash", "Dash_back", "Fall_Flat", "Front_Flip"]
        
        animation_file_numbers = {'Idle_stance': 10, 'Staff_Fast_Run': 6, "Dash": 5, "Dash_back": 1, "Fall_Flat": 6, "Front_Flip": 8}

        for animation in animation_types:
            temp_animation_list = []

            number_of_frames = animation_file_numbers[animation]

            for i in range(number_of_frames):
                knight = pygame.image.load(f'assets/{animation}/{i}.png')
                knight = pygame.transform.scale(knight, (int(knight.get_width() * scale), int(knight.get_height() * scale)))
                temp_animation_list.append(knight)
            self.animation_list.append(temp_animation_list)

        self.knight_image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect(0,0, 35, 90)
        self.rect.center = (x, y)

    def moving(self, move_left, move_right):
        changeinX = 0
        changeinY = 0
        if move_left:
            changeinX = -self.speed
            self.flip = True
            self.direction = -1
        if move_right:
            changeinX = self.speed
            self.flip = False
            self.direction = 1

        if self.jump == True and self.in_air == False:
            self.velocity_y = -13
            self.jump = False
            self.in_air = True

        self.velocity_y += Gravity
        if self.velocity_y > 10:
            self.velocity_y = 10
        changeinY  += self.velocity_y

        if self.rect.bottom + changeinY > 793:
            changeinY = 793 - self.rect.bottom
            self.in_air = False

        self.rect.x += changeinX
        self.rect.y += changeinY    

    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        self.knight_image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

        if self.frame_index  >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()



    def knight_draw(self):
        screen.blit(pygame.transform.flip(self.knight_image, self.flip, False), (self.rect.x -80, self.rect.y - 28))
    
