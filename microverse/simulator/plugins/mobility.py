from ..utils import vec2


class Mobility(object):
    def __call__(self, creature, _):
        new_position = creature.position.copy.add(creature.velocity)

        if new_position.x < 400 - creature.size and new_position.x > -400 + creature.size:
            creature.position.x = new_position.x

        if new_position.y < 300 - creature.size and new_position.y > -300 + creature.size:
            creature.position.y = new_position.y
