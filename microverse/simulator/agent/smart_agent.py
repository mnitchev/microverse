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
    def __init__(
        self, ray_count, strength, fov,
        environment, nn, parents=[None, None], *args
    ):
        super(SmartAgent, self).__init__(*args)
        self.collected_food = 0
        self.focus = False
        self.sight = Sight(
            fov=fov,
            ray_count=ray_count,
            strength=strength,
            environment=environment
        )
        self.brain = NeuralNetwork([self.sight.ray_count] + nn + [5])
        self.parents = parents
        navigator = Navigator()
        digestion = Digestion(environment)
        mobility = Mobility()
        fatigue = Fatigue()

        self.plug(self.sight, self.brain, navigator)
        self.plug(digestion)
        self.plug(mobility)
        self.plug(fatigue)

    def level_up(self, amount):
        super(SmartAgent, self).level_up(amount)
        self.collected_food += 1

    def fitness(self):
        return self.collected_food

    def render(self, renderer):
        for i in range(len(self.parents)):
            if self.parents[i] is not None:
                renderer.line(
                    self.position.x, self.position.y,
                    self.parents[i].position.x, self.parents[i].position.y,
                    fill='#222'
                )
                if self.parents[i].is_dead():
                    self.parents[i] = None

        if self.focus:
            renderer.arc(
                self.position.x, self.position.y,
                self.size,
                outline='#0f6',
                width=5
            )

        super(SmartAgent, self).render(renderer)
