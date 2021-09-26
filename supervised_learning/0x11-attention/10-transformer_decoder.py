#!/usr/bin/env python3
'''Transformer Decoder module'''
import tensorflow as tf
positional_encoding = __import__('4-positional_encoding').positional_encoding
DecoderBlock = __import__('8-transformer_decoder_block').DecoderBlock


class Decoder(tf.keras.layers.Layer):
    '''creates the decoder for a transformer'''

    def __init__(self, N, dm, h, hidden, target_vocab, max_seq_len,
                 drop_rate=0.1):
        '''Decoder class constructor
        Args:
            N - the number of blocks in the decoder
            dm - the dimensionality of the model
            h - the number of heads
            hidden - the number of hidden units in the fully connected layer
            input_vocab - the size of the target vocabulary
            max_seq_len - the maximum sequence length possible
            drop_rate - the dropout rate

        Sets the following public instance attributes:
            N - the number of blocks in the decoder
            dm - the dimensionality of the model
            embedding - the embedding layer for the targets
            positional_encoding - a numpy.ndarray of shape (max_seq_len, dm)
                                  containing the positional encodings
            blocks - a list of length N containing all of the DecoderBlock‘s
            dropout - the dropout layer, to be applied to the positional
            encodings
        '''
        super().__init__()
        self.N = N
        self.dm = dm
        self.embedding = tf.keras.layers.Embedding(
            input_dim=target_vocab,
            output_dim=dm,
        )
        self.positional_encoding = positional_encoding(max_seq_len, dm)
        self.blocks = [DecoderBlock(dm, h, hidden, drop_rate)
                       for n in range(N)]
        self.dropout = tf.keras.layers.Dropout(rate=drop_rate)

    def call(self, x, encoder_output, training, look_ahead_mask, padding_mask):
        '''method to call the instance
        Args:
            x - a tensor of shape (batch, target_seq_len, dm) containing the
                input to the decoder
            encoder_output - a tensor of shape (batch, input_seq_len, dm)
                             containing the output of the encoder
            training - a boolean to determine if the model is training
            look_ahead_mask - the mask to be applied to the first multi head
                              attention layer
            padding_mask - the mask to be applied to the second multi head
                           attention layer

        Returns: a tensor of shape (batch, target_seq_len, dm) containing the
                 decoder output
        '''
        target_seq_len = x.shape[1]
        x = self.embedding(x)

        # see chapter "3.4 Embeddings and Softmax" of
        # "Attention Is All You Need" paper
        # https://arxiv.org/pdf/1706.03762.pdf :
        x *= tf.math.sqrt(tf.cast(self.dm, dtype=tf.float32))

        x += self.positional_encoding[:target_seq_len]

        x = self.dropout(x, training)

        for block in self.blocks:
            x = block(
                x,
                encoder_output,
                training,
                look_ahead_mask,
                padding_mask,
            )

        return x
