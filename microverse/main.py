#!/usr/bin/env python3

from simulator import *
import sys
import math


# Flush std out
old_print = print


def print(*args):
    old_print(*args)
    sys.stdout.flush()


def main():
    creature = Creature(velocity=vec2(1, 0))
    engine = Engine()
    engine.add(creature)

    environment = [Creature(position=vec2(100), size=100)]

    sight = Sight(
        fov=math.pi / 2,
        ray_count=7,
        strength=250,
        environment=environment
    )
    nn = NeuralNetwork([7, 10, 2])
    navigator = Navigator(steering_magnitude=0.01)

    creature.plug(sight, nn, navigator)

    @set_interval(1 / 30, start=True)
    def loop():
        print(creature.position.x, creature.position.y)
        engine.update()


if __name__ == '__main__':
    main()
