from ..utils import vec2, color


class Agent(object):
    def __init__(
        self, position=vec2(),
        velocity=vec2(1),
        size=1,
        fill=color(0, 0, 0)
    ):
        self.time_alive = 0
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

    def update(self, dt=1):
        self.time_alive += 1
        for plugin in self.plugins:
            piped_value = self
            for part in plugin:
                piped_value = part(piped_value, self)

    def level_up(self, amount=1):
        self.health = min(self.health * 2, 1)

    def level_down(self, amount=1):
        self.health = max(self.health - amount, 0)

    def is_dead(self):
        return self.health <= 0

    def fitness(self):
        return self.health

    def render(self, renderer):
        for plugin in self.plugins:
            for part in plugin:
                if hasattr(part, 'render'):
                    part.render(renderer, self)

        renderer.arc(
            self.position.x,
            self.position.y,
            self.size,
            fill=self.color.to_hex(),
            outline=color((1 - self.health) * 255, self.health*255).to_hex(),
            width=self.fitness() / 10 + 2
        )
