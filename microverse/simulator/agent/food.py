from random import random as rand
from .agent import Agent
from ..plugins import Mobility
from ..utils import geometry

MAX_FOOD_HEALTH = 1


class Food(Agent):
    def __init__(self, *args, **kwargs):
        super(Food, self).__init__(*args, **kwargs)
        self.initial_size = self.size
        self.plug(Mobility())

    def update(self):
        super(Food, self).update()
        self.steer(rand() - 0.5)

    def intersect_ray(self, creature_position, sight_direction):
        center, radius = self.position.copy, self.size

        _, distance, intersection = geometry.ray_circle_intersect(
            (creature_position, sight_direction), (center, radius))

        return distance, intersection
