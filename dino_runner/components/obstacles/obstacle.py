import pygame
from dino_runner.utils.constants import SCREEN_WIDTH, ALL_CACTUS, BIRD

class Obstacle:
    def __init__(self, image):
        self.image = image  
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.step_index = 0

    def update(self, game_speed, player):
        
        self.rect.x -= game_speed

        if self.rect.colliderect(player.dino_rect):
            
            
            if not player.shield and not player.hammer:

                player.dino_dead = True
                player.dead()

            if player.hammer:
                player.smash = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    

