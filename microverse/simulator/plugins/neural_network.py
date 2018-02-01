import json
import random
import numpy as np
from random import random as prob
from random import randint


def array_mutate(array, mutation_prob):
    return np.array([
        gene if prob() < mutation_prob else gene + np.random.randn() / 20
        for gene in array
    ])


def matrix_mutate(matrix, mutation_prob):
    result = []
    for row in matrix:
        result.append(array_mutate(row, mutation_prob))

    return np.array(result)


def array_crossover(left, right):
    sp = randint(0, len(left))
    return np.concatenate((left[:sp], right[sp:]), axis=0)


def matrix_crossover(left, right):
    result = []
    for left_row, right_row in zip(left, right):
        result.append(array_crossover(left_row, right_row))

    return np.array(result)


def random_matrix(rows, cols):
    """Returns numpy matrix with values from the
    `standard normal` distribution.
    """
    return np.random.randn(rows, cols)


def sigmoid(x):
    """Mapping z to ~1 if z >> 0 else ~0."""
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.array([max(i, 0) for i in x])


class NeuralNetwork:
    """NeuralNetwork class implements sigmoid neurons and `learns` the parameters
    fitting the data with the backpropagation algorithm.
    """

    def __init__(self, sizes):
        """Initializing the parameters of the model.
        Setting initial random values of the weights and biases of the neural
        network.
        """
        self.sizes = sizes
        self.biases = [random_matrix(1, y)[0] for y in sizes[1:]]
        self.weights = [random_matrix(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]

        self.weighted_layer = []
        self.activations = []

    def predict(self, x):
        """Feed forward the network with the x vector and predict the
        maximal value from the output vector.
        """
        hypothesis = self._forward(x)
        winner = max(hypothesis)
        return [1 if h == winner else 0 for h in hypothesis]

    def _forward(self, a):
        """Calculating the output of the network based on the current
        parameters and the input `a`.
        """
        a = np.array(a)
        self.weighted_layer, self.activations = [], [a]
        for w, b in zip(self.weights, self.biases):
            z = w.dot(a) + b
            a = sigmoid(z)
            self.weighted_layer.append(z)
            self.activations.append(a)

        return a

    def crossover(self, other, mutation_prob):
        child = NeuralNetwork(self.sizes)

        for i in range(len(self.biases)):
            child.biases[i] = array_mutate(array_crossover(
                self.biases[i], other.biases[i]
            ), mutation_prob)

        for i in range(len(self.weights)):
            child.weights[i] = matrix_mutate(matrix_crossover(
                self.weights[i], other.weights[i]
            ), mutation_prob)

        return child

    def __call__(self, distances, _):
        return self._forward(distances)

    def _get_weights(self):
        return [[list(r) for r in w] for w in self.weights]

    def _get_biases(self):
        return [list(b) for b in self.biases]

    def file_export(self, file_name):
        with open(file_name, 'w') as file:
            json_nn = json.dumps({
                'weights': self._get_weights(),
                'biases': self._get_biases()
            }, sort_keys=True, indent=2)
            file.write(json_nn)

    def file_import(self, file_name):
        with open(file_name, 'r') as file:
            content = file.read()
            if content != '':
                data = json.loads(content)
                self.weights = [np.array(w) for w in data['weights']]
                self.biases = [np.array(b) for b in data['biases']]