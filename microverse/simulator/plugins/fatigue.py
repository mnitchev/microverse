class Fatigue(object):
    def __call__(self, creature, _):
        amount = 0.02
        if creature.position.x > 400 or creature.position.y < -400 or \
                creature.position.y > 300 or creature.position.y < -300:
            amount = 0.5
        creature.level_down(amount)
