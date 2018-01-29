class Navigator:
    def __call__(self, movement, creature):
        creature.steer((movement[0] * 2 - 1) / 10)
        creature.velocity.scale_to(movement[1] * 5 + 1)
