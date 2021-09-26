#!/usr/bin/env python3
'''Transformer Decoder Block module'''
import tensorflow as tf
MultiHeadAttention = __import__('6-multihead_attention').MultiHeadAttention


class DecoderBlock(tf.keras.layers.Layer):
    '''creates an encoder block for a transformer'''

    def __init__(self, dm, h, hidden, drop_rate=0.1):
        '''DecoderBlock class constructor
        Args:
            dm - the dimensionality of the model
            h - the number of heads
            hidden - the number of hidden units in the fully connected layer
            drop_rate - the dropout rate

        Sets the following public instance attributes:
            mha1 - the first MultiHeadAttention layer
            mha2 - the second MultiHeadAttention layer
            dense_hidden - the hidden dense layer with hidden units and relu
                           activation
            dense_output - the output dense layer with dm units
            layernorm1 - the first layer norm layer, with epsilon=1e-6
            layernorm2 - the second layer norm layer, with epsilon=1e-6
            layernorm3 - the third layer norm layer, with epsilon=1e-6
            dropout1 - the first dropout layer
            dropout2 - the second dropout layer
            dropout3 - the third dropout layer
        '''
        super().__init__()
        self.mha1 = MultiHeadAttention(dm, h)
        self.mha2 = MultiHeadAttention(dm, h)
        self.dense_hidden = tf.keras.layers.Dense(hidden, activation='relu')
        self.dense_output = tf.keras.layers.Dense(dm)
        self.layernorm1 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
        self.layernorm2 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
        self.layernorm3 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
        self.dropout1 = tf.keras.layers.Dropout(rate=drop_rate)
        self.dropout2 = tf.keras.layers.Dropout(rate=drop_rate)
        self.dropout3 = tf.keras.layers.Dropout(rate=drop_rate)

    def call(self, x, encoder_output, training, look_ahead_mask,
             padding_mask):
        '''method to call the instance
        Args:
            x - a tensor of shape (batch, target_seq_len, dm)containing the
                input to the decoder block
            encoder_output - a tensor of shape (batch, input_seq_len, dm)
                             containing the output of the encoder
           training - a boolean to determine if the model is training
           look_ahead_mask - the mask to be applied to the first multi head
                             attention layer
           padding_mask - the mask to be applied to the second multi head
                          attention layer

        Returns: a tensor of shape (batch, target_seq_len, dm) containing the
                 block’s output

        Based on: https://www.tensorflow.org/text/tutorials/
                  transformer#decoder_layer
        '''
        # first sub-block:
        mha1, _ = self.mha1(x, x, x, look_ahead_mask)
        mha1 = self.dropout1(mha1, training=training)
        out1 = self.layernorm1(mha1 + x)  # skip conn and norm

        # second sub-block:
        mha2, _ = self.mha2(
            out1,  # Q
            encoder_output,  # K
            encoder_output,  # V
            padding_mask,
        )
        mha2 = self.dropout2(mha2, training=training)
        out2 = self.layernorm2(mha2 + out1)  # skip conn and norm

        # third sub-block
        linear = self.dense_hidden(out2)
        linear = self.dense_output(linear)
        linear = self.dropout3(linear, training=training)
        out3 = self.layernorm3(linear + out2)

        return out3
