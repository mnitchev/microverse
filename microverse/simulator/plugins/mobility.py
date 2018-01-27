class Mobility(object):
    def __init__(self, obstacles):
        self.obstacles = obstacles

    def __call__(self, creature, _):
        new_position = creature.position.copy.add(creature.velocity)
        movement_direction = new_position.subtract(creature.position.copy)
        for obstacle in self.obstacles:
            distance, intersection = obstacle.intersect_ray(
                creature.position.copy, movement_direction)
            if distance <= movement_direction.length:
                creature.position = intersection.copy
                creature.velocity = creature.velocity.reverse
                creature.position.add(creature.velocity)
                return

        creature.position.add(creature.velocity)
