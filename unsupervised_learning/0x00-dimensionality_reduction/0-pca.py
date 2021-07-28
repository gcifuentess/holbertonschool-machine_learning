#!/usr/bin/env python3
'''Principal Components Analysys (PCA) with SVD, module'''
import numpy as np


def pca(X, var=0.95):
    '''performs PCA on a dataset
    Args:
        X is a numpy.ndarray of shape (n, d) where:
            - n is the number of data points
            - d is the number of dimensions in each point
            - all dimensions should  have a mean of 0 across all data points
        var is the fraction of the variance that the PCA transformation
            should maintain
    Returns: the weights matrix, W, that maintains var fraction of X‘s
             original variance
                 - W is a numpy.ndarray of shape (d, nd) where nd is the new
                     dimensionality of the transformed X
    '''
    U, S, VH = np.linalg.svd(X)

    var_total = np.cumsum(S)[-1]

    nd = 0
    while np.cumsum(S)[nd] / var_total < var:
        nd += 1

    return VH[:nd + 1].T
