#!/usr/bin/env python3
'''Vanilla Autoencoder module'''
import tensorflow.keras as keras


def autoencoder(input_dims, hidden_layers, latent_dims):
    '''creates an autoencoder
    Args:
        input_dims is an integer containing the dimensions of the model input
        hidden_layers is a list containing the number of nodes for each hidden
                      layer in the encoder, respectively
            * the hidden layers should be reversed for the decoder
        latent_dims is an integer containing the dimensions of the latent space
                    representation

    Returns: encoder, decoder, auto
        encoder is the encoder model
        decoder is the decoder model
        auto is the full autoencoder model
    '''
    inputs_aut = keras.Input(shape=(input_dims,))
    dense_layers_aut = []
    len_hl = len(hidden_layers)

    # encoder part:
    for i in range(len_hl + 1):

        if (i < len_hl):
            units = hidden_layers[i]
        else:
            units = latent_dims

        if (i > 0):
            x_aut = dense_layers_aut[-1]
        else:
            x_aut = inputs_aut

        layer_aut = keras.layers.Dense(
            units=units,
            activation='relu',
         )(x_aut)

        dense_layers_aut.append(layer_aut)

    # decoder part:
    for j in range(len_hl + 1):

        if (j < len_hl):
            units = hidden_layers[-j - 1]
        elif (j == 0):
            units = latent_dims
        else:
            units = input_dims

        x_aut = dense_layers_aut[-1]

        if (j < len_hl):
            activation = 'relu'
        else:
            activation = 'sigmoid'

        layer_aut = keras.layers.Dense(
            units=units,
            activation=activation,
        )(x_aut)

        dense_layers_aut.append(layer_aut)

    # autoencoder model:
    auto = keras.Model(inputs=inputs_aut, outputs=dense_layers_aut[-1])
    auto.compile(
        optimizer='Adam',
        loss="binary_crossentropy"
    )

    inputs_enc = auto.input
    for k, layer in enumerate(auto.layers):

        if (k > i + 2):
            outputs_dec = layer(outputs_dec)
        elif (k == i + 2):
            inputs_dec = keras.Input(shape=(latent_dims,))
            outputs_dec = layer(inputs_dec)
        elif (k == i + 1):
            outputs_enc = layer.output

    encoder = keras.Model(inputs=inputs_enc, outputs=outputs_enc)
    decoder = keras.Model(inputs=inputs_dec, outputs=outputs_dec)

    return encoder, decoder, auto
