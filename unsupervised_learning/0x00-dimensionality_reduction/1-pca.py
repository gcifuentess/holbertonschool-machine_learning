#!/usr/bin/env python3
'''Principal Components Analysys (PCA) with SVD, module'''
import numpy as np


def pca(X, ndim):
    '''performs PCA on a dataset
    Args:
        X is a numpy.ndarray of shape (n, d) where:
            - n is the number of data points
            - d is the number of dimensions in each point
        ndim is the new dimensionality of the transformed X
    Returns: T, a numpy.ndarray of shape (n, ndim) containing the transformed
             version of X
    '''
    std_x = X - np.mean(X, 0)
    U, S, VH = np.linalg.svd(std_x)
    W = VH[:ndim]

    return np.matmul(std_x, W.T)
