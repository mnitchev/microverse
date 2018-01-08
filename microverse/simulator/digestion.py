from .geometry import circles_intersect


class Digestion:
    def __init__(self, environment):
        self.environment = environment

    def __call__(self, creature, _):
        for element in self.environment:
            element_circle = element.position, element.size
            creature_circle = creature.position, creature.size
            if circles_intersect(element_circle, creature_circle):
                creature.level_up()
                element.level_down()
