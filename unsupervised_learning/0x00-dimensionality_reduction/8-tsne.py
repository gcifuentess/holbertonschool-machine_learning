#!/usr/bin/env python3
'''t-SNE transformation'''
import numpy as np
pca = __import__('1-pca').pca
P_affinities = __import__('4-P_affinities').P_affinities
grads = __import__('6-grads').grads
cost = __import__('7-cost').cost


def tsne(X, ndims=2, idims=50, perplexity=30.0, iterations=1000, lr=500):
    '''performs a t-SNE transformation
    Args:
        X is a numpy.ndarray of shape (n, d) containing the dataset to be
          transformed by t-SNE
            - n is the number of data points
            - d is the number of dimensions in each point
        ndims is the new dimensional representation of X
        idims is the intermediate dimensional representation of X after PCA
        perplexity is the perplexity
        iterations is the number of iterations
        lr is the learning rate

    Important:
        - Every 100 iterations, not including 0, print Cost at iteration
          {iteration}: {cost}
              * {iteration} is the number of times Y has been updated and
                {cost} is the corresponding cost
        - After every iteration, Y should be re-centered by subtracting its
          mean
        - For the first 100 iterations, perform early exaggeration with an
          exaggeration of 4
        - For momentum, a(t) = 0.5 for the first 20 iterations and 0.8
          thereafter

    Returns: Y, a numpy.ndarray of shape (n, ndim) containing the optimized
             low dimensional transformation of X
    '''
    n, d = X.shape
    X = pca(X, idims)
    P = P_affinities(X, perplexity=perplexity)
    # Y = np.random.normal(0, 10-4, size=(n, ndims))
    Y = np.random.randn(n, ndims)

    # initialize past values:
    Y_1 = Y.copy()
    Y_2 = Y.copy()

    # for momentum:
    early_exag = 4
    P = early_exag * P

    for i in range(1, iterations + 1):
        if i == 101:
            P = P / early_exag

        dY, Q = grads(Y, P)

        if i < 21:
            a_t = 0.5
        else:
            a_t = 0.8

        Y = Y - lr * dY + a_t * (Y_1 - Y_2)

        # mean re-centering
        Y = (Y - np.mean(Y, 0))  # / np.std(Y, 0)
        Y_2 = Y_1.copy()
        Y_1 = Y.copy()

        if i % 100 == 0:
            C = cost(P, Q)
            print("Cost at iteration {}: {}".format(i, C))

    return Y
