class HealthEmitter(object):
    def __call__(self, distances, creature):
        return distances + [creature.health]
