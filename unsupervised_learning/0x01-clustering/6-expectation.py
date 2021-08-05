#!/usr/bin/env python3
'''Expectation module'''
import numpy as np
pdf = __import__('5-pdf').pdf


def expectation(X, pi, m, S):
    '''calculates the expectation step in the EM algorithm for a GMM
    Args:
        X is a numpy.ndarray of shape (n, d) containing the data set
        pi is a numpy.ndarray of shape (k,) containing the priors for each
           cluster
        m is a numpy.ndarray of shape (k, d) containing the centroid means for
          each cluster
        S is a numpy.ndarray of shape (k, d, d) containing the covariance
          matrices for each cluster

    Returns: g, l, or None, None on failure
        - g is a numpy.ndarray of shape (k, n) containing the posterior
            probabilities for each data point in each cluster
        - l is the total log likelihood
    '''
    if (type(X) is not np.ndarray or len(X.shape) != 2):
        return None, None

    n, d = X.shape

    if (type(pi)is not np.ndarray or len(pi.shape) != 1):
        return None, None

    k = pi.shape[0]

    if (type(m)is not np.ndarray or m.shape != (k, d)):
        return None, None

    if (type(S)is not np.ndarray or S.shape != (k, d, d)):
        return None, None

    likelihood = []

    for i in range(k):
        likelihood.append(pdf(X, m[i], S[i]))

    likelihood = np.array(likelihood)  # shape (k, n)
    l_pi = likelihood * pi[:, np.newaxis]  # shape (k, n)
    marginal_p = np.sum(likelihood * pi[:, np.newaxis], axis=0)  # shape (n, )

    g = l_pi / marginal_p[:, np.newaxis].T  # posterior_p -> shape (k, n)

    # total log likelihood:
    tll = (np.log(l_pi.sum(axis=0))).sum()  # l

    return g, tll
