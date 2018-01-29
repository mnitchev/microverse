class Navigator:
    def __call__(self, movement, creature):
        creature.steer((movement[0] * 2 - 1) / 15)
        creature.velocity.scale_to(movement[1] * 8 + 1)
