#!/usr/bin/env python3
'''Maximization module'''
import numpy as np


def maximization(X, g):
    '''calculates the maximization step in the EM algorithm for a GMM
    Args:
        X is a numpy.ndarray of shape (n, d) containing the data set
        g is a numpy.ndarray of shape (k, n) containing the posterior
          probabilities for each data point in each cluster

    Returns: pi, m, S, or None, None, None on failure
        - pi is a numpy.ndarray of shape (k,) containing the updated priors for
             each cluster
        - m is a numpy.ndarray of shape (k, d) containing the updated centroid
            means for each cluster
        - S is a numpy.ndarray of shape (k, d, d) containing the updated
            covariance matrices for each cluster
    '''
    if (type(X) is not np.ndarray or len(X.shape) != 2):
        return None, None, None

    n, d = X.shape

    if (type(g)is not np.ndarray or len(g.shape) != 2 or g.shape[1] != n):
        return None, None, None

    k, _ = g.shape

    # posterior probabilities should sum up to 1
    if (not np.isclose(np.sum(g, axis=0), np.ones((k,))).all()):
        return None, None, None

    zg = np.sum(g, axis=1, keepdims=True)

    pi = (zg / n).reshape((k, ))

    m = np.sum(X.T * g[:, np.newaxis, :], axis=2) / zg

    S = []
    for i in range(k):
        dmean = X - m[i]
        S.append(((g[i][:, np.newaxis] * dmean).T @ dmean) / zg[i])
    S = np.array(S)

    return pi, m, S
