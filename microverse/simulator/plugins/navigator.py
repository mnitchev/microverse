class Navigator:
    def __init__(self, steering_magnitude=1):
        self.steering_magnitude = steering_magnitude

    def __call__(self, movement, creature):
        creature.steer((movement[0] - 0.5) / 10)
        # creature.velocity.scale_to(movement[1] * 5 + 1)
