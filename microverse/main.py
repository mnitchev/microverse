#!/usr/bin/env python3

import sys
import simulator as sim
from random import randint as rnd


WIDTH = 800
HEIGHT = 600
RENDERER = sim.Renderer(WIDTH, HEIGHT)

SMART_AGENTS_SIZE = 13
FOODS_SIZE = 40

SMART_AGENTS = set()
FOODS = set()

def select_parents(population):
    population = list(population)
    population.sort(key=lambda agent: -agent.fitness())
    print(population[0].fitness(), flush=True)
    return population[:2]


def random_world_position():
    return sim.vec2(
        rnd(-WIDTH / 2, WIDTH / 2),
        rnd(-HEIGHT / 2, HEIGHT / 2)
    )


def food_spawner():
    if len(FOODS) < FOODS_SIZE:
        FOODS.add(sim.Food(
            position=random_world_position(),
            size=20,
            fill=sim.color(200, 50, 72)
        ))


def smart_agent_spawner():
    if len(SMART_AGENTS) < SMART_AGENTS_SIZE:
        new_agent = sim.SmartAgent(FOODS)
        if len(SMART_AGENTS) >= 2:
            left_parent, right_parent = select_parents(SMART_AGENTS)
            new_agent = left_parent.crossover(right_parent)

        new_agent.position = random_world_position()
        new_agent.size = 10
        new_agent.color = sim.color(0, 0, 255)
        new_agent.velocity = sim.vec2(rnd(1, 2), rnd(1, 2)).scale_to(10)

        SMART_AGENTS.add(new_agent)


def recycle(items):
    for dead_item in [item for item in items if item.is_dead()]:
        items.remove(dead_item)


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

    recycle(FOODS)
    recycle(SMART_AGENTS)
