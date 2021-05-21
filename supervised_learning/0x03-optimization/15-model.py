#!/usr/bin/env python3
'''tensorflow deep neural network model module'''
import tensorflow as tf
import numpy as np


def shuffle_data(X, Y):
    '''shuffles the data points in two matrices the same way
    Args:
        X is the first numpy.ndarray of shape (m, nx) to shuffle
            m is the number of data points
            nx is the number of features in X
        Y is the second numpy.ndarray of shape (m, ny) to shuffle
            m is the same number of data points as in X
            ny is the number of features in Y
    Returns: the shuffled X and Y matrices
    '''
    shuffle = np.random.permutation(X.shape[0])
    return X[shuffle], Y[shuffle]


def create_placeholders(nx, classes):
    '''create two placeholders, x and y, for the neural network
    Args:
        nx: the number of feature columns in our data
        classes: the number of classes in our classifier
    Return: placeholders named x and y, respectively
            - x: is the placeholder for the input data to the neural network
            - y: is the placeholder for the one-hot labels for the input data
    '''
    x = tf.placeholder(tf.float32, shape=(None, nx), name='x')
    y = tf.placeholder(tf.float32, shape=(None, classes), name='y')
    return x, y


def create_layer(prev, n, activation):
    '''Creates a tensorflow layer
    Args:
              prev: is the tensor output of the previous layer
                 n: is the number of nodes in the layer to create
        activation: is the activation function that the layer should use
    Return: the tensor output of the layer
    '''
    W = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    layer = tf.layers.Dense(n, activation=activation, kernel_initializer=W,
                            name='layer')
    return layer(prev)


def create_batch_norm_layer(prev, n, activation):
    '''creates a batch normalization layer for a neural network in tensorflow
    Args:
        prev is the activated output of the previous layer
        n is the number of nodes in the layer to be created
    activation is the activation function that should be used on the
                   output of the layer
    Returns: a tensor of the activated output for the layer
    '''
    w = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    layer = tf.layers.Dense(n, kernel_initializer=w, name="norm_layer")
    mean, var = tf.nn.moments(layer(prev), axes=0)
    beta = tf.Variable(tf.zeros(n), trainable=True)
    gamma = tf.Variable(tf.ones(n), trainable=True)
    epsilon = 1e-8
    norm = tf.nn.batch_normalization(x=layer(prev),
                                     mean=mean,
                                     variance=var,
                                     offset=beta,
                                     scale=gamma,
                                     variance_epsilon=epsilon,
                                     name="batch_norm")
    if activation:
        a = activation(norm)
    else:
        a = norm
    return a


def forward_prop(x, layer_sizes=[], activations=[]):
    '''creates the forward propagation graph for the neural network
    Args:
                  x: is the placeholder for the input data
        layer_sizes: is a list containing the number of nodes in each layer
                     of the network
        activations: is a list containing the activation functions for each
                     layer of the network
    Return: the prediction of the network in tensor form
    '''
    current_x = x
    for i in range(len(layer_sizes)):
        if activations[i]:
            current_x = create_batch_norm_layer(current_x,
                                                layer_sizes[i],
                                                activations[i])
        else:
            current_x = create_layer(current_x,
                                     layer_sizes[i],
                                     activations[i])
    return current_x


def calculate_loss(y, y_pred):
    '''calculates the softmax cross-entropy loss of a prediction
    Args:
        y: is a placeholder for the labels of the input data
        y_pred: is a tensor containing the network’s predictions
    Return: a tensor containing the loss of the prediction
    '''
    return tf.losses.softmax_cross_entropy(y, y_pred)


