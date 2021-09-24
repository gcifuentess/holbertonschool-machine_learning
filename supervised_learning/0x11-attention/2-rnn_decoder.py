#!/usr/bin/env python3
'''RNN Decoder module'''
import tensorflow as tf


class RNNDecoder(tf.keras.layers.Layer):
    '''decode for machine translation'''

    def __init__(self, vocab, embedding, units, batch):
        '''RNNDecoder class constructor
        Args:
            vocab is an integer representing the size of the output vocabulary
            embedding is an integer representing the dimensionality of the
                      embedding vector
            units is an integer representing the number of hidden units in the
                  RNN cell
            batch is an integer representing the batch size

        Sets the following public instance attributes:
            embedding as a keras Embedding layer that converts words from the
                         vocabulary into an embedding vector
            gru as a keras GRU layer with units units
                - Should return both the full sequence of outputs as well as
                  the last hidden state
                - Recurrent weights should be initialized with glorot_uniform
            F as a Dense layer with vocab units
        '''
        super().__init__()
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
        self.F = tf.keras.layers.Dense(units=vocab)

    def call(self, x, s_prev, hidden_states):
        '''method to call the instance
        Args:
            x is a tensor of shape (batch, 1) containing the previous word in
              the target sequence as an index of the target vocabulary
            s_prev is a tensor of shape (batch, units) containing the previous
                   decoder hidden state
            hidden_states is a tensor of shape (batch, input_seq_len, units)
                          containing the outputs of the encoder

        Returns: y, s
            - y is a tensor of shape (batch, vocab) containing the output word
                as a one hot vector in the target vocabulary
            - s is a tensor of shape (batch, units) containing the new decoder
                hidden state
        '''
        SelfAttention = __import__('1-self_attention').SelfAttention

        _, units = s_prev.shape
        context, weights = SelfAttention(units)(s_prev, hidden_states)

        embed = self.embedding(x)
        context = tf.expand_dims(context, 1)

        concat = tf.concat([context, embed], axis=2)
        outputs, hidden = self.gru(inputs=concat)
        outputs = tf.reshape(outputs, (outputs.shape[0], outputs.shape[2]))
        y = self.F(outputs)

        return y, hidden
