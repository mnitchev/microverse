from ..utils import vec2, color


class Agent(object):
    def __init__(
        self, position=vec2(),
        velocity=vec2(),
        size=1,
        fill=color(0, 0, 0)
    ):
        self.position = position
        self.velocity = velocity
        self.size = size
        self.color = fill
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

    def level_up(self, amount=1):
        self.health = min(self.health + amount, 1)

    def level_down(self, amount=1):
        self.health = max(self.health - amount, 0)

    def is_dead(self):
        return self.health <= 0

    def render(self, renderer):
        renderer.arc(
            self.position.x,
            self.position.y,
            self.size,
            fill=self.color.to_hex(),
            outline=color((1-self.health)*255, self.health*255).to_hex(),
            width=3
        )
        for plugin in self.plugins:
            for part in plugin:
                if hasattr(part, 'render'):
                    part.render(renderer, self)
