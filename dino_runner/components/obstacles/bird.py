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

    def update(self, game_speed, player):
        if self.image in BIRD:
            self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
            self.step_index += 0.5
            if self.step_index >= 10:
                self.step_index = 0
        super().update(game_speed, player)
        