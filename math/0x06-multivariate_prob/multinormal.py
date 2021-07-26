#!/usr/bin/env python3
'''MultiNormal module'''
import numpy as np


class MultiNormal():
    '''Represents a Multivariate Normal distribution'''

    def __init__(self, data):
        '''class constructor
        Args:
            data is a numpy.ndarray of shape (d, n) containing the data set:
                - n is the number of data points
                - d is the number of dimensions in each data point
        '''
        if (type(data) is not np.ndarray or len(data.shape) != 2):
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        if (n < 2):
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, 1, keepdims=True)
        std_data = (data - self.mean)
        self.cov = np.matmul(std_data, std_data.T) / (n - 1)
