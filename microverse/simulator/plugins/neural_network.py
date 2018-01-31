import random
import numpy as np
from random import random as prob
from random import randint


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

    def crossover(self, other):
        child = NeuralNetwork(self.sizes)

        for i in range(len(self.biases)):
            child.biases[i] = array_crossover(self.biases[i], other.biases[i])

        for i in range(len(self.weights)):
            child.weights[i] = matrix_crossover(
                self.weights[i], other.weights[i])

        return child

    def __call__(self, distances, _):
        return self._forward(distances)
