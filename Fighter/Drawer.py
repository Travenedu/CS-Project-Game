import pygame
from .constants import screen, castle, Gravity

class Draw:
    def __init__(self, postionx, positiony):
        self.postionX = postionx
        self.postionY = positiony

    def castle_draw():
        screen.blit(castle, (0,-300))


class Knight(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.speed = speed
        self.direction = 1
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
        self.rect = self.knight_image.get_rect()
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
            self.velocity_y = -11
            self.jump = False
            self.in_air = True

        self.velocity_y += Gravity
        if self.velocity_y > 10:
            self.velocity_y = 10
        changeinY  += self.velocity_y

        if self.rect.bottom + changeinY > 318:
            changeinY = 318 - self.rect.bottom
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
        screen.blit(pygame.transform.flip(self.knight_image, self.flip, False), self.rect)
    
