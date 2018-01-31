import math

from .agent import Agent
from ..utils import vec2
from ..plugins import \
    Sight, \
    NeuralNetwork, \
    Navigator, \
    Digestion, \
    Mobility, \
    Fatigue, \
    HealthEmitter


class SmartAgent(Agent):
    def __init__(self, environment, *args, **kwargs):
        super(SmartAgent, self).__init__(*args, **kwargs)
        self.collected_food = 0
        self.sight = Sight(
            fov=math.pi / 2,
            ray_count=8,
            strength=500,
            environment=environment
        )
        self.brain = NeuralNetwork([8, 16, 3])
        navigator = Navigator()
        digestion = Digestion(environment)
        mobility = Mobility()
        fatigue = Fatigue()
        health_emitter = HealthEmitter()

        self.plug(self.sight, self.brain, navigator)
        self.plug(digestion)
        self.plug(mobility)
        self.plug(fatigue)

    def level_up(self, amount):
        super(SmartAgent, self).level_up(amount)
        self.collected_food += 1

    def crossover(self, other):
        child = SmartAgent(self.sight.environment)
        child.brain = self.brain.crossover(other.brain)
        return child

    def fitness(self):
        return self.collected_food
        # return self.health * (self.collected_food + self.parent_fitness)
