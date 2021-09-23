#!/usr/bin/env python3
'''RNN Encoder module'''
import tensorflow as tf


class RNNEncoder(tf.keras.layers.Layer):
    '''inherits from tensorflow.keras.layers.Layer to encode for machine
    translation'''

    def __init__(self, vocab, embedding, units, batch):
        '''RNNEncoder constructor
        Args:
            vocab is an integer representing the size of the input vocabulary
            embedding is an integer representing the dimensionality of the
                      embedding vector
            units is an integer representing the number of hidden units in the
                  RNN cell
            batch is an integer representing the batch size

        Sets the following public instance attributes:
            batch as the batch size
            units as the number of hidden units in the RNN cell
            embedding as a keras Embedding layer that converts words from the
                        vocabulary into an embedding vector
            gru as a keras GRU layer with units units
                  - return both the full sequence of outputs as well as the
                            last hidden state
                  - Recurrent weights initialized with glorot_uniform
        '''
        super().__init__()
        self.batch = batch
        self.units = units
        self.embedding = tf.keras.layers.Embedding(
            input_dim=vocab,
            output_dim=embedding,
        )
        self.gru = tf.keras.layers.GRU(
            units=units,
            recurrent_initializer="glorot_uniform",
            return_sequences=True,
            return_state=True,
        )

    def initialize_hidden_state(self):
        '''Initializes the hidden states for the RNN cell to a tensor of zeros

        Returns a tensor of shape (batch, units)containing the initialized
                hidden states
        '''
        initializer = tf.keras.initializers.Zeros()
        return initializer(shape=(self.batch, self.units))

    def __call__(self, x, initial):
        '''method to call the instance
        Args:
            x is a tensor of shape (batch, input_seq_len) containing the input
              to the encoder layer as word indices within the vocabulary
        initial is a tensor of shape (batch, units) containing the initial
                hidden state

        Returns: outputs, hidden
            - outputs is a tensor of shape (batch, input_seq_len, units)
                      containing the outputs of the encoder
            - hidden is a tensor of shape (batch, units) containing the last
                     hidden state of the encoder
        '''
        embeds = self.embedding(x)
        outputs, hidden = self.gru(inputs=embeds, initial_state=initial)

        return outputs, hidden
