#!/usr/bin/env python3
'''tensorflow accuracy module'''
import tensorflow as tf


def calculate_accuracy(y, y_pred):
    '''calculates the accuracy of a prediction
    Args:
             y: is a placeholder for the labels of the input data
        y_pred: is a tensor containing the network’s predictions
    Return: a tensor containing the decimal accuracy of the prediction
    '''
    mean = tf.equal(y, y_pred)
    mean = tf.cast(mean, tf.float32)
    mean = tf.reduce_mean(mean, name="Mean")
    return mean
