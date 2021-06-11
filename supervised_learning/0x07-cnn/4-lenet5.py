#!/usr/bin/env python3
'''LeNet-5 (Tensorflow) module'''
import tensorflow as tf


def lenet5(x, y):
    '''builds a modified version of the LeNet-5 architecture using tensorflow
    Args:
        x is a tf.placeholder of shape (m, 28, 28, 1) containing the input
          images for the network
            - m is the number of images
        y is a tf.placeholder of shape (m, 10) containing the one-hot
          labels for the network

    IMPORTANT:
    The model consist of the following layers in order:
         Convolutional layer with 6 kernels of shape 5x5 with same padding
         Max pooling layer with kernels of shape 2x2 with 2x2 strides
         Convolutional layer with 16 kernels of shape 5x5 with valid padding
         Max pooling layer with kernels of shape 2x2 with 2x2 strides
         Fully connected layer with 120 nodes
         Fully connected layer with 84 nodes
         Fully connected softmax output layer with 10 nodes

    Returns:
        a tensor for the softmax activated output
        a training operation that utilizes Adam optimization (with
          default hyperparameters)
        a tensor for the loss of the netowrk
        a tensor for the accuracy of the network
    '''
    w = tf.contrib.layers.variance_scaling_initializer()
    l1 = tf.layers.Conv2D(filters=6,
                          kernel_size=(5, 5),
                          padding='same',
                          activation='relu',
                          kernel_initializer=w)(x)

    l2 = tf.layers.MaxPooling2D(pool_size=(2, 2),
                                strides=(2, 2))(l1)

    l3 = tf.layers.Conv2D(filters=16,
                          kernel_size=(5, 5),
                          padding='valid',
                          activation='relu',
                          kernel_initializer=w)(l2)

    l4 = tf.layers.MaxPooling2D(pool_size=(2, 2),
                                strides=(2, 2))(l3)

    flatten = tf.layers.Flatten()(l4)

    l5 = tf.layers.Dense(units=120,
                         activation='relu',
                         kernel_initializer=w)(flatten)

    l6 = tf.layers.Dense(units=84,
                         activation='relu',
                         kernel_initializer=w)(l5)

    output = tf.layers.Dense(units=10,
                             kernel_initializer=w)(l6)

    y_pred = tf.nn.softmax(output)

    loss = tf.losses.softmax_cross_entropy(y, output)

    adam = tf.train.AdamOptimizer(loss)
    optimization = adam.minimize(loss)

    check_acc = tf.equal(tf.argmax(y, 1), tf.argmax(output, 1))
    cast_acc = tf.cast(check_acc, tf.float32)
    accuracy = tf.reduce_mean(cast_acc, name="Mean")

    return y_pred, optimization, loss, accuracy
