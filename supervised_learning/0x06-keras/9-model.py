#!/usr/bin/env python3
'''Save and Load Model'''
import tensorflow.keras as K


def save_model(network, filename):
    '''saves an entire model
    Args:
        network is the model to save
        filename is the path of the file that the model should be saved to
    Returns: None
    '''
    K.models.save_model(network, filename)


def load_model(filename):
    '''loads an entire model
    Args:
        filename is the path of the file that the model should be loaded from
    Returns: the loaded model
    '''
    print(filename)
    return K.models.load_model(filename)
