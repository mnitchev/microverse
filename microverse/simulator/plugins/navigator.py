from .neural_network import sigmoid


class Navigator:
    def __call__(self, movement, creature):
        creature.steer((sigmoid(movement[0]) - 1) / 2 * 10)
        creature.velocity.scale_to(movement[1])

        # speed = creature.velocity.copy.scale_to((movement[1] * 2 - 1) * 4)
        # if creature.velocity.copy.add(speed).length < 8:
        #     creature.velocity.add(speed)
