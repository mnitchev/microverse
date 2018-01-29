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
    def __init__(self, environment, parent_fitness=0, *args, **kwargs):
        super(SmartAgent, self).__init__(*args, **kwargs)
        self.collected_food = 0
        self.parent_fitness = parent_fitness
        self.sight = Sight(
            fov=math.pi / 3,
            ray_count=11,
            strength=700,
            environment=environment
        )
        self.brain = NeuralNetwork([12, 10, 7, 2])
        navigator = Navigator()
        digestion = Digestion(environment)
        mobility = Mobility()
        fatigue = Fatigue()
        health_emitter = HealthEmitter()

        self.plug(self.sight, health_emitter, self.brain, navigator)
        self.plug(digestion)
        self.plug(mobility)
        self.plug(fatigue)

    def level_up(self, amount):
        super(SmartAgent, self).level_up(amount)
        self.collected_food += 1

    def crossover(self, other):
        child = SmartAgent(self.sight.environment, self.fitness())
        child.brain = self.brain.crossover(other.brain)
        return child

    def fitness(self):
        return self.collected_food
        # return self.health * (self.collected_food + self.parent_fitness)
