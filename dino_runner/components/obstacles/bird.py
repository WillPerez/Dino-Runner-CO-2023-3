import pygame
import random
from dino_runner.utils.constants import BIRD

class Bird:
    X_POS_BIRD = 1300
    def __init__(self):
        self.image = BIRD[0]
        self.rect = self.image.get_rect()
        self.y_pos_bird = 200
        self.y_pos_bird_random = random.choice((85, 200, 290))
        self.x_pos_bird = 1300
        self.step_index = 0
        self.game_speed_bird = 20
        
    def update(self, player):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.step_index += 0.5
        if self.step_index >= 10:
            self.step_index = 0
        if self.rect.colliderect(player.dino_rect):
            player.dino_dead = True

    def draw(self, screen):
        screen.blit(self.image, (self.x_pos_bird, self.y_pos_bird))
    ##def fly(self):
        image_width_bird = self.image.get_width()
        screen.blit(self.image, (self.x_pos_bird, self.y_pos_bird))
        if self.x_pos_bird <= -image_width_bird:
            screen.blit(self.image, (self.x_pos_bird, self.y_pos_bird))
            self.x_pos_bird = self.X_POS_BIRD
        self.x_pos_bird -= self.game_speed_bird





    