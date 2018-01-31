import math


class Navigator:
    def __call__(self, movement, creature):
        # print(movement, flush=True)
        creature.steer((movement[0] * 2 - 1) / 16)
        creature.steer(-(movement[1] * 2 - 1) / 16)

        speed = creature.velocity.copy.scale_to((movement[2] * 2 - 1) * 4)
        if creature.velocity.copy.add(speed).length < 8:
            creature.velocity.add(speed)
