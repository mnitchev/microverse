import math

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
    def __init__(self, environment, *args, **kwargs):
        super(SmartAgent, self).__init__(*args, **kwargs)

        self.sight = Sight(
            fov=math.pi / 2,
            ray_count=7,
            strength=250,
            environment=environment
        )
        self.brain = NeuralNetwork([7, 10, 1])
        navigator = Navigator(steering_magnitude=0.01)
        digestion = Digestion(environment)
        mobility = Mobility()
        fatigue = Fatigue()

        self.plug(self.sight, self.brain, navigator)
        self.plug(digestion)
        self.plug(mobility)
        self.plug(fatigue)

    def crossover(self, other):
        child = SmartAgent(self.sight.environment)
        child.brain = self.brain.crossover(other.brain)
        return child

    def fitness(self):
        return self.health
