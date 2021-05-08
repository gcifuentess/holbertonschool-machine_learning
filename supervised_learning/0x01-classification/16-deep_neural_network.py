#!/usr/bin/env python3
'''Deep Neural Network module'''
import numpy as np


class DeepNeuralNetwork():
    '''defines a deep neural network performing binary classification'''

    def __init__(self, nx, layers):
        '''Neuron Network constructor
        Args:
            nx: is the number of input features to the neuron
            layers: is a list representing the number of nodes in each layer
                    of the network.
                    - The first value in layers represents the number of nodes
                      in the first layer, …
        '''
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(layers) is not list or len(layers) == 0:
            raise TypeError("layers must be a list of positive integers")

        self.L = len(layers)
        self.cache = {}
        self.weights = {}
        l_prev = nx
        for i, nodes in enumerate(layers):
            if type(nodes) is not int or nodes <= 0:
                raise TypeError("layers must be a list of positive integers")
            if i > 0:
                l_prev = layers[i - 1]
            # initialize weights:
            self.weights['W{}'.format(i + 1)] = (np.random.randn(nodes, l_prev)
                                                 * np.sqrt(2 / l_prev))
            # initialize biases:
            self.weights['b{}'.format(i + 1)] = np.zeros((nodes, 1))
