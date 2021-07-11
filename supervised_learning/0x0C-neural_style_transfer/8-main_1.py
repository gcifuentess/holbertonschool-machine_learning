#!/usr/bin/env python3

import numpy as np
import tensorflow as tf
NST = __import__('9-neural_style').NST


if __name__ == '__main__':
    np.random.seed(0)
    style_image = np.random.uniform(0, 256, size=(1000, 1000, 3))
    content_image = np.random.uniform(0, 256, size=(500, 1000, 3))
    print(style_image.shape)
    print(content_image.shape)

    nst = NST(style_image, content_image)
    tf.set_random_seed(0)
    generated_image = tf.random_uniform(nst.content_image.shape)
    print(generated_image.shape)
    grads, J, Js, Jc = nst.compute_grads(generated_image)
    print(grads.numpy())
    print(J.numpy())
    print(Js.numpy())
    print(Jc.numpy())
