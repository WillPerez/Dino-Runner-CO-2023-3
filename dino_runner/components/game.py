import pygame
import random

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD
from dino_runner.components.dinosaur import Dinosaur

class Game:
    X_POS_CLOUD = random.randint(900, 1100)
    X_POS_CLOUD_2 = random.randint(1300, 1600)
    X_POS_CLOUD_3 = random.randint(1800, 2000)
    X_POS_CLOUD_4 = random.randint(2200, 2600)
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        #____Clouds____
        self.x_pos_cloud = random.randint(900, 1100)
        self.y_pos_cloud = 80
        self.game_speed_cloud = 20

        self.x_pos_cloud_2 = random.randint(1300, 1600)
        self.y_pos_cloud_2 = 55

        self.x_pos_cloud_3 = random.randint(1800, 2000)
        self.y_pos_cloud_3 = 95

        self.x_pos_cloud_4 = random.randint(2200, 2600)
        self.y_pos_cloud_4 = 85

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.uptade(user_input)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_cloud_1()
        self.draw_cloud_2()
        self.draw_cloud_3()
        self.draw_cloud_4()
        self.player.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()


    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def draw_cloud_1(self):
        image_width_cloud = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -image_width_cloud and self.x_pos_cloud_4 <= -image_width_cloud:
            self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = self.X_POS_CLOUD
        self.x_pos_cloud -= self.game_speed_cloud

    def draw_cloud_2(self):
        image_width_cloud = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud_2, self.y_pos_cloud_2))
        if self.x_pos_cloud_2 <= -image_width_cloud and self.x_pos_cloud_4 <= -image_width_cloud:
            self.screen.blit(CLOUD, (self.x_pos_cloud_2, self.y_pos_cloud_2))
            self.x_pos_cloud_2 = self.X_POS_CLOUD_2
        self.x_pos_cloud_2 -= self.game_speed_cloud

    def draw_cloud_3(self):
        image_width_cloud = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud_3, self.y_pos_cloud_3))
        if self.x_pos_cloud_3 <= -image_width_cloud and self.x_pos_cloud_4 <= -image_width_cloud:
            self.screen.blit(CLOUD, (self.x_pos_cloud_3, self.y_pos_cloud_3))
            self.x_pos_cloud_3 = self.X_POS_CLOUD_3
        self.x_pos_cloud_3 -= self.game_speed_cloud

    def draw_cloud_4(self):
        image_width_cloud = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud_4, self.y_pos_cloud_4))
        if self.x_pos_cloud_4 <= -image_width_cloud:
            self.screen.blit(CLOUD, (self.x_pos_cloud_4, self.y_pos_cloud_4))
            self.x_pos_cloud_4 = self.X_POS_CLOUD_4
        self.x_pos_cloud_4 -= self.game_speed_cloud

