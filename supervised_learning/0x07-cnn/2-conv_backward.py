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
    m, dZh, dZw, f = dZ.shape
    m, ih, iw, ch = A_prev.shape
    kh, kw, ch, f = W.shape
    sh, sw = stride

    if (padding == 'same'):
        ph = int(np.ceil(((ih - 1) * sh + kh - ih) / 2))  # padding height
        pw = int(np.ceil(((iw - 1) * sw + kw - iw) / 2))  # padding width
    elif (padding == 'valid'):
        ph = pw = 0

    # 1) To calculate A_prev (input) gradient matrix:
    dA_prev = np.zeros_like(A_prev)  # dtype float32, needs transformation
    dA_prev = dA_prev.astype("float64")  # dtype transformation

    # 1.1) W rotation:
    Wr = np.rot90(m=W, k=2, axes=(0, 1))  # 180 degrees rotation

    # 1.2) dZ cero padding for convolution:
    pdZh = int(np.ceil(((ih - 1) * 1 + kh - dZh) / 2))  # padding height
    pdZw = int(np.ceil(((iw - 1) * 1 + kw - dZw) / 2))  # padding width
    dZ_pad = np.pad(dZ, ((0, 0),
                         (pdZh, pdZh),
                         (pdZw, pdZw),
                         (0, 0)), "constant")

    # 1.3) Convolution, with dZ padded and W rotated:
    for ch_ in range(ch):
        for k in range(ih):
            for l in range(iw):
                current = dZ_pad[:, k: k + kh, l: l + kw, :]
                dA_prev[:, k, l, ch_] = np.tensordot(current, Wr[..., ch_, :],
                                                     axes=([1, 2, 3],
                                                           [0, 1, 2]))

    # 2) To talculate W gradient matrix:
    dW = np.zeros_like(W)  # same shape as W
    A_prev_pad = np.pad(A_prev,
                        ((0,), (ph,), (pw,), (0,)),
                        mode="constant")  # input matrix padding

    # 2.1) Convolution (unefficient):
    for m_ in range(m):
        for f_ in range(f):
            for i in range(dZh):
                for j in range(dZw):
                    h = i * sh
                    w = j * sw
                    current = A_prev_pad[m_, h: h + kh, w: w + kw, :]
                    dW[..., f_] += np.multiply(current,
                                               dZ[m_, i, j, f_],
                                               dtype="float32")

    # 3) bias gradient vector:
    db = np.sum(dZ, axis=(0, 1, 2), keepdims=True)

    return dA_prev, dW, db
