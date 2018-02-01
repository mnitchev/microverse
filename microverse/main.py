#!/usr/bin/env python3

import sys
import time
import pdb
import simulator as sim
from random import randint as rnd
from random import shuffle
import math


WIDTH = 800
HEIGHT = 600
RENDERER = sim.Renderer(WIDTH, HEIGHT)

SMART_AGENTS_SIZE = 10
FOODS_SIZE = 10

SMART_AGENTS = set()
FOODS = set()
DEAD_AGENTS = set()


def initializeAgents():
    for _ in range(SMART_AGENTS_SIZE):
        new_agent = create_brainless_agent()
        SMART_AGENTS.add(new_agent)


def food_spawner():
    if len(FOODS) < FOODS_SIZE:
        FOODS.add(sim.Food(
            position=random_world_position(),
            size=15,
            fill=sim.color(200, 50, 72)
        ))


def smart_agent_spawner():
    half = int(SMART_AGENTS_SIZE / 2)
    if len(SMART_AGENTS) <= half:
        all_agents = list(SMART_AGENTS) + list(DEAD_AGENTS)
        best = list(sorted(all_agents, key=lambda a: -a.fitness()))
        shuffle(best)
        needed_count = SMART_AGENTS_SIZE - len(SMART_AGENTS)
        for i in range(0, needed_count - 1):
            left_parent, right_parent = best[i], best[i + 1]
            new_agent = create_new_agent(left_parent, right_parent)
            SMART_AGENTS.add(new_agent)
        new_agent = create_new_agent(best[needed_count - 1], best[0])
        SMART_AGENTS.add(new_agent)
        DEAD_AGENTS.clear()


def create_new_agent(left_parent, right_parent):
    new_agent = create_brainless_agent()
    # left_parent, right_parent = select_parents(SMART_AGENTS)
    new_agent.brain = left_parent.brain.crossover(
        right_parent.brain, 0.05
    )
    new_agent.parents = [left_parent, right_parent]
    return new_agent


def create_brainless_agent():
    new_agent = sim.SmartAgent(
        environment=FOODS, ray_count=9,
        strength=1000, fov=math.pi / 2, nn=[5]
    )
    new_agent.position = random_world_position()
    new_agent.velocity = sim.vec2(rnd(1, 2), rnd(-1, 2)).scale_to(3)
    new_agent.size = 20
    new_agent.color = sim.color(120, 50, 250)
    return new_agent


def recycle_agents():
    for dead_item in [item for item in SMART_AGENTS if item.is_dead()]:
        SMART_AGENTS.remove(dead_item)
        DEAD_AGENTS.add(dead_item)


def recycle_food():
    for dead_item in [item for item in FOODS if item.is_dead()]:
        FOODS.remove(dead_item)


def random_world_position():
    return sim.vec2(
        rnd(-WIDTH / 2, WIDTH / 2),
        rnd(-HEIGHT / 2, HEIGHT / 2)
    )


def select_parents(population):
    return sorted(list(population),
                  key=lambda agent: -agent.fitness())[:2]


def recycle(items):
    for dead_item in [item for item in items if item.is_dead()]:
        items.remove(dead_item)


initializeAgents()

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

    recycle_food()
    recycle_agents()
