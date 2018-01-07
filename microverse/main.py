#!/usr/bin/env python3

from simulator import *
import sys


# Flush std out
old_print = print


def print(*args):
    old_print(*args)
    sys.stdout.flush()


def main():
    creature = Creature(velocity=vec2(1, 0.5))
    engine = Engine()
    engine.add(creature)

    @set_interval(1 / 30, start=True)
    def loop():
        print(creature.position.x, creature.position.y)
        engine.update()


if __name__ == "__main__":
    main()