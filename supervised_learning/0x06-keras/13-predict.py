#!/usr/bin/env python3
'''predict module'''
import tensorflow.keras as K


def predict(network, data, verbose=False):
    '''that makes a prediction using a neural network:
    Args:
        network is the network model to make the prediction with
        data is the input data to make the prediction with
        verbose is a boolean that determines if output should be printed
                during the prediction process
    Returns: the prediction for the data
    '''
    return network.predict(x=data,
                           batch_size=None,
                           verbose=verbose)
