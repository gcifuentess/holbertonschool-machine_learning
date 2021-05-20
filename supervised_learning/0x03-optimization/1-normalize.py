#!/usr/bin/env python3
'''Normalize module'''
import numpy as np


def normalize(X, m, s):
    '''normalizes (standardizes) a matrix
    Args:
        X is the numpy.ndarray of shape (d, nx) to normalize
            d is the number of data points
            nx is the number of features
        m is a numpy.ndarray of shape (nx,) that contains the mean of all
          features of X
        s is a numpy.ndarray of shape (nx,) that contains the standard
          deviation of all features of X
    Returns: The normalized X matrix
    '''
    for i in range(X.shape[1]):
        X[:, i] = np.subtract(X[:, i], m[i])
        X[:, i] = np.divide(X[:, i], s[i])
    return X
