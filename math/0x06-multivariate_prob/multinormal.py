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
        self.n = n
        self.d = d

    def pdf(self, x):
        '''calculates the PDF at a data point
        Args:
        x is a numpy.ndarray of shape (d, 1) containing the data point
          whose PDF should be calculated
            - d is the number of dimensions of the Multinomial instance
        Returns the value of the PDF
        '''
        if (type(x) is not np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        d, _ = x.shape

        if (len(x.shape) != 2 or x.shape != (self.d, 1)):
            raise ValueError("x must have the shape ({}, 1)".
                             format(self.d))

        cov_det = np.linalg.det(self.cov)

        const = 1 / (((2 * np.pi) ** (d / 2)) * (cov_det ** (1 / 2)))

        potence = ((x - self.mean).T @
                   np.linalg.inv(self.cov) @
                   (x - self.mean)) * (- 1 / 2)

        return np.asscalar(const * np.exp(potence))