def calculate_accuracy(y, y_pred):
    '''calculates the accuracy of a prediction
    Args:
        y: is a placeholder for the labels of the input data
        y_pred: is a tensor containing the network’s predictions
    Return: a tensor containing the decimal accuracy of the prediction
    '''
    check = tf.equal(tf.argmax(y, 1), tf.argmax(y_pred, 1))
    cast = tf.cast(check, tf.float32)
    mean = tf.reduce_mean(cast, name="Mean")
    return mean


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    '''creates a learning rate decay operation in tensorflow using inverse
    time decay
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
    lrd = tf.train.inverse_time_decay(learning_rate=alpha,
                                      global_step=global_step,
                                      decay_steps=decay_step,
                                      decay_rate=decay_rate,
                                      staircase=True,
                                      name="learning_rate_decay")
    return lrd


def create_Adam_op(loss, alpha, beta1, beta2, epsilon):
    '''creates the training operation for a neural network in tensorflow using
    the Adam optimization algorithm
    Args:
        loss is the loss of the network
        alpha is the learning rate
        beta1 is the weight used for the first moment
        beta2 is the weight used for the second moment
        epsilon is a small number to avoid division by zero
    Returns: the Adam optimization operation
    '''
    optimizer = tf.train.AdamOptimizer(learning_rate=alpha, beta1=beta1,
                                       beta2=beta2, epsilon=epsilon)
    return optimizer.minimize(loss)


def model(Data_train, Data_valid, layers, activations, alpha=0.001, beta1=0.9,
          beta2=0.999, epsilon=1e-8, decay_rate=1, batch_size=32, epochs=5,
          save_path='/tmp/model.ckpt'):
    '''builds, trains, and saves a neural network model in tensorflow using
    Adam optimization, mini-batch gradient descent, learning rate decay,
    and batch normalization
    Args:
        Data_train is a tuple containing the training inputs and training
                   labels, respectively
        Data_valid is a tuple containing the validation inputs and validation
                   labels, respectively
        layers is a list containing the number of nodes in each layer of the
               network
        activations is a list containing the activation functions used for each
                   layer of the network
        alpha is the learning rate
        beta1 is the weight for the first moment of Adam Optimization
        beta2 is the weight for the second moment of Adam Optimization
        epsilon is a small number used to avoid division by zero
        decay_rate is the decay rate for inverse time decay of the learning
                   rate (the corresponding decay step should be 1)
        batch_size is the number of data points that should be in a mini-batch
        epochs is the number of times the training should pass through the
               whole dataset
        save_path is the path where the model should be saved to
    Returns: the path where the model was saved
    '''
    X_train = Data_train[0]
    Y_train = Data_train[1]
    X_valid = Data_valid[0]
    Y_valid = Data_valid[1]

    x, y = create_placeholders(X_train.shape[1], Y_train.shape[1])
    y_pred = forward_prop(x, layers, activations)
    loss = calculate_loss(y, y_pred)
    accuracy = calculate_accuracy(y, y_pred)

    tf.add_to_collection('x', x)
    tf.add_to_collection('y', y)
    tf.add_to_collection('y_pred', y_pred)
    tf.add_to_collection('loss', loss)
    tf.add_to_collection('accuracy', accuracy)

    with tf.Session() as sess:
        global_step = tf.Variable(0, trainable=False)
        alpha_d = learning_rate_decay(alpha, decay_rate, global_step,
                                      decay_step=1)
        train_op = create_Adam_op(loss, alpha_d, beta1, beta2, epsilon)
        init = tf.global_variables_initializer()
        sess.run(init)

        for epoch in range(epochs + 1):
            cost_t = sess.run(loss, feed_dict={x: X_train, y: Y_train})
            accu_t = sess.run(accuracy, feed_dict={x: X_train, y: Y_train})
            cost_val = sess.run(loss, feed_dict={x: X_valid, y: Y_valid})
            accu_val = sess.run(accuracy, feed_dict={x: X_valid, y: Y_valid})
            print("After {} epochs:".format(epoch))
            print("\tTraining Cost: {}".format(cost_t))
            print("\tTraining Accuracy: {}".format(accu_t))
            print("\tValidation Cost: {}".format(cost_val))
            print("\tValidation Accuracy: {}".format(accu_val))

            if epoch < epochs:

                sess.run(tf.assign(global_step, epoch))
                X_train_s, Y_train_s = shuffle_data(X_train, Y_train)

                # MINI BATCH training:
                m = X_train.shape[0]
                sess.run(alpha_d)
                for start in range(0, m, batch_size):
                    if (start + batch_size) < m:
                        X_train_m = X_train_s[start: start + batch_size]
                        Y_train_m = Y_train_s[start: start + batch_size]
                    else:
                        X_train_m = X_train_s[start: m]
                        Y_train_m = Y_train_s[start: m]

                    sess.run(train_op, {x: X_train_m, y: Y_train_m})

                    if start != 0 and (start / batch_size + 1) % 100 == 0:
                        cost_mini = sess.run(loss,
                                             feed_dict={x: X_train_m,
                                                        y: Y_train_m})
                        accu_mini = sess.run(accuracy,
                                             feed_dict={x: X_train_m,
                                                        y: Y_train_m})
                        print("\tStep {}:".format(int(start / batch_size + 1)))
                        print("\t\tCost: {}".format(cost_mini))
                        print("\t\tAccuracy: {}".format(accu_mini))

        return saver.save(sess, save_path)
