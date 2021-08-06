#!/usr/bin/env python3
'''BIC module'''
import numpy as np
expectation_maximization = __import__('8-EM').expectation_maximization


def BIC(X, kmin=1, kmax=None, iterations=1000, tol=1e-5, verbose=False):
    '''finds the best number of clusters for a GMM using the Bayesian
       Information Criterion
    '''
    
