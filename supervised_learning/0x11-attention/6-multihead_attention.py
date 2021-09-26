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
        self.depth = dm // h  # more precise than int(dm / h)
        self.Wq = tf.keras.layers.Dense(dm)
        self.Wk = tf.keras.layers.Dense(dm)
        self.Wv = tf.keras.layers.Dense(dm)
        self.linear = tf.keras.layers.Dense(dm)

    def split_into_heads(self, x, batch_size):
        '''splits x into self.h number of heads
        Args:
            x is a tensor of shape (batch seq_len, dm)
            batch_size is a tensorflow.python.framework.ops.Tensor that
                       holds the size of th batch

        Returns: a tensor of shape (batch, heads, seq_len, depth)
        '''
        x = tf.reshape(
            tensor=x,
            shape=(batch_size, -1, self.h, self.depth)
        )

        return tf.transpose(
            a=x,
            perm=[0, 2, 1, 3],
        )

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
        batch = tf.shape(Q)[0]

        # --- PREVIOUS VERSION ---
        # # shape (batch, seq_len_q, heads, depth):
        # Qi = tf.reshape(self.Wq(Q), (batch, -1, self.h, self.depth))
        # # shape (batch, heads, seq_len_q, depth):
        # Qi = tf.transpose(Qi, perm=[0, 2, 1, 3])

        # # shape (batch, seq_len_v, heads, depth):
        # Ki = tf.reshape(self.Wk(K), (batch, -1, self.h, self.depth))
        # # shape (batch, heads, seq_len_v, depth):
        # Ki = tf.transpose(Ki, perm=[0, 2, 1, 3])

        # # shape (batch, seq_len_v, heads, depth):
        # Vi = tf.reshape(self.Wv(V), (batch, -1, self.h, self.depth))
        # # shape (batch, heads, seq_len_v, depth):
        # Vi = tf.transpose(Vi, perm=[0, 2, 1, 3])
        # ---

        # --- NEW VERSION ---
        Qi = self.split_into_heads(self.Wq(Q), batch)
        Ki = self.split_into_heads(self.Wk(K), batch)
        Vi = self.split_into_heads(self.Wv(V), batch)
        # ---

        # scaled_attention shape (batch, heads, seq_len_q, depth) &
        # weights shape (batch, heads, seq_len_q, seq_len_v):
        scaled_attention, weights = sdp_attention(Qi, Ki, Vi, mask)

        # scaled_attention shape (batch, seq_len_q, heads, depth):
        scaled_attention = tf.transpose(scaled_attention, perm=[0, 2, 1, 3])
        # concat_attention shape (batch, seq_len_q, dm):
        concat_attention = tf.reshape(scaled_attention, (batch, -1, self.dm))

        # ouput shape (batch, seq_len_q, dm)
        output = self.linear(concat_attention)

        return output, weights
