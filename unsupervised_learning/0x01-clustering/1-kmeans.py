#!/usr/bin/env python3
'''K-means'''
import numpy as np


def kmeans(X, k, iterations=1000):
    '''initializes cluster centroids for K-means
    Args:
        X is a numpy.ndarray of shape (n, d) containing the dataset that
          will be used for K-means clustering
            - n is the number of data points
            - d is the number of dimensions for each data point
        k is a positive integer containing the number of clusters
        iterations is a positive integer containing the maximum number of
                   iterations that should be performed
    Important:
        If no change in the cluster centroids occurs between iterations,
            your function should return
        Initialize the cluster centroids using a multivariate uniform
            distribution
        If a cluster contains no data points during the update step,
            reinitialize its centroid

    Returns: C, clss, or None, None  on failure
                 - C is a numpy.ndarray of shape (k, d) containing the
                     centroid means for each cluster
                 - clss is a numpy.ndarray of shape (n,) containing the
                     index of the cluster in C that each data point belongs to
    '''
    if (type(iterations) is not int or iterations < 1):
        return None, None

    C = initialize(X, k)

    if (C is None):
        return None, None

    for i in range(iterations):
        C_prev = C.copy()
        # euclidian distance between data points and centroids:
        distances = np.sqrt(((X - C[:, np.newaxis])**2).sum(axis=2))
        clss = np.argmin(distances, axis=0)
        for j in range(k):
            # check if cluster contains data points:
            if (X[clss == j].size and X[clss == j].ndim):
                C[j] = X[clss == j].mean(axis=0)
            else:
                C[j] = initialize(X, 1)
        if np.allclose(C_prev, C):
            break

    return C, clss


def initialize(X, k):
    '''initializes cluster centroids for K-means
    Args:
        X is a numpy.ndarray of shape (n, d) containing the dataset that
          will be used for K-means clustering
            - n is the number of data points
            - d is the number of dimensions for each data point
        k is a positive integer containing the number of clusters
    Important:
        The cluster centroids should be initialized with a multivariate
        uniform distribution along each dimension in d:
            - The minimum values for the distribution should be the minimum
              values of X along each dimension in d
            - The maximum values for the distribution should be the maximum
              values of X along each dimension in d
    Returns: a numpy.ndarray of shape (k, d) containing the initialized
             centroids for each cluster, or None on failure
    '''
    if (type(X) is not np.ndarray):
        return None

    if (len(X.shape) != 2):
        return None

    if (type(k) is not int):
        return None

    if (k <= 0):
        return None

    return np.random.uniform(low=np.min(X, axis=0),
                             high=np.max(X, axis=0),
                             size=(k, X.shape[1]))
