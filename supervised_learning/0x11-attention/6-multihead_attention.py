#!/usr/bin/env python3
'''Multi Head Attention module'''
import tensorflow as tf
sdp_attention = __import__('5-sdp_attention').sdp_attention


class MultiHeadAttention(tf.keras.layers.Layer):
    '''performs multi head attention'''

    def __init__(self, dm, h):
        '''MultiHeadAttention class constructor
        Args:
            dm is an integer representing the dimensionality of the model
            h is an integer representing the number of heads
            dm is divisible by h

        Sets the following public instance attributes:
            h - the number of heads
            dm - the dimensionality of the model
            depth - the depth of each attention head
            Wq - a Dense layer with dm units, used to generate the query matrix
            Wk - a Dense layer with dm units, used to generate the key matrix
            Wv - a Dense layer with dm units, used to generate the value matrix
            linear - a Dense layer with dm units, used to generate the
                     attention output
        '''
        super().__init__()
        self.h = h
        self.dm = dm
        self.depth = int(dm / h)
        self.Wq = tf.keras.layers.Dense(dm)
        self.Wk = tf.keras.layers.Dense(dm)
        self.Wv = tf.keras.layers.Dense(dm)
        self.linear = tf.keras.layers.Dense(dm)

    def call(self, Q, K, V, mask):
        '''method to call the instance
        Args:
            Q is a tensor of shape (batch, seq_len_q, dk) containing the input
              to generate the query matrix
            K is a tensor of shape (batch, seq_len_v, dk) containing the input
              to generate the key matrix
            V is a tensor of shape (batch, seq_len_v, dv) containing the input
              to generate the value matrix
            mask is always None

        Returns: output, weights
            output a tensor with its last two dimensions as
                   (..., seq_len_q, dm) containing the scaled dot product
                   attention
            weights a tensor with its last three dimensions as
                    (..., h, seq_len_q, seq_len_v) containing the attention
                    weights
        '''
        batch = Q.shape[0]

        # shape (batch, seq_len_q, heads, depth):
        Qi = tf.reshape(self.Wq(Q), (batch, -1, self.h, self.depth))
        # shape (batch, heads, seq_len_q, depth):
        Qi = tf.transpose(Qi, perm=[0, 2, 1, 3])

        # shape (batch, seq_len_v, heads, depth):
        Ki = tf.reshape(self.Wk(K), (batch, -1, self.h, self.depth))
        # shape (batch, heads, seq_len_v, depth):
        Ki = tf.transpose(Ki, perm=[0, 2, 1, 3])

        # shape (batch, seq_len_v, heads, depth):
        Vi = tf.reshape(self.Wv(V), (batch, -1, self.h, self.depth))
        # shape (batch, heads, seq_len_v, depth):
        Vi = tf.transpose(Vi, perm=[0, 2, 1, 3])

        # output shape (batch, heads, seq_len_q, depth) &
        # weights shape (batch, heads, seq_len_q, seq_len_v):
        output, weights = sdp_attention(Qi, Ki, Vi, mask)

        # output shape (batch, seq_len_q, heads, depth):
        output = tf.transpose(output, perm=[0, 2, 1, 3])
        # output shape (batch, seq_len_q, dm):
        output = tf.reshape(output, (batch, -1, self.dm))

        output = self.linear(output)

        return output, weights
