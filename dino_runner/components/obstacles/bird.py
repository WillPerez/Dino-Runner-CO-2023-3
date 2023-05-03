import pygame
import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    X_POS_BIRD = 1200
    Y_POS_BIRD = [260, 220, 170]
    def __init__(self):
        self.image = BIRD[0]
        super().__init__(self.image)
        self.rect.y = random.choice(self.Y_POS_BIRD)
    """   self.x_pos_bird = 1200
        self.step_index = 0
        self.game_speed_bird = 20
        
    def update(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.step_index += 0.5
        if self.step_index >= 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x_pos_bird, self.y_pos_bird))
    ##def fly(self):
        image_width_bird = self.image.get_width()
        screen.blit(self.image, (self.x_pos_bird, self.y_pos_bird))
        if self.x_pos_bird <= -image_width_bird:
            screen.blit(self.image, (self.x_pos_bird, self.y_pos_bird))
            self.x_pos_bird = self.X_POS_BIRD
        self.x_pos_bird -= self.game_speed_bird
"""




    