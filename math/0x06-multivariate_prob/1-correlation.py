#!/usr/bin/env python3
'''Correlation module'''
import numpy as np


def correlation(C):
    '''calculates a correlation matrix
    Args:
        C is a numpy.ndarray of shape (d, d) containing the data set:
            - d is the number of dimensions.
    Returns: numpy.ndarray of shape (d, d) containing the correlation matrix
    '''
    if (type(C) is not np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    d, _ = C.shape

    if (len(C.shape) != 2 or C.shape != (d, d)):
        raise ValueError("C must be a 2D square matrix")

    diag_sqrt = np.diag(np.sqrt(np.diag(C)))
    diag_inv = np.linalg.inv(diag_sqrt)

    return diag_inv @ C @ diag_inv
