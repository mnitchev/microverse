from .neural_network import sigmoid


class Navigator:
    def __call__(self, movement, creature):
        creature.steer(movement[0])
        creature.steer(-movement[1])
        # creature.velocity.scale_to(movement[1] * 10)

        speed = creature.velocity.copy.scale_to((movement[2] * 2 - 1) * 4)
        if creature.velocity.copy.add(speed).length < 8:
            creature.velocity.add(speed)
