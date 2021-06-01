#!/usr/bin/env python3
'''Learning Rate Decay module'''
import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, early_stopping=False,
                patience=0, learning_rate_decay=False, alpha=0.1,
                decay_rate=1, verbose=True, shuffle=False):
    '''trains a model using mini-batch gradient descent
    Args:
        network is the model to train
        data is a numpy.ndarray of shape (m, nx) containing the input data
        labels is a one-hot numpy.ndarray of shape (m, classes) containing
               the labels of data
        batch_size is the size of the batch used for mini-batch gradient
                   descent
        epochs is the number of passes through data for mini-batch gradient
               descent
        validation_data is the data to validate the model with, if not None
        early_stopping is a boolean that indicates whether early stopping
                       should be used
                       - only performed if validation_data exists
                       - based on validation loss
        patience is the patience used for early stopping
        learning_rate_decay is a boolean that indicates whether learning rate
                            decay should be used
                            - only performed if validation_data exists
                            - performed using inverse time decay
                            - decays in a stepwise fashion after each epoch
                            - each time the learning rate updates, Keras
                              prints a message
        alpha is the initial learning rate
        decay_rate is the decay rate
        verbose is a boolean that determines if output should be printed
                during training
        shuffle is a boolean that determines whether to shuffle the batches
                every epoch. Normally, it is a good idea to shuffle, but for
                reproducibility, we have chosen to set the default to False.
    Returns: the History object generated after training the model
    '''
    callbacks = []
    if validation_data:
        if early_stopping:
            early_stop = K.callbacks.EarlyStopping(monitor='val_loss',
                                                   patience=patience)
            callbacks.append(early_stop)
        if learning_rate_decay:
            def schedule(step):
                '''stepwise inverse time decay function'''
                return alpha * 1 / (1 + decay_rate * step)
            lr_decay = K.callbacks.LearningRateScheduler(schedule=schedule,
                                                         verbose=1)
            callbacks.append(lr_decay)
    return network.fit(x=data,
                       y=labels,
                       batch_size=batch_size,
                       validation_data=validation_data,
                       epochs=epochs,
                       verbose=verbose,
                       callbacks=callbacks,
                       shuffle=shuffle)
