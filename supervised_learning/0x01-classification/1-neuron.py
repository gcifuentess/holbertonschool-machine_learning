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
