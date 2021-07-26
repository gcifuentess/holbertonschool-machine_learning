#!/usr/bin/env python3
'''Mean and Covariance module'''
import numpy as np


def mean_cov(X):
    '''calculates the mean and covariance of a data set
    Args:
        X is a numpy.ndarray of shape (n, d) containing the data set:
            - n is the number of data points
            - d is the number of dimensions in each data point
    Returns: mean, cov:
        - mean is a numpy.ndarray of shape (1, d) containing the mean of the
               data set
        - cov is a numpy.ndarray of shape (d, d) containing the covariance
              matrix of the data set
    '''
    if (type(X) is not np.ndarray or len(X.shape) != 2):
        raise TypeError("X must be a 2D numpy.ndarray")

    n, d = X.shape

    if (n < 2):
        raise ValueError("X must contain multiple data points")

    mean = np.mean(X, 0, keepdims=True)
    std_x = (X - mean)
    cov = np.matmul(std_x.T, std_x) / (n - 1)
    # The reason the sample covariance matrix has N-1} the denominator rather
    # than N is essentially that the population mean E(X) is not known and is
    # replaced by the sample mean.
    # From https://en.wikipedia.org/wiki/Covariance

    return mean, cov
