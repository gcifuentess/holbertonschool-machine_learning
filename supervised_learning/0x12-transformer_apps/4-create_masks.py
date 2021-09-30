#!/usr/bin/env python3
'''Create Masks module
based on: https://www.tensorflow.org/text/tutorials/transformer#masking
'''
import tensorflow.compat.v2 as tf


def create_masks(inputs, target):
    '''creates all masks for training/validation
    Args:
        inputs is a tf.Tensor of shape (batch_size, seq_len_in) that contains
               the input sentence
        target is a tf.Tensor of shape (batch_size, seq_len_out) that contains
               the target sentence

    Returns: encoder_mask, combined_mask, decoder_mask
        encoder_mask is the tf.Tensor padding mask of shape
                     (batch_size, 1, 1, seq_len_in) to be applied in the
                     encoder
        combined_mask is the tf.Tensor of shape
                      (batch_size, 1, seq_len_out, seq_len_out) used in the 1st
                      attention block in the decoder to pad and mask future
                      tokens in the input received by the decoder. It takes the
                      maximum between a look ahead mask and the decoder target
                      padding mask.
        decoder_mask is the tf.Tensor padding mask of shape
                     (batch_size, 1, 1, seq_len_in) used in the 2nd attention
                     block in the decoder.

    Concept: Mask all the pad tokens in the batch of sequence. It ensures that
             the model does not treat padding as the input. The mask indicates
             where pad value 0 is present: it outputs a 1 at those locations,
             and a 0 otherwise.
    '''
    encoder_mask = tf.cast(tf.math.equal(inputs, 0), tf.float32)
    encoder_mask = encoder_mask[:, tf.newaxis, tf.newaxis, :]

    decoder_mask = tf.cast(tf.math.equal(inputs, 0), tf.float32)
    decoder_mask = decoder_mask[:, tf.newaxis, tf.newaxis, :]

    dec_targ_mask = tf.cast(tf.math.equal(inputs, 0), tf.float32)
    dec_targ_mask = dec_targ_mask[:, tf.newaxis, tf.newaxis, :]

    seq_len_out = tf.shape(target)[1]
    mask_shape = (seq_len_out, seq_len_out)
    look_ahead_mask = 1 - tf.linalg.band_part(tf.ones(mask_shape), -1, 0)
    combined_mask = tf.maximum(dec_targ_mask, look_ahead_mask)

    return encoder_mask, combined_mask, decoder_mask
