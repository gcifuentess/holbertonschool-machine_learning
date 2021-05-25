#!/usr/bin/env python3

import numpy as np
f1_score = __import__('4-f1_score').f1_score

if __name__ == '__main__':
    training = np.array([[54, 2, 4], [5, 52, 3], [15, 4, 41]])
    validation = np.array([[53, 1, 6], [7, 51, 2], [15, 5, 40]])

    np.set_printoptions(suppress=True)
    print(f1_score(training))
    print(f1_score(validation))
