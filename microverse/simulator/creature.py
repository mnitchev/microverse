from .vec2 import vec2


class Creature:
    def __init__(self, position=vec2(), velocity=vec2()):
        self.position = position
        self.velocity = velocity

    def update(self, dt):
        self.position.add(self.velocity)
