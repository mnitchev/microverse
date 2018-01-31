import math
from ..utils import ray_circle_intersect


class Sight(object):
    def __init__(self, fov, ray_count, strength, environment=[]):
        self.strength = strength
        self.environment = environment
        self.ray_count = ray_count
        self.fov = fov

    def get_sight_directions(self, forward):
        self.ray_angles = [i / (self.ray_count - 1) * self.fov - self.fov / 2
                           for i in range(self.ray_count)]
        return [forward.copy.rotate(ray_angle).scale_to(self.strength)
                for ray_angle in self.ray_angles]

    def __call__(self, creature, _):
        sight_directions = self.get_sight_directions(creature.velocity)
        self.distances = []
        self.intersections = []

        for sight_direction in sight_directions:
            closest_distance = math.inf
            for element in self.environment:
                distance, intersection = element.intersect_ray(
                    creature.position.copy, sight_direction.copy
                )

                self.intersections.append(intersection)

                if distance == math.inf:
                    distance = self.strength

                if distance < closest_distance:
                    closest_distance = distance

            da = (self.strength - closest_distance) / self.strength
            self.distances.append(da)

        return self.distances

    def render(self, renderer, agent):
        sight_directions = self.get_sight_directions(agent.velocity)

        for intersection in self.intersections:
            renderer.arc(intersection.x, intersection.y, 3, fill='#fc0')
        for i, sight_direction in enumerate(sight_directions):
            position, forward = agent.position.copy, sight_direction.copy
            end = position.copy.add(forward.copy.scale_to(30))

            renderer.line(
                position.x, position.y,
                end.x, end.y, fill='#666' if self.distances[i] == 0 else '#ff0',
                width=3
            )
