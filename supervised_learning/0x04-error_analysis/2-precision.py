#!/usr/bin/env python3
'''confussion matrix precision module'''
import numpy as np


def precision(confusion):
    '''calculates the precision for each class in a confusion matrix
    Args:
        confusion is a confusion numpy.ndarray of shape (classes, classes)
                  where row indices represent the correct labels and column
                  indices represent the predicted labels
        classes is the number of classes
    Returns: a numpy.ndarray of shape (classes,) containing the precision of
             each class
    '''
    True_Positives = np.diagonal(confusion)
    Predicted_Positives = np.sum(confusion, axis=0)
    return True_Positives / Predicted_Positives
