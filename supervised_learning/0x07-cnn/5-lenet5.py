#!/usr/bin/env python3
'''LeNet-5 (Keras) module'''
import tensorflow.keras as K


def lenet5(X):
    '''builds a modified version of the LeNet-5 architecture using
    keras
    Args:
        X is a K.Input of shape (m, 28, 28, 1) containing the input images
          for the network
            - m is the number of images
    IMPORTANT:
    The model consist of the following layers in order:
        Convolutional layer with 6 kernels of shape 5x5 with same padding
        Max pooling layer with kernels of shape 2x2 with 2x2 strides
        Convolutional layer with 16 kernels of shape 5x5 with valid padding
        Max pooling layer with kernels of shape 2x2 with 2x2 strides
        Fully connected layer with 120 nodes
        Fully connected layer with 84 nodes
        Fully connected softmax output layer with 10 nodes

    Returns: a K.Model compiled to use Adam optimization (with default
             hyperparameters) and accuracy metrics
    '''
    w = K.initializers.he_normal(seed=None)
    l1 = K.layers.Conv2D(filters=6,
                         kernel_size=(5, 5),
                         padding='same',
                         activation='relu',
                         kernel_initializer=w)(X)

    l2 = K.layers.MaxPool2D(pool_size=(2, 2),
                            strides=(2, 2))(l1)

    l3 = K.layers.Conv2D(filters=16,
                         kernel_size=(5, 5),
                         padding='valid',
                         activation='relu',
                         kernel_initializer=w)(l2)

    l4 = K.layers.MaxPool2D(pool_size=(2, 2),
                            strides=(2, 2))(l3)

    flatten = K.layers.Flatten()(l4)

    l5 = K.layers.Dense(units=120,
                        activation='relu',
                        kernel_initializer=w)(flatten)

    l6 = K.layers.Dense(units=84,
                        activation='relu',
                        kernel_initializer=w)(l5)

    output = K.layers.Dense(units=10,
                            activation='softmax'
                            kernel_initializer=w)(l6)

    model = K.Model(inputs=X, outputs=output)
    model.compile(optimizer="adam",
                  loss="categorical_crossentropy",
                  metrics=["accuracy"])
    return model
