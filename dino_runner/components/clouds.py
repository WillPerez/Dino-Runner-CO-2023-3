import random
from dino_runner.utils.constants import CLOUD

class Cloud:
    X_POS_CLOUD = random.randint(1200, 1500)
    X_POS_CLOUD_2 = random.randint(1800, 2100)
    X_POS_CLOUD_3 = random.randint(2400, 2600)
    X_POS_CLOUD_4 = random.randint(2900, 3300)

    def __init__(self):
        self.x_pos_cloud = random.randint(1200, 1500)
        self.y_pos_cloud = 80
        self.game_speed_cloud = 20

        self.x_pos_cloud_2 = random.randint(1800, 2100)
        self.y_pos_cloud_2 = 55

        self.x_pos_cloud_3 = random.randint(2400, 2600)
        self.y_pos_cloud_3 = 95

        self.x_pos_cloud_4 = random.randint(2900, 3300)
        self.y_pos_cloud_4 = 85

    def draw(self, screen):
        image_width_cloud = CLOUD.get_width()
        screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -image_width_cloud and self.x_pos_cloud_4 <= -image_width_cloud:
            screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = self.X_POS_CLOUD
        self.x_pos_cloud -= self.game_speed_cloud


 
        screen.blit(CLOUD, (self.x_pos_cloud_2, self.y_pos_cloud_2))
        if self.x_pos_cloud_2 <= -image_width_cloud and self.x_pos_cloud_4 <= -image_width_cloud:
            screen.blit(CLOUD, (self.x_pos_cloud_2, self.y_pos_cloud_2))
            self.x_pos_cloud_2 = self.X_POS_CLOUD_2
        self.x_pos_cloud_2 -= self.game_speed_cloud



        screen.blit(CLOUD, (self.x_pos_cloud_3, self.y_pos_cloud_3))
        if self.x_pos_cloud_3 <= -image_width_cloud and self.x_pos_cloud_4 <= -image_width_cloud:
            screen.blit(CLOUD, (self.x_pos_cloud_3, self.y_pos_cloud_3))
            self.x_pos_cloud_3 = self.X_POS_CLOUD_3
        self.x_pos_cloud_3 -= self.game_speed_cloud



        screen.blit(CLOUD, (self.x_pos_cloud_4, self.y_pos_cloud_4))
        if self.x_pos_cloud_4 <= -image_width_cloud:
            screen.blit(CLOUD, (self.x_pos_cloud_4, self.y_pos_cloud_4))
            self.x_pos_cloud_4 = self.X_POS_CLOUD_4
        self.x_pos_cloud_4 -= self.game_speed_cloud