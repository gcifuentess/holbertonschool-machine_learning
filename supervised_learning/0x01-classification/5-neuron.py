#!/usr/bin/env python3
'''Neuron module'''
import numpy as np


class Neuron():
    '''defines a single neuron performing binary classification'''

    def __init__(self, nx):
        '''Neuron constructor
        Args:
            nx: is the number of input features to the neuron
        '''
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        '''W getter'''
        return self.__W

    @property
    def b(self):
        '''b getter'''
        return self.__b

    @property
    def A(self):
        '''W getter'''
        return self.__A

    def forward_prop(self, X):
        '''Calculates the forward propagation of the neuron
        Args:
            X: is a numpy.ndarray with shape (nx, m) that contains
               the input data.
               - nx is the number of input features to the neuron
               - m is the number of examples
        Return: the private attribute __A updated
        '''
        Z = np.matmul(self.W, X) + self.b
        self.__A = sigmoid(Z)
        return(self.A)

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
        '''Evaluates the neuron’s predictions
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
        A = self.forward_prop(X)
        cost = self.cost(Y, A)
        prediction = np.zeros((1, Y.shape[1]), dtype=int)
        prediction[A >= 0.5] = 1
        return prediction, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        '''Calculates one pass of gradient descent on the neuron
        Args:
            X: is a numpy.ndarray with shape (nx, m) that contains
               the input data.
               - nx is the number of input features to the neuron
               - m is the number of examples
            Y: is a numpy.ndarray with shape (1, m) that contains
               the correct labels for the input data
            A: a numpy.ndarray with shape (1, m) containing the activated
               output of the neuron for each example
            alpha: is the learning rate
        Description: Updates the private attributes __W and __b
        Return: Nothing
        '''
        m = Y.shape[1]
        dZ = A - Y
        dW = np.matmul(dZ, X.T) / m
        db = np.sum(dZ) / m
        self.__W = self.W - alpha * dW
        self.__b = self.b - alpha * db


def sigmoid(x, derivative=False):
    '''The sigmoid function
    Args:
       x: the value to be transformed by the funcion
       derivative: if true acts as the firts derivative
    Return: the sigmoid value of x
    '''
    if derivative is False:
        result = 1 / (1 + np.exp(-x))
    else:
        result = sigmoid(x) * (1 - sigmoid(x))
    return result
