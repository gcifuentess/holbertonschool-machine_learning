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

    def evaluate(self, X, Y):
        '''Evaluates the neural network’s predictions
        Args:
            X: is a numpy.ndarray with shape (nx, m) that contains
               the input data.
               - nx is the number of input features to the neuron
               - m is the number of examples
            Y: is a numpy.ndarray with shape (1, m) that contains
               the correct labels for the input data
        Return: the neuron’s prediction and the cost of the network
            - The prediction is a numpy.ndarray with shape (1, m)
              containing the predicted labels for each example
            - The label values are 1 if the output of the network
              is >= 0.5 and 0 otherwise
        '''
        A1, A2 = self.forward_prop(X)
        cost = self.cost(Y, A2)
        prediction = np.zeros((1, Y.shape[1]), dtype=int)
        prediction[A2 >= 0.5] = 1
        return prediction, cost

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        '''Calculates one pass of gradient descent on the neural network
        Args:
            X: is a numpy.ndarray with shape (nx, m) that contains
               the input data.
               - nx is the number of input features to the neuron
               - m is the number of examples
            Y: is a numpy.ndarray with shape (1, m) that contains
               the correct labels for the input data
            A1: is the output of the hidden layer
            A2: is the predicted output
            alpha: is the learning rate
        Description: Updates the private attributes __W and __b
        Return: Nothing
        '''
        m = Y.shape[1]
        dZ2 = A2 - Y  # shape (1, m)
        dW2 = np.matmul(dZ2, A1.T) / m  # shape (1, nodes)
        db2 = (1 / m) * np.sum(dZ2, axis=1, keepdims=True)
        dZ1 = np.matmul((self.W2).T, dZ2) * (A1 * (1 - A1))  # shape (nodes, m)
        dW1 = (1 / m) * (np.matmul(dZ1, X.T))
        db1 = np.sum(dZ1, axis=1, keepdims=True) / m  # shape (nodes, 1)
        self.__W1 = self.W1 - alpha * dW1
        self.__b1 = self.b1 - alpha * db1
        self.__W2 = self.W2 - alpha * dW2
        self.__b2 = self.b2 - alpha * db2
