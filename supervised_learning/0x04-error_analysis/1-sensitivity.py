#!/usr/bin/env python3
'''confussion matrix sensitivity module'''
import numpy as np


def sensitivity(confusion):
    '''calculates the sensitivity for each class in a confusion matrix
    Args:
        confusion is a confusion numpy.ndarray of shape (classes, classes)
                  where row indices represent the correct labels and column
                  indices represent the predicted labels
        classes is the number of classes
    Returns: a numpy.ndarray of shape (classes,) containing the sensitivity
             of each class
    '''
    True_Positives = np.diagonal(confusion)
    Actual_Positives = np.sum(confusion, axis=1)
    return True_Positives / Actual_Positives
