#!/usr/bin/env python3
'''Optimize k'''
import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    '''tests for the optimum number of clusters by variance
    Args:
        X is a numpy.ndarray of shape (n, d) containing the dataset that
          will be used for K-means clustering
            - n is the number of data points
            - d is the number of dimensions for each data point
        kmin is a positive integer containing the minimum number of clusters to
             check for (inclusive)
        kmax is a positive integer containing the maximum number of clusters to
             check for (inclusive)
        iterations is a positive integer containing the maximum number of
                   iterations for K-means

    Important: This function should analyze at least 2 different cluster sizes

    Returns: results, d_vars, or None, None on failure
                 - results is a list containing the outputs of K-means for
                           each cluster size
                 - d_vars is a list containing the difference in variance from
                          the smallest cluster size for each cluster size
    '''
    if (type(X) is not np.ndarray or len(X.shape) != 2):
        return None, None

    if (type(kmin) is not int or kmin < 1):
        return None, None

    if (kmax is None):
        kmax = X.shape[0]
    elif (type(kmax) is not int or kmax <= kmin):
        return None, None

    results = []
    d_vars = []
    for k in range(kmin, kmax + 1):

        C, clss = kmeans(X, k, iterations)
        if (C is None or clss is None):
            return None, None

        var = variance(X, C)
        if (var is None):
            return None, None

        var = float(var)

        if (k == kmin):
            first_var = var

        results.append((C, clss))
        d_vars.append(first_var - var)

    return results, d_vars
