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
    check = tf.equal(tf.argmax(y, 1), tf.argmax(y_pred, 1))
    cast = tf.cast(check, tf.float32)
    mean = tf.reduce_mean(cast, name="Mean")
    return mean
