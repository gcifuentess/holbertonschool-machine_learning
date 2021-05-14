#!/usr/bin/env python3
'''tensorflow trainin a neural network module'''
import tensorflow as tf


def evaluate(X, Y, save_path):
    '''evaluates the output of a neural network
    Args:
        X: is a numpy.ndarray containing the input data to evaluate
        Y: is a numpy.ndarray containing the one-hot labels for X
        save_path: is the location to load the model from
    Return: the network’s prediction, accuracy, and loss, respectively
    '''
    with tf.Session() as sess:
        new_saver = tf.train.import_meta_graph(save_path + ".meta")
        new_saver.restore(sess, save_path)
        x = tf.get_collection("x")[0]
        y = tf.get_collection("y")[0]
        y_pred = tf.get_collection("y_pred")[0]
        accuracy = tf.get_collection("accuracy")[0]
        loss = tf.get_collection("loss")[0]
        y_pred = sess.run(y_pred, feed_dict={x: X, y: Y})
        accuracy = sess.run(accuracy, feed_dict={x: X, y: Y})
        loss = sess.run(loss, feed_dict={x: X, y: Y})
        return y_pred, accuracy, loss
