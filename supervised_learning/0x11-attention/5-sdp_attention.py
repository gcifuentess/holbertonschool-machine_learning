#!/usr/bin/env python3
'''Scaled Dot Product Attention'''
import tensorflow as tf


def sdp_attention(Q, K, V, mask=None):
    '''calculates the scaled dot product attention
    Args:
        Q is a tensor with its last two dimensions as (..., seq_len_q, dk)
          containing the query matrix
        K is a tensor with its last two dimensions as (..., seq_len_v, dk)
          containing the key matrix
        V is a tensor with its last two dimensions as (..., seq_len_v, dv)
          containing the value matrix
        mask is a tensor that can be broadcast into (..., seq_len_q, seq_len_v)
             containing the optional mask, or defaulted to None
            - if mask is not None, multiply -1e9 to the mask and add it to the
              scaled matrix multiplication

    Important: The preceding dimensions of Q, K, and V are the same

    Returns: output, weights
        output is a tensor with its last two dimensions as
               (..., seq_len_q, dv) containing the scaled dot product attention
        weights is a tensor with its last two dimensions as
                (..., seq_len_q, seq_len_v) containing the attention weights
    '''
    Q_K = tf.matmul(Q, K, transpose_b=True)
    dk = tf.cast(Q.shape[-1], dtype=tf.float32)
    Q_K_scaled = Q_K / tf.math.sqrt(dk)

    if mask is not None:
        Q_K_scaled += (mask * -1e9)

    weights = tf.nn.softmax(Q_K_scaled)
    attention = tf.matmul(weights, V)

    return attention, weights
