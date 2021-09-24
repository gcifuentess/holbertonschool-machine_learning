#!/usr/bin/env python3
'''Self Attention module'''
import tensorflow as tf


class SelfAttention(tf.keras.layers.Layer):
    '''to calculate the attention for machine translation'''

    def __init__(self, units):
        '''SeflAttention constructor
        Args:
            units is an integer representing the number of hidden units in the
                  alignment model

        Sets the following public instance attributes:
            W as a Dense layer with units units, to be applied to the previous
                decoder hidden state
            U as a Dense layer with units units, to be applied to the encoder
                hidden states
            V as a Dense layer with 1 units, to be applied to the tanh of the
                sum of the outputs of W and U
        '''
        super().__init__()
        self.W = tf.keras.layers.Dense(units=units)
        self.U = tf.keras.layers.Dense(units=units)
        self.V = tf.keras.layers.Dense(units=1)

    def call(self, s_prev, hidden_states):
        '''method to call the instance
        Args:
            s_prev is a tensor of shape (batch, units) containing the previous
                   decoder hidden state
            hidden_states is a tensor of shape (batch, input_seq_len, units)
                          containing the outputs of the encoder

        Returns: context, weights
            - context is a tensor of shape (batch, units) that contains the
                      context vector for the decoder
            - weights is a tensor of shape (batch, input_seq_len, 1) that
                      contains the attention weights
        '''
        s_prev = tf.expand_dims(s_prev, 1)
        W_s = self.W(s_prev)
        U_h = self.U(hidden_states)
        aligment_model = self.V(tf.nn.tanh(W_s + U_h))
        attention_weights = tf.nn.softmax(aligment_model, axis=1)
        context = tf.reduce_sum(attention_weights * hidden_states, axis=1)

        return context, attention_weights
