#!/usr/bin/env python3
'''Agglomerative module'''
import scipy.cluster.hierarchy
import matplotlib.pyplot as plt


def agglomerative(X, dist):
    '''performs agglomerative clustering on a dataset'''
    
