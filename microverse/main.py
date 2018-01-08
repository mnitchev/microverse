#!/usr/bin/env python3

import simulator as sim
import sys
import math


# Flush std out
old_print = print


def print(*args):
    old_print(*args)
    sys.stdout.flush()


def main():
    environment = [
        sim.Food(position=sim.vec2(100), size=100),
        sim.Food(position=sim.vec2(20, 20), size=10)
    ]

    sight = sim.Sight(
        fov=math.pi / 2,
        ray_count=7,
        strength=250,
        environment=environment
    )
    brain = sim.NeuralNetwork([7, 10, 2])
    navigator = sim.Navigator(steering_magnitude=0.01)
    digestion = sim.Digestion(environment=environment)
    mobility = sim.Mobility()

    creature = sim.Creature(velocity=sim.vec2(1, 0))
    creature.plug(mobility)
    creature.plug(sight, brain, navigator)
    creature.plug(digestion)

    engine = sim.Engine()
    engine.add(creature)

    @sim.set_interval(1 / 30, start=True)
    def loop():
        print(creature.position.x, creature.position.y)
        engine.update()


if __name__ == '__main__':
    main()
