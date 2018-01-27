import math

from .agent import Agent
from ..utils import vec2
from ..plugins import \
    Sight, \
    NeuralNetwork, \
    Navigator, \
    Digestion, \
    Mobility


class SmartAgent(Agent):
    def __init__(self, environment, *args, **kwargs):
        super(SmartAgent, self).__init__(*args, **kwargs)

        sight = Sight(
            fov=math.pi / 2,
            ray_count=7,
            strength=50,
            environment=environment
        )
        brain = NeuralNetwork([7, 10, 2])
        navigator = Navigator(steering_magnitude=0.01)
        digestion = Digestion(environment=environment)
        mobility = Mobility()

        self.plug(sight, brain, navigator)
        self.plug(digestion)
        self.plug(mobility)