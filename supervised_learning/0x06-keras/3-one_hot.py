#!/usr/bin/env python3
'''One Hot module'''
import tensorflow.keras as K


def one_hot(labels, classes=None):
    '''converts a label vector into a one-hot matrix
    Important: The last dimension of the one-hot matrix is the number of
               classes
    Returns: the one-hot matrix
    '''
    return K.utils.to_categorical(y=labels,
                                  num_classes=classes)
