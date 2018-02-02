#!/usr/bin/env python3

import sys
import time
import pdb
import simulator as sim
from numpy.random import choice
from random import randint as rnd
from random import shuffle
import math
from random import randint as rnd
import simulator as sim

AGENT_FILE = "agent.json"

WIDTH = 800
HEIGHT = 600
RENDERER = sim.Renderer(WIDTH, HEIGHT, title='Microverse')

SMART_AGENTS_SIZE = 10
FOODS_SIZE = 15

SMART_AGENTS = set()
FOODS = set()
DEAD_AGENTS = set()


def initializeAgents():
    for _ in range(SMART_AGENTS_SIZE):
        new_agent = create_brainless_agent()
        # new_agent.brain.file_import(AGENT_FILE)
        SMART_AGENTS.add(new_agent)


SNAPSHOT_INTERVAL = 500
NN_FILE = 'assets/brain.json'
TIME = 1


def food_spawner():
    if len(FOODS) < FOODS_SIZE:
        FOODS.add(sim.Food(
            position=random_world_position(),
            size=10,
            fill=sim.color(200, 50, 72)
        ))


def smart_agent_spawner(max_fitness):
    half = int(SMART_AGENTS_SIZE / 2)
    if len(SMART_AGENTS) <= half:
        all_agents = list(SMART_AGENTS) + list(DEAD_AGENTS)
        best = list(sorted(all_agents, key=lambda a: -a.fitness()))
        fitnesses = [a.fitness() for a in best]
        total_fitness = sum(fitnesses)
        if max_fitness < best[0].fitness():
            max_fitness = best[0].fitness()
            print("New max:", max_fitness, flush=True)
            best[0].brain.file_export(AGENT_FILE)
        if total_fitness == 0 or best[0].fitness() == total_fitness:
            probabilities = None
        elif best[0].fitness() / total_fitness >= 0.7 and best[0].fitness() >= max_fitness:
            print("Local minima found. Trying again.", flush=True)
            SMART_AGENTS.clear()
            initializeAgents()
            best = [best[0], best[0]]
            probabilities = None
        else:
            probabilities = [a.fitness() / total_fitness for a in best]
        while len(SMART_AGENTS) < SMART_AGENTS_SIZE:
            parents = choice(best, 2, replace=False, p=probabilities)
            left_parent, right_parent = parents[0], parents[1]
            new_agent = create_new_agent(left_parent, right_parent)
            new_agent.brain.file_export("retard.json")

            new_agent = create_brainless_agent()
            new_agent.brain.file_import("retard.json")
            SMART_AGENTS.add(new_agent)
        DEAD_AGENTS.clear()
    return max_fitness


def create_new_agent(left_parent, right_parent):
    new_agent = create_brainless_agent()
    total_fitness = left_parent.fitness() + right_parent.fitness()
    if total_fitness == 0:
        probability = 0.5
    else:
        probability = left_parent.fitness() / total_fitness

    new_brain = left_parent.brain.crossover(
        right_parent.brain,
        probability,
        0.01
    )
    new_agent.brain.weights = new_brain.weights
    new_agent.brain.biases = new_brain.biases
    new_agent.parents = [left_parent, right_parent]
    return new_agent


def create_brainless_agent():
    new_agent = sim.SmartAgent(
        environment=FOODS, ray_count=9,
        strength=1000, fov=math.pi / 2, nn=[6]
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


def focus_best():
    best_agent = max(SMART_AGENTS, key=lambda a: a.fitness())
    for smart_agent in SMART_AGENTS:
        smart_agent.focus = False
    best_agent.focus = True

    if TIME % SNAPSHOT_INTERVAL == 0:
        best_agent.brain.file_export(NN_FILE)


def main():
    max_fitness = 260

    initializeAgents()
    while RENDERER.is_running:
        food_spawner()
        max_fitness = smart_agent_spawner(max_fitness)

        for agent in SMART_AGENTS:
            agent.render(RENDERER)
        for food in FOODS:
            food.render(RENDERER)

        recycle_food()
        recycle_agents()
        recycle(FOODS)
        recycle(SMART_AGENTS)
        focus_best()

        TIME += 1


main()
