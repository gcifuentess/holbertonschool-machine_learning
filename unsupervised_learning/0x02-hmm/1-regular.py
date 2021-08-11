#!/usr/bin/env python3
'''Regular Chains module'''
import numpy as np


def regular(P):
    '''Determines the steady state probabilities of a regular markov chain
    Args:
        P is a square 2D numpy.ndarray of shape (n, n) representing the
          transition matrix
            - P[i, j] is the probability of transitioning from state i to
                      state j
            - n is the number of states in the markov chain

    Returns: a numpy.ndarray of shape (1, n) containing the steady state
             probabilities, or None on failure
    '''
    if (type(P) is not np.ndarray or
            len(P.shape) != 2 or
            P.shape[0] != P.shape[1]):
        return None

    n = P.shape[0]

    # to check if the transition matrix is regular:
    transition_regular = 0
    for i in range(1, 11):
        power_p = np.linalg.matrix_power(P, i)
        if (np.greater(P, 0).all()):
            transition_regular = 1
            break

    if (not transition_regular):
        return None

    # Based on: https://stackoverflow.com/questions/31098228/...
    # ...solving-system-using-linalg-with-constraints
    # see answer from vladcrash
    C = np.ones((n + 1, n))  # C stands for coefficients, adds a new row of 1's
    C[:-1, :] = (P.T - np.eye(n))  # moves to the left the dependent values
    D = np.ones((n + 1, 1))  # Ordinate or “dependent variable” values
    D[:-1, :] = np.zeros((n, 1))  # a matrix with 0's but the last
    X, residuals, rank, s = np.linalg.lstsq(
        a=C,
        b=D,
        rcond=None,
    )  # solves the equations system

    # Also see: https://riptutorial.com/numpy/example/16034/...
    # ...find-the-least-squares-solution-to-a-linear-system-with-np-linalg-lstsq
    # to understand how to solve equations systems with np.linalg.lstsq

    return X.reshape((1, n))
