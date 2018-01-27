from ..utils import vec2, color


class Agent(object):
    def __init__(
        self, position=vec2(),
        velocity=vec2(),
        size=1,
        object_color=color(0, 0, 0)
    ):
        self.position = position
        self.velocity = velocity
        self.size = size
        self.color = object_color
        self.health = 1

        # The plugins are list of lists.
        # Each plugin consists of multiple callable "parts",
        # which are piped when the creature is updated.
        self.plugins = []

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

    def level_up(self):
        self.health += 1

    def level_down(self):
        self.health -= 1

    def is_dead(self):
        return self.health <= 0

    def render(self, render):
        render.arc(
            self.position.x,
            self.position.y,
            self.size / 2,
            fill=self.color.to_hex()
        )
