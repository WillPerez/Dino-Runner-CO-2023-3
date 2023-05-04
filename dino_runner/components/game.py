import pygame
import random

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_mannager import ObstacleManager
from dino_runner.components.clouds import Cloud
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components import text_utils

class Game:
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = False
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.cloud = Cloud()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.death_count = 0
        self.speed_turbo = self.game_speed * 2
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.color_sky = self.WHITE
        self.time_sky = self.points
        self.list_colors = [self.BLACK, self.WHITE]


    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            if event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset_game()

    def update(self):
        if self.playing:
            self.points += 1
            user_input = pygame.key.get_pressed()
            self.player.uptade(user_input, self.game_speed)
            self.obstacle_manager.update(self.game_speed, self.player)
            self.power_up_manager.update(self.game_speed, self.points, self.player)
            if self.player.dino_dead:
               self.player.dead()
               pygame.time.delay(500)
               self.playing = False
               self.death_count += 1
            if self.player.dino_dash:
                self.game_speed = self.speed_turbo
            else: self.game_speed = 20
            if self.points % 200 == 0:
                self.color_sky = random.choice(self.list_colors)
            
            
    def draw(self):
        if self.playing:
            self.clock.tick(FPS)
            self.screen.fill(self.color_sky)
            self.draw_background()
            self.cloud.draw(self.screen)
            self.player.draw(self.screen)
            self.obstacle_manager.draw(self.screen)
            ##self.bird.draw(self.screen)
            self.power_up_manager.draw(self.screen)
            self.draw_score()
        else:
            self.draw_menu()
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

    def draw_score(self):
        score, score_text = text_utils.get_message('points: ' + str(self.points), 20, 1000, 40)
        self.screen.blit(score, score_text)
    
    def draw_menu(self):
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        if self.death_count == 0:
            text, text_rect = text_utils.get_message('Pess Any Key To Start', 30, height= SCREEN_HEIGHT //3)
            self.screen.blit(text, text_rect)
            controls, controls_rect = text_utils.get_message('Controls:', 30, height= SCREEN_HEIGHT //2 - 30)
            self.screen.blit(controls, controls_rect)
            controls, controls_rect = text_utils.get_message('^ : ' + 'jump', 20, height= SCREEN_HEIGHT //2 + 10)
            self.screen.blit(controls, controls_rect)
            controls, controls_rect = text_utils.get_message('down : ' + 'Duck', 20, height= SCREEN_HEIGHT //2 + 40)
            self.screen.blit(controls, controls_rect)
            controls, controls_rect = text_utils.get_message('Space : ' + 'Super Jump', 20, height= SCREEN_HEIGHT //2 + 70)
            self.screen.blit(controls, controls_rect)
            controls, controls_rect = text_utils.get_message('Shilft : ' + 'Dash', 20, height= SCREEN_HEIGHT //2 + 100)
            self.screen.blit(controls, controls_rect)
            power, power_rect = text_utils.get_message('Powers', 30, height= SCREEN_HEIGHT //2 + 130)
            self.screen.blit(power, power_rect)
            power, power_rect = text_utils.get_message('Shield : ' + 'invulnerability', 20, height= SCREEN_HEIGHT //2 + 160)
            self.screen.blit(power, power_rect)
            power, power_rect = text_utils.get_message('Hammer : ' + 'destroy obstacles', 20, height= SCREEN_HEIGHT //2 + 190)
            self.screen.blit(power, power_rect)
            power, power_rect = text_utils.get_message('black heart : ' + 'avoid it, it will kill you', 20, height= SCREEN_HEIGHT //2 + 220)
            self.screen.blit(power, power_rect)
            
            
        else:
            text,text_rect = text_utils.get_message('Press Any Key To Start', 30)
            score, score_rect = text_utils.get_message('your score: ' + str(self.points), 30, height= SCREEN_HEIGHT //2 + 50)
            self.screen.blit(text,text_rect)
            self.screen.blit(score, score_rect)
    def reset_game(self):
        self.game_speed = 20
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.color_sky = self.WHITE

            
    