#!/usr/bin/env python3
'''ResNet-50 module'''
import tensorflow.keras as K
identity_block = __import__('2-identity_block').identity_block
projection_block = __import__('3-projection_block').projection_block


def resnet50():
    '''Builds the ResNet-50 architecture as described in Deep Residual
    Learning for Image Recognition (2015)
    Important: Input data must be of shape (224, 224, 3)
    Returns: the keras model
    '''
    # block filters:
    block1 = [64, 64, 256]
    block2 = [128, 128, 512]
    block3 = [256, 256, 1024]
    block4 = [512, 512, 2048]

    # number of blocks stacked:
    blocks = [3, 4, 6, 3]

    # strides per block:
    strides = [1, 2, 2, 2]

    w = K.initializers.he_normal()

    inputs = K.Input(shape=(224, 224, 3))

    l1 = K.layers.Conv2D(filters=64,
                         kernel_size=(7, 7),
                         strides=2,
                         padding="same",
                         kernel_initializer=w)(inputs)

    l2 = K.layers.BatchNormalization()(l1)
    l2 = K.layers.Activation("relu")(l2)

    l3 = K.layers.MaxPool2D(pool_size=(3, 3),
                            strides=2,
                            padding="same")(l2)

    l4 = projection_block(l3, block1, strides[0])
    for i in range(blocks[0] - 1):
        l4 = identity_block(l4, block1)

    l5 = projection_block(l4, block2, strides[1])
    for i in range(blocks[1] - 1):
        l5 = identity_block(l5, block2)

    l6 = projection_block(l5, block3, strides[2])
    for i in range(blocks[2] - 1):
        l6 = identity_block(l6, block3)

    l7 = projection_block(l6, block4, strides[3])
    for i in range(blocks[3] - 1):
        l7 = identity_block(l7, block4)

    l8 = K.layers.AveragePooling2D(pool_size=(7, 7),
                                   strides=1,
                                   padding="valid")(l7)

    output = K.layers.Dense(units=1000,
                            activation="softmax",
                            kernel_initializer=w)(l8)

    return K.Model(inputs=inputs, outputs=output)
