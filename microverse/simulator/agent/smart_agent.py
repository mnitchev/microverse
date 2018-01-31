import math
from random import random as rand

from .agent import Agent
from ..utils import vec2
from ..plugins import \
    Sight, \
    NeuralNetwork, \
    Navigator, \
    Digestion, \
    Mobility, \
    Fatigue


class SmartAgent(Agent):
    def __init__(self, ray_count, strength, fov, environment, nn, *args):
        super(SmartAgent, self).__init__(*args)
        self.collected_food = 0
        self.sight = Sight(
            fov=fov,
            ray_count=ray_count,
            strength=strength,
            environment=environment
        )
        self.brain = NeuralNetwork([self.sight.ray_count] + nn + [2])
        navigator = Navigator()
        digestion = Digestion(environment)
        mobility = Mobility()
        fatigue = Fatigue()

        self.plug(self.sight, self.brain, navigator)
        self.plug(digestion)
        self.plug(mobility)
        self.plug(fatigue)

    def apply(self, sight, ):
        self.sight = Sight(*args)

    def level_up(self, amount):
        super(SmartAgent, self).level_up(amount)
        self.collected_food += 1

    def fitness(self):
        return self.collected_food
