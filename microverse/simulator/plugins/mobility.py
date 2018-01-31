class Mobility(object):
    def __call__(self, creature, _):
        creature.position.add(creature.velocity)
        if creature.position.x > 400:
            creature.position.x = 400
        if creature.position.x < -400:
            creature.position.x = -400

        if creature.position.y > 300:
            creature.position.y = 300
        if creature.position.y < -300:
            creature.position.y = -300
