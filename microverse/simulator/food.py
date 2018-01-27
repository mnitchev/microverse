from .creature import Creature


class Food(Creature):
    def __init__(self, *args, **kwargs):
        Creature.__init__(self, *args, **kwargs)
        self.color = 'red'
