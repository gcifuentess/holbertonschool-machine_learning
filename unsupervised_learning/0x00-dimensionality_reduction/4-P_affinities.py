#!/usr/bin/env python3
'''P affinities'''
import numpy as np
P_init = __import__('2-P_init').P_init
HP = __import__('3-entropy').HP


def P_affinities(X, tol=1e-5, perplexity=30.0):
    '''calculates the symmetric P affinities of a data set
    Args:
    X is a numpy.ndarray of shape (n, d) containing the dataset to be
      transformed by t-SNE
        - n is the number of data points
        - d is the number of dimensions in each point
    perplexity is the perplexity that all Gaussian distributions should have
    tol is the maximum tolerance allowed (inclusive) for the difference in
        Shannon entropy from perplexity for all Gaussian distributions

    Important: We'll need to perform a binary search on each point’s
    distribution to find the correct value of beta that will give a Shannon
    Entropy H within the tolerance (Think about why we analyze the Shannon
    entropy instead of perplexity). Since beta can be in the range (0, inf),
    we'll have to do a binary search with the high and low initially set to
    None. In our search, we are supposed to increase/decrease beta to
    high/low but they are still set to None, we should double/half the value
    of beta instead.

    Returns: P, a numpy.ndarray of shape (n, n) containing the symmetric P
             affinities
    '''
    n, d = X.shape
    D, P, betas, H = P_init(X, perplexity)

    for i in range(n):
        Di = np.delete(D[i], i)  # excludes itself point
        beta = betas[i]
        Hi, Pi = HP(Di, beta)

        # Binary search:
        high = low = None
        while np.abs(H - Hi) >= tol:
            if H < Hi:
                low = beta.copy()
                if high is None:
                    beta *= 2
                else:
                    beta = (beta + high) / 2
            else:
                high = beta.copy()
                if low is None:
                    beta /= 2
                else:
                    beta = (low + beta) / 2

            Hi, Pi = HP(Di, beta)

        betas[i] = beta.copy()
        P[i][:i] = Pi[:i].copy()
        P[i][i + 1:] = Pi[i:].copy()

    return (P + P.T) / (2 * n)
