class Navigator:
    def __init__(self, steering_magnitude=1):
        self.steering_magnitude = steering_magnitude

    def __call__(self, direction_decision, creature):
        clockwise, anti_clockwise = tuple(direction_decision)
        if clockwise:
            creature.steer(self.steering_magnitude)
        elif anti_clockwise:
            creature.steer(-self.steering_magnitude)
