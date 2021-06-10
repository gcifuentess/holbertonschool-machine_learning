#!/usr/bin/env python3
'''Convolutional Forward Prop module'''
import numpy as np


def conv(input_c, kernels, b, padding='same', stride=(1, 1)):
    '''performs a convolution on images using multiple kernels
    Args:
        input_c is a numpy.ndarray with shape (m, h, w, c) containing multiple
               units
               - m is the number of units
               - h is the height
               - w is the width
               - c is the number of channel
        kernels is a numpy.ndarray with shape (kh, kw, c, nc) containing the
               kernels for the convolution
               - kh is the height of the kernel
               - kw is the width of the kernel
               - c is the number of channels
               - nc is the number of kernels
        b is a numpy.ndarray of shape (1, 1, 1, c) containing the biases
           applied to the convolution
        padding is either a tuple of (ph, pw), ‘same’, or ‘valid’
                - if ‘same’, performs a same convolution
                - if ‘valid’, performs a valid convolution
                Important: the image will be padded with 0’s
        stride is a tuple of (sh, sw)
               - sh is the stride for the height
               - sw is the stride for the width
    Returns: a numpy.ndarray containing the convolved matrix
    '''
    m, ih, iw, ich = input_c.shape
    kh, kw, _, nk = kernels.shape
    sh, sw = stride

    if (padding == 'same'):
        ph = int(np.ceil(((ih - 1) * sh + kh - ih) / 2))  # padding height
        pw = int(np.ceil(((iw - 1) * sw + kw - iw) / 2))  # padding width
    elif (padding == 'valid'):
        ph = pw = 0

    oh = int(np.floor((ih + ph * 2 - kh) / sh) + 1)  # output matrix heght
    ow = int(np.floor((iw + pw * 2 - kw) / sw) + 1)  # output matrix width

    output = np.zeros([m, oh, ow, nk])  # convolution output
    input_padded = np.pad(input_c, [(0, 0), (ph, ph),
                                    (pw, pw), (0, 0)], mode="constant")

    h = 0
    for i in range(oh):
        w = 0
        for j in range(ow):
            h = i * sh
            w = j * sw
            current = input_padded[:, h: h + kh, w: w + kw, :]
            output[:, i, j, :] = np.tensordot(current, kernels,
                                              axes=([1, 2, 3],
                                                    [0, 1, 2])) + b
    return output


def conv_forward(A_prev, W, b, activation, padding="same", stride=(1, 1)):
    '''performs forward propagation over a convolutional layer of a neural
    network
    Args:
        A_prev is a numpy.ndarray of shape (m, h_prev, w_prev, c_prev)
               containing the output of the previous layer
            - m is the number of examples
            - h_prev is the height of the previous layer
            - w_prev is the width of the previous layer
            - c_prev is the number of channels in the previous layer
        W is a numpy.ndarray of shape (kh, kw, c_prev, c_new) containing the
          kernels for the convolution
            - kh is the filter height
            - kw is the filter width
            - c_prev is the number of channels in the previous layer
            - c_new is the number of channels in the output
        b is a numpy.ndarray of shape (1, 1, 1, c_new) containing the biases
          applied to the convolution
        activation is an activation function applied to the convolution
        padding is a string that is either same or valid, indicating the type
                of padding used
        stride is a tuple of (sh, sw) containing the strides for the
               convolution
            sh is the stride for the height
            sw is the stride for the width
    Returns: the output of the convolutional layer
    '''
    convolution = conv(A_prev, W, b, padding, stride)
    return activation(convolution)
