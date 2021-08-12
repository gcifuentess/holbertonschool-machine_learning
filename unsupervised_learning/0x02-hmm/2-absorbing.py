#!/usr/bin/env python3
'''Absorbing Chains module'''
import numpy as np


def absorbing(P):
    '''determines if a markov chain is absorbing

    Args:
       P is a is a square 2D numpy.ndarray of shape (n, n) representing the
         standard transition matrix
           - P[i, j] is the probability of transitioning from state i to
                     state j
           - n is the number of states in the markov chain

    Returns: True if it is absorbing, or False on failure
    '''
    if (type(P) is not np.ndarray or len(P.shape) != 2):
        return None

    n = P.shape[0]
    diag = np.diag(P)

    # checks for absorving dimensions:
    if (not np.any(diag == 1)):
        return False

    # the identity matrix is an absorbing markov chain:
    if (P == np.eye(n)).all():
        return True

    # Build the standard form of a transition matrix for an
    # absorbing markov chain, based on:
    # https://www.youtube.com/watch?v=bTeKu7WdbT8

    abs_s_idxs = np.where(diag == 1)[0]  # absorbing states idxs
    n_abss = 0  # number of absorbing states checked

    # orders the absorbing states and creates the standad
    # form matrix
    for idx in abs_s_idxs:

        # check, how many states are already ordered
        while(P[n_abss, n_abss] == 1):
            n_abss += 1

        # Orders actual state if needed:
        if(idx > n_abss):

            permutation = []
            for i in range(n):
                if (i == n_abss):
                    permutation.append(idx)
                    permutation.append(i)
                elif (i != idx):
                    permutation.append(i)

            P[:] = P[permutation, :]  # rearranges rows of P
            P[:] = P[:, permutation]  # rearranges colums of P

            n_abss += 1

    # Identify the R and Q sub-matrices:
    n_abss = len(abs_s_idxs)
    R = P[n_abss:, :n_abss]
    Q = P[n_abss:, n_abss:]

    # Find the(Q - I) matrix, first step towards the
    # fundamental matrix F
    QminusI = np.eye(n - n_abss) - Q

    # check if QminusI is invertible:
    if np.linalg.det(QminusI) == 0:
        return False

    # Find the fundamental matrix:
    F = np.linalg.inv(QminusI)

    # Probabilities for the non-absorbing states:
    FR = np.matmul(F, R)

    # Check if the second property for an Absorbing Markov Chain
    # is met. If in FR there is a row that doesn't sum up to one,
    # the property is not met:
    for i in range(n_abss):
        if (not np.allclose(FR.sum(axis=1), np.ones((FR.shape[0], )))):
            return False

    return True
