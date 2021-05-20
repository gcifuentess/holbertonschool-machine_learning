#!/usr/bin/env python3
'''Learning Rate Decay module'''
import numpy as np


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    '''updates the learning rate using inverse time decay
    Args:
        alpha is the original learning rate
        decay_rate is the weight used to determine the rate at which alpha
                   will decay
        global_step is the number of passes of gradient descent that have
                    elapsed
        decay_step is the number of passes of gradient descent that should
                   occur before alpha is decayed further
    Returns: the updated value for alpha

    Important: the learning rate decay occurs in a stepwise fashion
    '''
    lr = alpha * 1 / (1 + decay_rate * int(global_step / decay_step))
    return lr
