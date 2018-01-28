from ..utils import circles_intersect


class Digestion:
    def __init__(self, environment):
        self.environment = environment

    def __call__(self, creature, _):
        to_be_removed = []
        for element in self.environment:
            element_circle = element.position, element.size
            creature_circle = creature.position, creature.size
            if circles_intersect(element_circle, creature_circle):
                amount_consumed = 1
                creature.level_up(amount_consumed)
                element.level_down(amount_consumed)
                if element.is_dead():
                    to_be_removed.append(element)
        for element in to_be_removed:
            self.environment.remove(element)
