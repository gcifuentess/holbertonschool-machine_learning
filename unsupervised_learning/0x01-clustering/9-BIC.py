#!/usr/bin/env python3
'''BIC module'''
import numpy as np
expectation_maximization = __import__('8-EM').expectation_maximization


def BIC(X, kmin=1, kmax=None, iterations=1000, tol=1e-5, verbose=False):
    '''finds the best number of clusters for a GMM using the Bayesian
    Information Criterion (BIC)
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
        tol is a non-negative float containing tolerance of the log likelihood
        verbose is a boolean that determines if you should print information

    Returns: best_k, best_result, l, b, or None, None, None, None on failure
        best_k is the best value for k based on its BIC
        best_result is tuple containing pi, m, S
            - pi is a numpy.ndarray of shape (k,) containing the cluster priors
                 for the best number of clusters
            - m is a numpy.ndarray of shape (k, d) containing the centroid
                means for the best number of clusters
            - S is a numpy.ndarray of shape (k, d, d) containing the covariance
                matrices for the best number of clusters
        l is a numpy.ndarray of shape (kmax - kmin + 1) containing the log
          likelihood for each cluster size tested
    '''
    if (type(X) is not np.ndarray or len(X.shape) != 2):
        return None, None, None, None

    if (type(kmin) is not int or kmin < 1):
        return None, None, None, None

    if (kmax is None):
        kmax = X.shape[0]
    elif (type(kmax) is not int or kmax <= kmin):
        return None, None, None, None

    EM = expectation_maximization
    n, d = X.shape

    b = []
    maximizations = []
    all_k = []
    all_tll = []
    for k in range(kmin, kmax + 1):
        all_k.append(k)
        pi, m, S, g, tll = EM(X, k, iterations, tol, verbose)
        if (pi is None or m is None or S is None or g is None or tll is None):
            return None, None, None, None
        maximizations.append((pi, m, S))
        all_tll.append(tll)
        # from https://stats.stackexchange.com/questions/229293/
        # the-number-of-parameters-in-gaussian-mixture-model/229321:
        p = (k * d) * (d + 3) / 2 + k - 1
        bic = p * np.log(n) - 2 * tll
        b.append(bic)

    all_tll = np.array(all_tll)
    b = np.array(b)

    min_bic_idx = np.argmin(b)
    best_k = all_k[min_bic_idx]
    best_result = maximizations[min_bic_idx]

    return best_k, best_result, all_tll, b
