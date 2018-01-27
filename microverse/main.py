#!/usr/bin/env python3

import sys
import math

import simulator as sim

# Flush std out
old_print = print


def print(*args):
    old_print(*args)
    sys.stdout.flush()


def main():
    environment = [
        sim.Food(position=sim.vec2(100, 0), size=30),
        sim.Food(position=sim.vec2(0, 0), size=20)
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

    creature = sim.Creature(
        position=sim.vec2(-30, 0),
        velocity=sim.vec2(1, 0),
        size=10
    )
    creature.plug(mobility)
    creature.plug(sight, brain, navigator)
    creature.plug(digestion)

    engine = sim.Engine(
        sim.Renderer(800, 600)
    )
    engine.add(creature)
    engine.add(*environment)

    @sim.utils.set_interval(1 / 30, start=True)
    def loop():
        print(creature.position.x, creature.position.y)
        engine.update()
        engine.render()


if __name__ == '__main__':
    main()
