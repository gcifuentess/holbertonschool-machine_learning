#!/usr/bin/env python3
'''Bayesian Optimization Module'''
import numpy as np
from scipy.stats import norm
GP = __import__('2-gp').GaussianProcess


class BayesianOptimization():
    '''performs Bayesian optimization on a noiseless 1D Gaussian process'''

    def __init__(self, f, X_init, Y_init, bounds, ac_samples, l=1, sigma_f=1,
                 xsi=0.01, minimize=True):
        '''class constructor
        Args:
            f is the black-box function to be optimized
            X_init is a numpy.ndarray of shape (t, 1) representing the inputs
                   already sampled with the black-box function
            Y_init is a numpy.ndarray of shape (t, 1) representing the outputs
                   of the black-box function for each input in X_init
            t is the number of initial samples
            bounds is a tuple of (min, max) representing the bounds of the
                   space in which to look for the optimal point
            ac_samples is the number of samples that should be analyzed during
                       acquisition
            l is the length parameter for the kernel
            sigma_f is the standard deviation given to the output of the
                    black-box function
            xsi is the exploration-exploitation factor for acquisition
            minimize is a bool determining whether optimization should be
                     performed for minimization (True) or maximization (False)

        Important: the constructor sets the following public instance attr:
            - f: the black-box function
            - gp: an instance of the class GaussianProcess
            - X_s: a numpy.ndarray of shape (ac_samples, 1) containing all
                   acquisition sample points, evenly spaced between min and max
            - xsi: the exploration-exploitation factor
            - minimize: a bool for minimization versus maximization

        '''
        self.f = f
        self.gp = GP(X_init, Y_init, l, sigma_f)
        min_, max_ = bounds
        X_s = np.linspace(min_, max_, num=ac_samples)
        self.X_s = (np.sort(X_s)).reshape(-1, 1)
        self.xsi = xsi
        self.minimize = minimize

    def acquisition(self):
        '''calculates the next best sample location

        Important: Uses the Expected Improvement acquisition function

        Returns: X_next, EI
            - X_next is a numpy.ndarray of shape (1,) representing the next
                     best sample point
            - EI is a numpy.ndarray of shape (ac_samples,) containing the
                 expected improvement of each potential sample
        '''
        mu, cov = self.gp.predict(self.X_s)
        Z = np.zeros(cov.shape[0])

        if (self.minimize):
            mu_s_opt = np.min(self.gp.Y)
            imp = mu_s_opt - mu - self.xsi
        else:
            mu_s_opt = np.max(self.gp.Y)
            imp = mu - mu_s_opt - self.xsi

        for i in range(cov.shape[0]):
            if cov[i] > 0:
                Z[i] = imp[i] / cov[i]
            else:
                Z[i] = 0
            EI = imp * norm.cdf(Z) + cov * norm.pdf(Z)

        X_next = self.X_s[np.argmax(EI)]

        return X_next, EI
