from .vec2 import vec2


class Creature:
    def __init__(self, position=vec2(), velocity=vec2(), size=1):
        self.position = position
        self.velocity = velocity
        self.size = size

        # The plugins are list of lists.
        # Each plugin consists of multiple callable "parts",
        # which are piped when the creature is updated.
        self.plugins = []
        self.score = 0

    def level_up(self):
        self.score += 1

    def level_down(self):
        self.score -= 1

    def plug(self, *plugin):
        self.plugins.append(plugin)
        return self

    def steer(self, angle):
        self.velocity.rotate(angle)

    def update(self, dt):
        for plugin in self.plugins:
            piped_value = self
            for part in plugin:
                piped_value = part(piped_value, self)
