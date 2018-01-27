from ..utils import color
from .agent import Agent


class Food(Agent):
    def __init__(self, *args, **kwargs):
        Agent.__init__(self, *args, **kwargs)
        self.color = color(255, 255, 0)

    def level_down(self):
        self.health = 0
