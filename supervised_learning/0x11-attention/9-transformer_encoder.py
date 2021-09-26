#!/usr/bin/env python3
'''Transformer Encoder module'''
import tensorflow as tf
positional_encoding = __import__('4-positional_encoding').positional_encoding
EncoderBlock = __import__('7-transformer_encoder_block').EncoderBlock


class Encoder(tf.keras.layers.Layer):
    '''creates the encoder for a transformer'''

    def __init__(self, N, dm, h, hidden, input_vocab, max_seq_len,
                 drop_rate=0.1):
        '''Encoder class constructor
        Args:
            N - the number of blocks in the encoder
            dm - the dimensionality of the model
            h - the number of heads
            hidden - the number of hidden units in the fully connected layer
            input_vocab - the size of the input vocabulary
            max_seq_len - the maximum sequence length possible
            drop_rate - the dropout rate

        Sets the following public instance attributes:
            N - the number of blocks in the encoder
            dm - the dimensionality of the model
            embedding - the embedding layer for the inputs
            positional_encoding - a numpy.ndarray of shape (max_seq_len, dm)
                                  containing the positional encodings
            blocks - a list of length N containing all of the EncoderBlock‘s
            dropout - the dropout layer, to be applied to the positional
            encodings
        '''
        super().__init__()
        self.N = N
        self.dm = dm
        self.embedding = tf.keras.layers.Embedding(
            input_dim=input_vocab,
            output_dim=dm,
        )
        self.positional_encoding = positional_encoding(max_seq_len, dm)
        self.blocks = [EncoderBlock(dm, h, hidden, drop_rate)
                       for n in range(N)]
        self.dropout = tf.keras.layers.Dropout(rate=drop_rate)

    def call(self, x, training, mask):
        '''method to call the instance
        Args:
            x - a tensor of shape (batch, input_seq_len, dm) containing the
                input to the encoder
            training - a boolean to determine if the model is training
            mask - the mask to be applied for multi head attention

        Returns: a tensor of shape (batch, input_seq_len, dm) containing the
                 encoder output
        '''
        input_seq_len = x.get_shape().as_list()[-1]
        x = self.embedding(x)

        # see chapter "3.4 Embeddings and Softmax" of
        # "Attention Is All You Need" paper
        # https://arxiv.org/pdf/1706.03762.pdf :
        x *= tf.math.sqrt(tf.cast(self.dm, dtype=tf.float32))

        pos_encoding = tf.cast(
            x=self.positional_encoding[:input_seq_len, :],
            dtype=tf.float32,
        )

        x += pos_encoding[tf.newaxis, :, :]
        x = self.dropout(x, training)

        for block in self.blocks:
            x = block(x, training, mask)

        return x
