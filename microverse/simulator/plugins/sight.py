import math
from ..utils import ray_circle_intersect


class Sight:
    def __init__(
        self,
        fov=math.pi / 2,
        ray_count=8,
        strength=250,
        environment=[]
    ):
        self.strength = strength
        self.environment = environment
        self.ray_angles = [i / (ray_count - 1) * fov - fov / 2
                           for i in range(ray_count)]

    def get_sight_directions(self, forward):
        return [forward.copy.rotate(ray_angle).scale_to(self.strength)
                for ray_angle in self.ray_angles]

    def __call__(self, creature, _):
        sight_directions = self.get_sight_directions(creature.velocity)
        distances = []

        for sight_direction in sight_directions:
            closest_distance = math.inf
            for element in self.environment:
                position, forward = creature.position.copy, sight_direction.copy
                center, radius = element.position.copy, element.size

                valid, distance, intersection_point = ray_circle_intersect(
                    (position, forward), (center, radius))

                if not valid:
                    distance = math.inf

                if distance < closest_distance:
                    closest_distance = distance

            distances.append(closest_distance)

        return distances

    def render(self, renderer, agent):
        sight_directions = self.get_sight_directions(agent.velocity)
        for sight_direction in sight_directions:
            position, forward = agent.position.copy, sight_direction.copy
            end = position.copy.add(forward)

            renderer.line(
                position.x, position.y,
                end.x, end.y, fill=agent.color.to_hex()
            )
