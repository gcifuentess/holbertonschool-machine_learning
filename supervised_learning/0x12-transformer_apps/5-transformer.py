#!/usr/bin/env python3
'''Transformer Network module'''
import tensorflow as tf
import numpy as np


class Transformer(tf.keras.Model):
    '''creates a transformer network'''

    def __init__(self, N, dm, h, hidden, input_vocab, target_vocab,
                 max_seq_input, max_seq_target, drop_rate=0.1):
        '''Transformer class constructor
        Args:
            N - the number of blocks in the encoder and decoder
            dm - the dimensionality of the model
            h - the number of heads
            hidden - the number of hidden units in the fully connected layers
            input_vocab - the size of the input vocabulary
            target_vocab - the size of the target vocabulary
            max_seq_input - the maximum sequence length possible for the input
            max_seq_target - the maximum sequence length possible for the
                             target
            drop_rate - the dropout rate

        Sets the following public instance attributes:
            encoder - the encoder layer
            decoder - the decoder layer
            linear - a final Dense layer with target_vocab units
        '''
        super(Transformer, self).__init__()
        self.encoder = Encoder(
            N=N,
            dm=dm,
            h=h,
            hidden=hidden,
            input_vocab=input_vocab,
            max_seq_len=max_seq_input,
            drop_rate=drop_rate,
        )
        self.decoder = Decoder(
            N=N,
            dm=dm,
            h=h,
            hidden=hidden,
            target_vocab=target_vocab,
            max_seq_len=max_seq_target,
            drop_rate=drop_rate,
        )
        self.linear = tf.keras.layers.Dense(target_vocab)

    def call(self, inputs, target, training, encoder_mask, look_ahead_mask,
             decoder_mask):
        '''method to call the instance
        Args:
            inputs - a tensor of shape (batch, input_seq_len) containing the
                     inputs
            target - a tensor of shape (batch, target_seq_len) containing the
                     target
            training - a boolean to determine if the model is training
            encoder_mask - the padding mask to be applied to the encoder
            look_ahead_mask - the look ahead mask to be applied to the decoder
            decoder_mask - the padding mask to be applied to the decoder
        Returns: a tensor of shape (batch, target_seq_len, target_vocab)
                 containing the transformer output
        '''
        encoder_out = self.encoder(
            inputs,
            training,
            encoder_mask,
        )
        decoder_out = self.decoder(
            target,
            encoder_out,
            training,
            look_ahead_mask,
            decoder_mask,
        )

        return self.linear(decoder_out)


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
        input_seq_len = x.shape[1]
        x = self.embedding(x)

        # see chapter "3.4 Embeddings and Softmax" of
        # "Attention Is All You Need" paper
        # https://arxiv.org/pdf/1706.03762.pdf :
        x *= tf.math.sqrt(tf.cast(self.dm, dtype=tf.float32))

        x += self.positional_encoding[:input_seq_len]

        x = self.dropout(x, training)

        for block in self.blocks:
            x = block(x, training, mask)

        return x


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


class EncoderBlock(tf.keras.layers.Layer):
    '''creates an encoder block for a transformer'''

    def __init__(self, dm, h, hidden, drop_rate=0.1):
        '''EncoderBlock class constructor
        Args:
            dm - the dimensionality of the model
            h - the number of heads
            hidden - the number of hidden units in the fully connected layer
            drop_rate - the dropout rate
        Sets the following public instance attributes:
            mha - a MultiHeadAttention layer
            dense_hidden - the hidden dense layer with hidden units and relu
                           activation
            dense_output - the output dense layer with dm units
            layernorm1 - the first layer norm layer, with epsilon=1e-6
            layernorm2 - the second layer norm layer, with epsilon=1e-6
            dropout1 - the first dropout layer
            dropout2 - the second dropout layer
        '''
        super(EncoderBlock, self).__init__()
        self.mha = MultiHeadAttention(dm, h)
        self.dense_hidden = tf.keras.layers.Dense(hidden, activation='relu')
        self.dense_output = tf.keras.layers.Dense(dm)
        self.layernorm1 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
        self.layernorm2 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
        self.dropout1 = tf.keras.layers.Dropout(rate=drop_rate)
        self.dropout2 = tf.keras.layers.Dropout(rate=drop_rate)

    def call(self, x, training, mask=None):
        '''method to call the instance
        Args:
            x - a tensor of shape (batch, input_seq_len, dm) containing the
                input to the encoder block
            training - a boolean to determine if the model is training
            mask - the mask to be applied for multi head attention
        Returns: a tensor of shape (batch, input_seq_len, dm) containing the
                 block’s output
        '''
        # first sub-block:
        attn_output, _ = self.mha(x, x, x, mask)
        attn_output = self.dropout1(attn_output, training=training)
        out1 = self.layernorm1(x + attn_output)  # skip conn and normalization

        # second sub-block:
        ffn_output = self.dense_hidden(out1)
        ffn_output = self.dense_output(ffn_output)
        ffn_output = self.dropout2(ffn_output, training=training)
        out2 = self.layernorm2(out1 + ffn_output)  # skip conn and norm

        return out2


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

        # --- NEW VERSION ---
        Qi = self.Wq(Q)
        Ki = self.Wk(K)
        Vi = self.Wv(V)

        Qi = self.split_into_heads(Qi, batch)
        Ki = self.split_into_heads(Ki, batch)
        Vi = self.split_into_heads(Vi, batch)
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
    dk = tf.cast(tf.shape(Q)[-1], dtype=tf.float32)
    Q_K_scaled = Q_K / tf.math.sqrt(dk)

    if mask is not None:
        Q_K_scaled += mask * -1e9

    weights = tf.nn.softmax(Q_K_scaled)
    attention = tf.matmul(weights, V)

    return attention, weights


def positional_encoding(max_seq_len, dm):
    '''calculates the positional encoding for a transformer
    Args:
        max_seq_len is an integer representing the maximum sequence length
        dm is the model depth
    Returns: a numpy.ndarray of shape (max_seq_len, dm) containing the
             positional encoding vectors
    '''
    PE = np.zeros((max_seq_len, dm))
    even = np.array([x for x in range(0, dm, 2)])
    pos = np.arange(max_seq_len)

    PE[:, ::2] = np.sin(pos[:, np.newaxis] / np.power(10000, even / dm))
    PE[:, 1::2] = np.cos(pos[:, np.newaxis] / np.power(10000, even / dm))

    return PE
