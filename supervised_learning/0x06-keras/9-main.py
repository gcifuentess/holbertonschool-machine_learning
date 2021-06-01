#!/usr/bin/env python3
"""
Main file
"""

# Force Seed - fix for Keras
SEED = 0

import os
os.environ['PYTHONHASHSEED'] = str(SEED)
import random
random.seed(SEED)
import numpy as np
np.random.seed(SEED)
import tensorflow as tf
tf.set_random_seed(SEED)
import tensorflow.keras as K
session_conf = tf.ConfigProto(intra_op_parallelism_threads=1, inter_op_parallelism_threads=1)
sess = tf.Session(graph=tf.get_default_graph(), config=session_conf)
K.backend.set_session(sess)

# Imports
one_hot = __import__('3-one_hot').one_hot
train_model = __import__('8-train').train_model 
model = __import__('9-model')

if __name__ == '__main__':
    datasets = np.load('../data/MNIST.npz')
    X_train = datasets['X_train']
    X_train = X_train.reshape(X_train.shape[0], -1)
    Y_train = datasets['Y_train']
    Y_train_oh = one_hot(Y_train)
    X_valid = datasets['X_valid']
    X_valid = X_valid.reshape(X_valid.shape[0], -1)
    Y_valid = datasets['Y_valid']
    Y_valid_oh = one_hot(Y_valid)

    network = model.load_model('network1.h5')
    batch_size = 32
    epochs = 1000
    train_model(network, X_train, Y_train_oh, batch_size, epochs,
                validation_data=(X_valid, Y_valid_oh), early_stopping=True,
                patience=2, learning_rate_decay=True, alpha=0.001)
    model.save_model(network, 'network2.h5')
    network.summary()
    print(network.get_weights())
    del network

    network2 = model.load_model('network2.h5')
    network2.summary()
    print(network2.get_weights())

