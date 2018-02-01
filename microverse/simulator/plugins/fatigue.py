class Fatigue(object):
    def __call__(self, creature, _):
        creature.level_down(0.005)
