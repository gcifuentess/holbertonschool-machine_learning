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


def sigmoid(x, derivative=False):
    '''The sigmoid function
    Args:
       x: the value to be transformed by the funcion
       derivative: if true acts as the firts derivative
    Return: the transformed value
    '''
    if derivative is False:
        result = 1 / (1 + np.exp(-x))
    else:
        result = sigmoid(x) * (1 - sigmoid(x))
    return result
