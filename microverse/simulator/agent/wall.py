import math
from .agent import Agent
from ..utils import geometry


class Wall(Agent):
    def __init__(self, direction, *args, **kwargs):
        super(Wall, self).__init__(*args, **kwargs)
        self.direction = direction
        self.health = math.inf

    def intersect_ray(self, creature_position, sight_direction):
        sight_ray = creature_position, sight_direction.add(sight_direction)
        direction = self.direction.copy.scale(self.size)
        wall_line = self.position.copy.add(direction), \
            self.position.copy.subtract(direction)

        _, intersection = geometry.line_line_intersect(sight_ray, wall_line)

        distance = creature_position.distance(intersection)
        return distance, intersection
