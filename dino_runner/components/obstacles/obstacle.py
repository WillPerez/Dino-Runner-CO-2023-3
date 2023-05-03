import pygame
from dino_runner.utils.constants import SCREEN_WIDTH, ALL_CACTUS, BIRD

class Obstacle:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.step_index = 0

    def update(self, game_speed, player):
        
        if self.image == ALL_CACTUS:
            self.rect.x -= game_speed
        self.rect.x -= game_speed

        if self.image == BIRD:
            self.image = BIRD[0], print("pajaro") if self.step_index < 5 else BIRD[1]
            self.step_index += 0.5
            if self.step_index >= 10:
                print("reseteos")
                self.step_index = 0

        if self.rect.colliderect(player.dino_rect):
            player.dino_dead = True
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    

