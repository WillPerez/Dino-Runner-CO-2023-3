import random
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.live import Live


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.shield_or_hammer = ["live"]
        self.random_power = None

    def update(self, game_speed, points, player):
        self.random_power = random.choice(self.shield_or_hammer)
        if len(self.power_ups) == 0 and points % 200 == 0 and self.random_power == "shield":
            self.power_ups.append(Shield())
        elif len(self.power_ups) == 0 and points % 200 == 0 and self.random_power == "hammer":
            self.power_ups.append(Hammer())
        elif len(self.power_ups) == 0 and points % 200 == 0 and self.random_power == "live":
            self.power_ups.append(Live())
                
        for power_up in self.power_ups:
            if power_up.used or power_up.rect.x < -power_up.rect.width:
                self.power_ups.remove(power_up)
            if power_up.used:
                player.set_power_up(power_up)
            power_up.update(game_speed, player)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)