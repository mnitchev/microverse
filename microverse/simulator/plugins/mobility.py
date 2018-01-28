class Mobility(object):
    def __init__(self, obstacles):
        self.obstacles = obstacles

    def __call__(self, creature, _):
        creature.position.add(creature.velocity)
