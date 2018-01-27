#!/usr/bin/env python3

import sys
import simulator as sim

# Flush std out
old_print = print


def print(*args):
    old_print(*args)
    sys.stdout.flush()


def main():
    environment = []
    for i in range(0, 800, 100):
        for j in range(0, 600, 100):
            environment.append(
                sim.Food(position=sim.vec2(i - 400, j - 300), size=20))

    obstacles = [
        sim.Wall(direction=sim.vec2(1, 0),
                 position=sim.vec2(0, 300), size=400),
        sim.Wall(direction=sim.vec2(1, 0),
                 position=sim.vec2(0, -300), size=400),
        sim.Wall(direction=sim.vec2(0, 1),
                 position=sim.vec2(400, 0), size=300),
        sim.Wall(direction=sim.vec2(0, 1),
                 position=sim.vec2(-400, 0), size=300)
    ]

    engine = sim.Engine(
        sim.Renderer(800, 600)
    )

    smart_agent = sim.SmartAgent(
        position=sim.vec2(-50, 0),
        velocity=sim.vec2(5, 2),
        size=10,
        environment=environment,
        obstacles=obstacles,
        fill=sim.color(255, 0, 0)
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
