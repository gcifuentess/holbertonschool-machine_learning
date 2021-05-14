#!/usr/bin/env python3
'''tensorflow trainin a neural network module'''
import tensorflow as tf
calculate_accuracy = __import__('3-calculate_accuracy').calculate_accuracy
calculate_loss = __import__('4-calculate_loss').calculate_loss
create_placeholders = __import__('0-create_placeholders').create_placeholders
create_train_op = __import__('5-create_train_op').create_train_op
forward_prop = __import__('2-forward_prop').forward_prop


def train(X_train, Y_train, X_valid, Y_valid, layer_sizes, activations,
          alpha, iterations, save_path="/tmp/model.ckpt"):
    '''builds, trains, and saves a neural network classifier
    Args:
        X_train: is a numpy.ndarray containing the training input data
        Y_train: is a numpy.ndarray containing the training labels
        X_valid: is a numpy.ndarray containing the validation input data
        Y_valid: is a numpy.ndarray containing the validation labels
        layer_sizes: is a list containing the number of nodes in each layer of
                     the network
        activations: is a list containing the activation functions for each
                     layer of the network
        alpha: is the learning rate
        iterations: is the number of iterations to train over
        save_path: designates where to save the model
    Return: the path where the model was saved
    '''

    x, y = create_placeholders(X_train.shape[1], Y_train.shape[1])
    y_pred = forward_prop(x, layer_sizes, activations)
    loss = calculate_loss(y, y_pred)
    accuracy = calculate_accuracy(y, y_pred)
    train_op = create_train_op(loss, alpha)

    tf.add_to_collection('x', x)
    tf.add_to_collection('y', y)
    tf.add_to_collection('y_pred', y_pred)
    tf.add_to_collection('loss', loss)
    tf.add_to_collection('accuracy', accuracy)
    tf.add_to_collection('train_op', train_op)

    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    with sess.as_default():
        for i in range(iterations + 1):
            cost_t = loss.eval(feed_dict={x: X_train, y: Y_train})
            accu_t = accuracy.eval(feed_dict={x: X_train, y: Y_train})
            cost_val = loss.eval(feed_dict={x: X_valid, y: Y_valid})
            accu_val = accuracy.eval(feed_dict={x: X_valid, y: Y_valid})
            if i == iterations or i % 100 == 0:
                print("After {} iterations:".format(i))
                print("\tTraining Cost: {}".format(cost_t))
                print("\tTraining Accuracy: {}".format(accu_t))
                print("\tValidation Cost: {}".format(cost_val))
                print("\tValidation Accuracy: {}".format(accu_val))
            if i < iterations:
                sess.run(train_op, {x: X_train, y: Y_train})
        to_save = tf.train.Saver()

        return to_save.save(sess, save_path)
