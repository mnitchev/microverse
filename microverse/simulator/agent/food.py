from ..utils import color, geometry
from .agent import Agent


class Food(Agent):
    def __init__(self, *args, **kwargs):
        super(Food, self).__init__(*args, **kwargs)
        self.color = color(255, 255, 0)

    def level_down(self):
        self.health = 0

    def intersect_ray(self, creature_position, sight_direction):
        center, radius = self.position.copy, self.size

        _, distance, intersection = geometry.ray_circle_intersect(
            (creature_position, sight_direction), (center, radius))

        return distance, intersection
