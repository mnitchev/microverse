#!/usr/bin/env python3

import sys
import simulator as sim
from random import randint as rnd
from random import random as prob


WIDTH = 800
HEIGHT = 600
RENDERER = sim.Renderer(WIDTH, HEIGHT)

SMART_AGENTS_SIZE = 10
FOODS_SIZE = 10

SMART_AGENTS = set()
FOODS = set()


def food_spawner():
    if prob() < 0.1 and len(FOODS) < FOODS_SIZE:
        FOODS.add(sim.Food(
            position=sim.vec2(
                rnd(-WIDTH / 2, WIDTH / 2),
                rnd(-HEIGHT / 2, HEIGHT / 2)),
            size=20,
            fill=sim.color(200, 50, 72)
        ))


def smart_agent_spawner():
    if prob() < 0.1 and len(SMART_AGENTS) < SMART_AGENTS_SIZE:
        SMART_AGENTS.add(sim.SmartAgent(
            position=sim.vec2(rnd(-300, 300), rnd(-200, 200)),
            velocity=sim.vec2(rnd(1, 3), rnd(-3, 3)).scale_to(10),
            size=10,
            environment=FOODS,
            fill=sim.color(0, 0, 255)
        ))


def recycle(items):
    return {item for item in items if not item.is_dead()}


while True:
    food_spawner()
    smart_agent_spawner()

    RENDERER.update()

    for agent in SMART_AGENTS:
        agent.update()
        agent.render(RENDERER)

    for food in FOODS:
        food.update()
        food.render(RENDERER)

    FOODS = recycle(FOODS)
    SMART_AGENTS = recycle(SMART_AGENTS)
