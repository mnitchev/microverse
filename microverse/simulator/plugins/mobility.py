class Mobility:
    def __call__(self, creature, _):
        creature.position.add(creature.velocity)