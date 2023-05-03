import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

class ObstacleManager:
    def __init__(self):
        self.obstacles =[]
        self.random_obstacles = ["cactus", "cactus", "cactus", "bird"]
        self.random_obstacle = None

    def update(self, game_speed, player):
        self.random_obstacle = random.choice(self.random_obstacles)
        if len(self.obstacles) == 0 and self.random_obstacle == "cactus":
            self.obstacles.append(Cactus())

        if len(self.obstacles) == 0 and self.random_obstacle == "bird":
            self.obstacles.append(Bird())

        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                 self.obstacles.remove(obstacle)
            obstacle.update(game_speed, player)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)