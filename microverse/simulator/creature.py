from .vec2 import vec2
from .agent import Agent


class Creature(Agent):
    def __init__(self, *args, **kwargs):
        super(Creature, self).__init__(*args, **kwargs)
