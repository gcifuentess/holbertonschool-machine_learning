#!/usr/bin/env python3
'''Neural Network module'''
import numpy as np


class NeuralNetwork():
    '''defines a neural network with one hidden layer performing binary
    classification'''

    def __init__(self, nx, nodes):
        '''Neuron Network constructor
        Args:
            nx: is the number of input features to the neuron
            nodes: is the number of nodes found in the hidden layer
        '''
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(nodes) is not int:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        '''W1 getter'''
        return self.__W1

    @property
    def b1(self):
        '''b1 getter'''
        return self.__b1

    @property
    def A1(self):
        '''A1 getter'''
        return self.__A1

    @property
    def W2(self):
        '''W2 getter'''
        return self.__W2

    @property
    def b2(self):
        '''b2 getter'''
        return self.__b2

    @property
    def A2(self):
        '''A2 getter'''
        return self.__A2

    def forward_prop(self, X):
        '''Calculates the forward propagation of the neural network
        Args:
            X: is a numpy.ndarray with shape (nx, m) that contains
               the input data.
               - nx is the number of input features to the neuron
               - m is the number of examples
        Return: the private attributes __A1 and __A2 updated
        '''
        Z1 = np.matmul(self.W1, X) + self.b1
        self.__A1 = 1 / (1 + np.exp(-Z1))  # A1 shape: (nodes, m)
        Z2 = np.matmul(self.W2, self.A1) + self.b2
        self.__A2 = 1 / (1 + np.exp(-Z2))  # A2 shape: (1, m)
        return self.A1, self.A2

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
