#!/usr/bin/env python3
'''Deep Neural Network module'''
import numpy as np


class DeepNeuralNetwork():
    '''defines a deep neural network performing binary classification'''

    def __init__(self, nx, layers):
        '''Deep Neuron Network constructor
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

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}
        l_prev = nx
        for i, nodes in enumerate(layers):
            if type(nodes) is not int or nodes <= 0:
                raise TypeError("layers must be a list of positive integers")
            if i > 0:
                l_prev = layers[i - 1]
            # initialize weights using He et al method:
            self.weights['W{}'.format(i + 1)] = (np.random.randn(nodes,
                                                                 l_prev)
                                                 * np.sqrt(2 / l_prev))
            # initialize biases:
            self.weights['b{}'.format(i + 1)] = np.zeros((nodes, 1))

    @property
    def L(self):
        '''L getter'''
        return self.__L

    @property
    def cache(self):
        '''cache getter'''
        return self.__cache

    @property
    def weights(self):
        '''weights getter'''
        return self.__weights

    def forward_prop(self, X):
        '''Calculates the forward propagation of the neural network
        Args:
            X: is a numpy.ndarray with shape (nx, m) that contains
               the input data.
               - nx is the number of input features to the neuron
               - m is the number of examples
        Return: the output of the neural network and the cache, respectively
        '''
        self.cache['A0'] = X
        for i in range(1, self.L + 1):
            W = self.weights['W{}'.format(i)]
            b = self.weights['b{}'.format(i)]
            A = self.cache['A{}'.format(i - 1)]
            Z = np.matmul(W, A) + b
            #  Forwar propagation with sigmoid activation function:
            self.cache['A{}'.format(i)] = 1 / (1 + np.exp(-Z))
        return self.cache['A{}'.format(i)], self.cache

    def cost(self, Y, A):
        '''Calculates the cost of the model using logistic regression
        Args:
            Y: a numpy.ndarray with shape (1, m) that contains the correct
               labels for the input data
            A: a numpy.ndarray with shape (1, m) containing the activated
               output of the neuron for each example
        Return: the cost
        '''
        part_A = Y * np.log(A)
        part_B = (1 - Y) * np.log(1.0000001 - A)
        return float((-1 / Y.shape[1]) * np.sum(part_A + part_B))
