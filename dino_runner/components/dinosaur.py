import pygame
from dino_runner.utils.constants import (RUNNING, DUCKING, JUMPING, DEAD, RUNNING_SHIELD, DUCKING_SHIELD, 
                                         JUMPING_SHIELD, DEFAULT_TYPE, SHIELD_TYPE, HAMMER_TYPE, LIVE_TYPE, RUNNING_HAMMER, 
                                         DUCKING_HAMMER, JUMPING_HAMMER)
from dino_runner.components.obstacles import obstacle
class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    Y_POS_DASH = 200
    JUMP_VEL = 8.5
    VEL_SUPER_DOWN = 0.5

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
        self.dino_dash = False
        self.jump_vel = self.JUMP_VEL
        self.dino_dead = False
        self.smash = False
        self.down = False
        self.vel_down = 0.8
        self.vel_super_down = 0.5
        self.shield = False
        self.hammer = False
        self.death = False
        self.time_up_power_up = 0
        self.time_dash = 0
        self.dash_time = 1000
        
    def uptade(self, user_input, game_speed):
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_super_jump:
            self.super_jump()
        if self.dino_dash:
            self.dash()
            game_speed = 40
        if self.death:
            self.dead()

            
        if user_input[pygame.K_DOWN] and not self.dino_jump and not self.dino_super_jump and not self.dino_dash:
            self.dino_run = False
            self.dino_jump = False  
            self.dino_duck = True
            self.dino_super_jump = False
            self.dino_dash = False

        elif user_input[pygame.K_UP] and not self.dino_jump and not self.dino_super_jump and not self.dino_dash:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False
            self.dino_super_jump = False
            self.down = False
            self.dino_dash = False
        
        elif user_input[pygame.K_SPACE] and not self.dino_jump and not self.dino_dash:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = False
            self.dino_super_jump = True
            self.down = False
            self.dino_dash = False

        elif user_input[pygame.K_RSHIFT] and not self.dino_jump and not self.dino_super_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = False
            self.dino_super_jump = False
            self.down = False
            self.dino_dash = True

        elif not self.dino_jump and not self.dino_super_jump :
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False
            self.dino_super_jump = False
            self.down = False
            self.dino_dash = False
        
        if user_input[pygame.K_DOWN]:
            self.down = True   

        if self.step_index >= 10:
            self.step_index = 0

        if self.shield:
            time_to_show = round((self.time_up_power_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show <0:
                self.reset()

        if self.hammer:
            time_to_show = round((self.time_up_power_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show <0:
                self.reset()

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
            if self.down:
                self.vel_super_down = 0.6
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= self.vel_super_down
            
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_super_jump = False
            self.jump_vel = self.JUMP_VEL
            self.vel_super_down = self.VEL_SUPER_DOWN

    def dead(self):
        if self.dino_duck:
            self.image = DEAD
            self.dino_rect = self.image.get_rect()
            self.dino_rect.y = self.Y_POS            
        self.image = DEAD
        self.dino_dead = True
        self.image = DEAD
        print("imagen muerto")
        
    def set_power_up(self, power_up):
        if power_up.type == SHIELD_TYPE:
            self.type = SHIELD_TYPE
            self.shield = True
            self.time_up_power_up = power_up.time_up
        if power_up.type == HAMMER_TYPE:
            self.type = HAMMER_TYPE
            self.hammer = True
            self.time_up_power_up = power_up.time_up
        if power_up.type == LIVE_TYPE:
            self.image = DEAD
            self.death = True
            print("debe morir")
            

    def reset(self):
        self.type = DEFAULT_TYPE
        self.shield = False
        self.hammer = False
        self.time_up_power_up = 0
        self.time_dash = 0

    def dash(self):                  
        self.image = self.duck_img[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DASH


