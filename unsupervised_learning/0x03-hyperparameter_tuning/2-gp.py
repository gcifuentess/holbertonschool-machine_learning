#!/usr/bin/env python3
'''Gaussian Process Class'''
import numpy as np


class GaussianProcess():
    '''represents a noiseless 1D Gaussian process'''

    def __init__(self, X_init, Y_init, l=1, sigma_f=1):
        '''class constructor
        Args:
            X_init is a numpy.ndarray of shape (t, 1) representing the inputs
                   already sampled with the black-box function
            Y_init is a numpy.ndarray of shape (t, 1) representing the outputs
                   of the black-box function for each input in X_init
            t is the number of initial samples
            le is the length parameter for the kernel
            sigma_f is the standard deviation given to the output of the
                    black-box function
        '''
        self.X = X_init
        self.Y = Y_init
        self.l = l
        self.sigma_f = sigma_f
        self.K = self.kernel(X_init, X_init)

    def kernel(self, X1, X2):
        '''calculates the covariance kernel matrix between two matrices
        Args:
            X1 is a numpy.ndarray of shape (m, 1)
            X2 is a numpy.ndarray of shape (n, 1)

        Important: the kernel should use the Radial Basis Function (RBF)

        Returns: the covariance kernel matrix as a numpy.ndarray of shape
                 (m, n)
        '''
        sqdist = (np.sum(X1 ** 2, 1).reshape(-1, 1) +
                  np.sum(X2 ** 2, 1) +
                  (-2 * np.dot(X1, X2.T)))

        K = (self.sigma_f ** 2) * np.exp((-1 / (2 * self.l ** 2)) * sqdist)

        return K

    def predict(self, X_s):
        ''' predicts the mean and standard deviation of points in a Gaussian
            process
        Args:
            X_s is a numpy.ndarray of shape (s, 1) containing all of the points
                whose mean and standard deviation should be calculated
                - s is the number of sample points
        Returns: mu, sigma
            - mu is a numpy.ndarray of shape (s,) containing the mean for each
                 point in X_s, respectively
            - sigma is a numpy.ndarray of shape (s,) containing the variance
                    for each point in X_s, respectively
        '''
        K = self.kernel(self.X, X_s)
        Ks = self.kernel(X_s, X_s)
        Kinv = np.linalg.inv(self.K)
        mu = K.T.dot(Kinv).dot(self.Y).reshape(-1)
        cov = Ks - K.T.dot(Kinv).dot(K)
        cov = cov.diagonal()

        return mu, cov

    def update(self, X_new, Y_new):
        '''updates a Gaussian Process
        Args:
            X_new is a numpy.ndarray of shape (1,) that represents the new
                  sample point
            Y_new is a numpy.ndarray of shape (1,) that represents the new
                  sample function value
        '''
        self.X = np.append(self.X, X_new).reshape(-1, 1)
        self.Y = np.append(self.Y, Y_new).reshape(-1, 1)
        self.K = self.kernel(self.X, self.X)
