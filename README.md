# Microverse
[![Build Status](https://travis-ci.org/mnitchev/microverse.svg?branch=master)](https://travis-ci.org/mnitchev/microverse)

Self reinforcement training of neural network using genetic algorithms.

## About
In this repo we implement `neural network model` that is being trained using heuristics from `genetic algorithms`.
The microverse module has simulator of `2D world` in which `agents` can `see` the food they need to eat in order to stay alive. The fit function that the model is trying to optimize is the number of eaten food items.
Every time an agent dies, we get the two best agents in the current population and we cross their behavior functions (the neural networks) and we mutate them - making a new agent.

## Content
 - Simulator
   - Intersection algorithm
   - Set of render-able and updatable agents

 - Renderer - we use the `ikinter` library to visualize the running simulation

 - Agent - base class for agent - (contains health, color, position and velocity properties)
 - Plugins
   - Sight - sensor module for the agent
   - Digestion - module for `consuming` the food and `leveling_up` the agent
   - Mobility - module used for adding the velocity to the position of the agent
   - Neural network - simple implementation of neural network (it has only `feed-forward` and `crossover` as public methods) used as the brain of the agent
   - Navigator - module that consumes the output of the network and steers the agent accordingly 
   - Fatigue - this module reduces the health of each agent in every `tick` of the simulation

## Heuristics used in the genetic algorithm

### Fitness function
Number of eaten food items.

### Crossover

#### For biases
```python
parent_a = [a1, a2, a3, a4, a5]
parent_b = [b1, b2, b3, b4, b5]
random_split = random(0, 5) # ex. 2

child = [a1, a2, b3, b4, b5]
```

#### For weights
The heuristic for `weights` applied for each row of the weights `matrix`.

### Mutation
Apply `gene` change with probability (mutation_rate).
```python
mutated_dna = [gene if prob() < mutation_rate else
               random(0, 1) for gene in dna]
```

### Selection
When the target population size is more than the current - crossover `the two most fit` agents in the current population.

## Examples

### How to run a simulation
```python
while RENDERER.is_running:
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
```

### How the plugin design implements the `smart agent`
```python
self.sight = Sight(
    fov=fov,
    ray_count=ray_count,
    strength=strength,
    environment=environment
)
self.brain = NeuralNetwork([self.sight.ray_count] + nn + [3])
self.parents = parents
navigator = Navigator()
digestion = Digestion(environment)
mobility = Mobility()
fatigue = Fatigue()

self.plug(self.sight, self.brain, navigator)
self.plug(digestion)
self.plug(mobility)
self.plug(fatigue)
```