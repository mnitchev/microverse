#!/usr/bin/env python3

import sys
import time
import simulator as sim
from random import randint as rnd
from random import shuffle
import math


WIDTH = 800
HEIGHT = 600
RENDERER = sim.Renderer(WIDTH, HEIGHT)

SMART_AGENTS_SIZE = 10
FOODS_SIZE = 5

SMART_AGENTS = set()
FOODS = set()


def food_spawner():
    if len(FOODS) < FOODS_SIZE:
        FOODS.add(sim.Food(
            position=random_world_position(),
            size=10,
            fill=sim.color(200, 50, 72)
        ))


def smart_agent_spawner():
    if len(SMART_AGENTS) < SMART_AGENTS_SIZE:
        new_agent = sim.SmartAgent(
            environment=FOODS, ray_count=16,
            strength=700, fov=math.pi, nn=[10]
        )
        new_agent.position = random_world_position()
        new_agent.velocity = sim.vec2(rnd(1, 2), rnd(-1, 2)).scale_to(1)
        new_agent.size = 15
        new_agent.color = sim.color(0, 255, 255)

        if len(SMART_AGENTS) >= 2:
            left_parent, right_parent = select_parents(SMART_AGENTS)
            new_agent.brain = left_parent.brain.crossover(
                right_parent.brain, 0.05
            )

        SMART_AGENTS.add(new_agent)


def random_world_position():
    return sim.vec2(
        rnd(-WIDTH / 2, WIDTH / 2),
        rnd(-HEIGHT / 2, HEIGHT / 2)
    )


def select_parents(population):
    population = list(population)
    population.sort(key=lambda agent: -agent.fitness())
    return population[:2]


def recycle(items):
    for dead_item in [item for item in items if item.is_dead()]:
        items.remove(dead_item)


while True:
    food_spawner()
    smart_agent_spawner()

    RENDERER.update()

    for agent in SMART_AGENTS:
        agent.update()
    for food in FOODS:
        food.update()

    for agent in SMART_AGENTS:
        agent.render(RENDERER)
    for food in FOODS:
        food.render(RENDERER)

    recycle(FOODS)
    recycle(SMART_AGENTS)
