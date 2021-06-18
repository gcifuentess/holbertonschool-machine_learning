#!/usr/bin/env python3
'''DenseNet-121 module'''
import tensorflow.keras as K
dense_block = __import__('5-dense_block').dense_block
transition_layer = __import__('6-transition_layer').transition_layer


def densenet121(growth_rate=32, compression=1.0):
    '''Builds the DenseNet-121 architecture as described in Densely
    Connected Convolutional Networks
    Args:
        growth_rate is the growth rate
        compression is the compression factor
    Important: Input data should have shape (224, 224, 3)
    Returns: the keras model
    '''
    w = K.initializers.he_normal()
    inputs = K.Input(shape=(224, 224, 3))

    sub_layers = [6, 12, 24, 16]

    l1 = K.layers.BatchNormalization()(inputs)
    l1 = K.layers.Activation("relu")(l1)

    l2 = K.layers.Conv2D(filters=64,
                         kernel_size=(7, 7),
                         strides=2,
                         padding="same",
                         kernel_initializer=w)(l1)

    l3 = K.layers.MaxPool2D(pool_size=(3, 3),
                            strides=2,
                            padding="same")(l2)

    l4 = l3
    filters = 64
    for i in range(4):
        l4, filters = dense_block(l4, filters, growth_rate, sub_layers[i])
        if i < 3:
            l4, filters = transition_layer(l4, filters, compression)

    l5 = K.layers.AveragePooling2D(pool_size=(7, 7),
                                   strides=1,
                                   padding="valid")(l4)

    output = K.layers.Dense(units=1000,
                            activation="softmax",
                            kernel_initializer=w)(l5)

    return K.Model(inputs=inputs, outputs=output)
