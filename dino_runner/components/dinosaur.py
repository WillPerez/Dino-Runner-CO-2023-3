import pygame
from dino_runner.utils.constants import (RUNNING, DUCKING, JUMPING, DEAD, RUNNING_SHIELD, DUCKING_SHIELD, 
                                         JUMPING_SHIELD, DEFAULT_TYPE, SHIELD_TYPE, HAMMER_TYPE, RUNNING_HAMMER, 
                                         DUCKING_HAMMER, JUMPING_HAMMER)
from dino_runner.components.obstacles import obstacle
class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.run_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}
        self.duck_img = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
        self.jump_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
        self.type = DEFAULT_TYPE
        self.image = self.run_img[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.dino_super_jump = False
        self.jump_vel = self.JUMP_VEL
        self.dino_dead = False
        self.down = False
        self.vel_down = 0.8
        self.vel_super_down = 0.4
        
    def uptade(self, user_input):
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_super_jump:
            self.super_jump()
            
        if user_input[pygame.K_DOWN] and not self.dino_jump and not self.dino_super_jump:
            self.dino_run = False
            self.dino_jump = False  
            self.dino_duck = True
            self.dino_super_jump = False

        elif user_input[pygame.K_UP] and not self.dino_jump and not self.dino_super_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False
            self.dino_super_jump = False
            self.down = False
        
        elif user_input[pygame.K_SPACE] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = False
            self.dino_super_jump = True
            self.down = False

        elif not self.dino_jump and not self.dino_super_jump:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False
            self.dino_super_jump = False
            self.down = False
        
        if user_input[pygame.K_DOWN]:
            self.down = True   

        if self.step_index >= 10:
            self.step_index = 0

    def draw(self,screen):
        screen.blit(self.image, self.dino_rect)

    def run(self):
        self.image = self.run_img[self.type][0] if self.step_index < 5 else self.run_img[self.type][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def duck(self):
        self.image = self.duck_img[self.type][0] if self.step_index < 5 else self.duck_img[self.type][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img[self.type]
        if self.dino_jump:

            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= self.vel_down
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def super_jump(self):
        self.image = self.jump_img[self.type]
        if self.dino_super_jump:
           ## if self.down:
           ##     print("baje rapido")
           ##     self.vel_super_down = 1.2
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= self.vel_super_down
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_super_jump = False
            self.jump_vel = self.JUMP_VEL

    def dead(self):
        if self.dino_duck:
            self.dino_rect.y = self.Y_POS
            self.image = DEAD
        self.image = DEAD
        
    def set_power_up(self, power_up):
        if power_up.type == SHIELD_TYPE:
            self.type = SHIELD_TYPE
        if power_up.type == HAMMER_TYPE:
            self.type = HAMMER_TYPE
