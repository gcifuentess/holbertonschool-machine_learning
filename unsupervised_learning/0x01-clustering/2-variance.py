#!/usr/bin/env python3
'''Variance module'''
import numpy as np


def variance(X, C):
    '''calculates the total intra-cluster variance for a data set
    Args:
        X is a numpy.ndarray of shape (n, d) containing the data set
        C is a numpy.ndarray of shape (k, d) containing the centroid means for
          each cluster
    Returns: var, or None on failure
                 - var is the total variance
    '''
    if (type(X) is not np.ndarray):
        return None

    if (len(X.shape) != 2):
        return None

    if (type(C) is not np.ndarray):
        return None

    if (len(C.shape) != 2):
        return None

    return ((X - C[:, np.newaxis])**2).sum(axis=2).min(axis=0).sum()
