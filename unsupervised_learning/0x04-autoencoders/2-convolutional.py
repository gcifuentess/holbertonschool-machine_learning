#!/usr/bin/env python3
'''Convolutional Autoencoder'''
import tensorflow.keras as keras


def autoencoder(input_dims, filters, latent_dims):
    '''creates an autoencoder
    Args:
        input_dims is a tuple of integers containing the dimensions of the
                   model input
        filters is a list containing the number of filters for each
                convolutional layer in the encoder, respectively
            * the filters should be reversed for the decoder
        latent_dims is a tuple of integers containing the dimensions of the
                    latent space representation

    Returns: encoder, decoder, auto
        encoder is the encoder model
        decoder is the decoder model
        auto is the full autoencoder model
    '''
    kernel_size = (3, 3)
    pool_size = (2, 2)

    inputs_enc = keras.Input(shape=input_dims)
    layer = None
    len_filters = len(filters)

    # encoder part:
    for i in range(len_filters):

        filter_ = filters[i - 1]

        if (i > 0):
            x = layer
        else:
            x = inputs_enc

        layer = keras.layers.Conv2D(
            filters=filter_,
            kernel_size=kernel_size,
            padding='same',
            activation='relu',
         )(x)

        layer = keras.layers.MaxPooling2D(
            pool_size=pool_size,
            padding="same",
        )(layer)

    encoded = layer

    inputs_dec = keras.Input(shape=latent_dims)

    # decoder part:
    for j in range(len_filters + 1):

        if (j < len_filters):
            filter_ = filters[-j - 1]

        if (j > 0):
            x = layer
        else:
            x = inputs_dec

        if (j < len_filters):
            activation = 'relu'
        else:
            activation = 'sigmoid'
            filter_ = input_dims[2]

        if (j == len_filters - 1):
            padding = 'valid'
        else:
            padding = 'same'

        layer = keras.layers.Conv2D(
            filters=filter_,
            kernel_size=kernel_size,
            padding=padding,
            activation=activation,
         )(x)

        decoded = layer

        layer = keras.layers.UpSampling2D(
            size=pool_size,
        )(layer)

    encoder = keras.Model(inputs=inputs_enc, outputs=encoded)
    decoder = keras.Model(inputs=inputs_dec, outputs=decoded)

    # autoencoder model:
    auto = keras.Model(inputs=inputs_enc, outputs=decoder(encoder(inputs_enc)))
    auto.compile(
        optimizer='Adam',
        loss="binary_crossentropy",
    )

    return encoder, decoder, auto
