#!/usr/bin/env python3

import sys

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

    smart_agent = sim.SmartAgent(
        position=sim.vec2(-50, 0),
        velocity=sim.vec2(1, 0),
        size=10,
        environment=environment,
        fill=sim.color(255, 0, 0)
    )

    engine = sim.Engine(
        sim.Renderer(800, 600)
    )
    engine.add(smart_agent)
    engine.add(*environment)

    @sim.set_interval(1 / 40, start=True)
    def loop():
        print(smart_agent.position.x, smart_agent.position.y)
        engine.update()
        engine.render()


if __name__ == '__main__':
    main()
