class Navigator:
    def __init__(self, steering_magnitude=1):
        self.steering_magnitude = steering_magnitude

    def __call__(self, angle, creature):
        creature.steer(angle[0] * 2 - 1)
