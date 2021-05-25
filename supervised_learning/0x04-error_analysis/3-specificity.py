#!/usr/bin/env python3
'''confussion matrix specificity module'''
import numpy as np


def specificity(confusion):
    '''calculates the specificity for each class in a confusion matrix
    Args:
        confusion is a confusion numpy.ndarray of shape (classes, classes)
                  where row indices represent the correct labels and column
                  indices represent the predicted labels
        classes is the number of classes
    Returns: a numpy.ndarray of shape (classes,) containing the specificity of
             each class
    '''
    True_Positives = np.diagonal(confusion)
    Predicted_Positives = np.sum(confusion, axis=0)
    Actual_Positives = np.sum(confusion, axis=1)
    False_Positives = Predicted_Positives - True_Positives
    False_Negatives = Actual_Positives - True_Positives
    True_Negatives = np.sum(confusion) - (False_Positives +
                                          False_Negatives + True_Positives)
    return True_Negatives / (True_Negatives + False_Positives)
