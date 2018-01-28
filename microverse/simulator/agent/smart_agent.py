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
    HealthEmmiter


class SmartAgent(Agent):
    def __init__(self, environment, parent_fitness=0, *args, **kwargs):
        super(SmartAgent, self).__init__(*args, **kwargs)
        self.collected_food = 0
        self.parent_fitness = parent_fitness
        self.sight = Sight(
            fov=math.sqrt(2) * math.pi / 6,
            ray_count=9,
            strength=125,
            environment=environment
        )
        self.brain = NeuralNetwork([10, 16, 2])
        navigator = Navigator(steering_magnitude=0.01)
        digestion = Digestion(environment)
        mobility = Mobility()
        fatigue = Fatigue()
        health_emmiter = HealthEmmiter()

        self.plug(self.sight, health_emmiter, self.brain, navigator)
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
        return self.time_alive
        # return self.health * (self.collected_food + self.parent_fitness)
