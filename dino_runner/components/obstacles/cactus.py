import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import ALL_CACTUS
class Cactus(Obstacle):
    Y_POS_CACTUS_SMALL = 325
    Y_POS_CACTUS_LARGE = 295

    def __init__(self):
        self.image = random.choice(ALL_CACTUS)
        super().__init__(self.image)
        if self.image == ALL_CACTUS[0] or self.image == ALL_CACTUS[1] or self.image == ALL_CACTUS[2]:
            self.rect.y = self.Y_POS_CACTUS_SMALL
        else: 
            self.rect.y = self.Y_POS_CACTUS_LARGE




