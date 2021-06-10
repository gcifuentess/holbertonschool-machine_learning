#!/usr/bin/env python3
'''Convolutional Back Prop module'''
import numpy as np


def conv_backward(dZ, A_prev, W, b, padding="same", stride=(1, 1)):
    '''performs back propagation over a convolutional layer of a neural
    network
    Args:
        dZ is a numpy.ndarray of shape (m, h_new, w_new, c_new) containing
           the partial derivatives with respect to the unactivated output of
           the convolutional layer
            - m is the number of examples
            - h_new is the height of the output
            - w_new is the width of the output
            - c_new is the number of channels in the output
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
        padding is a string that is either same or valid, indicating the type
                of padding used
        stride is a tuple of (sh, sw) containing the strides for the
               convolution
            sh is the stride for the height
            sw is the stride for the width
    Returns: the partial derivatives with respect to the previous layer
             (dA_prev), the kernels (dW), and the biases (db), respectively
    '''
    m, dZh, dZw, dZch = dZ.shape
    _, ih, iw, ich = A_prev.shape
    kh, kw, kch, f = W.shape
    sh, sw = stride

    if (padding == 'same'):
        ph = int(np.ceil(((ih - 1) * sh + kh - ih) / 2))  # padding height
        pw = int(np.ceil(((iw - 1) * sw + kw - iw) / 2))  # padding width
    elif (padding == 'valid'):
        ph = pw = 0

    dA_prev = np.zeros_like(A_prev)
    dW = np.zeros_like(W)
    db = np.zeros_like(b)

    A_prev_pad = np.pad(A_prev, ((0, ), (ph,), (pw,), (0,)), "constant")

    for m_ in range(m):
        for f_ in range(f):
            for k in range(kh):
                for l in range(kw):
                    for i in range(dZh):
                        for j in range(dZw):
                            for c in range(kch):
                                dW[k, l, c, f_] = (A_prev_pad[m_, sh * k + i,
                                                              sw * l + j, c] *
                                                   dZ[m_, i, j, f_])

    dZ_pad = np.pad(dZ, ((0,), (kh - 1,), (kw - 1, ), (0,)), "constant")
    dA_prev_pad = np.pad(A_prev, ((0, ), (ph,), (pw,), (0,)), "constant")
    Wr = np.rot90(m=W, k=2, axes=(0, 1))  # 180 degrees rotation

    for m_ in range(m):
        for f_ in range(f):
            for k in range(ih + 2 * ph):
                for l in range(iw + 2 * pw):
                    for i in range(kh):
                        for j in range(kw):
                            for c in range(kch):
                                dA_prev_pad[m_, k, l, c] = (dZ_pad[m_, k + i,
                                                                   l + j, f_] *
                                                            Wr[i, j, c, f_])
    dA_prev_pad = dA_prev_pad[:, ph:-ph, pw:-pw, :]

    db = np.sum(dZ, axis=(0, 1, 2))

    return dA_prev, dW, b
