from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import LIVE, LIVE_TYPE
class Live(PowerUp):
    def __init__(self):
        self.image = LIVE
        self.type = LIVE_TYPE
        super().__init__(self.image, self.type)