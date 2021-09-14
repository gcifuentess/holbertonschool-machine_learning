#!/usr/bin/env python3
'''Extract Word2Vec module'''
import numpy as np
from keras.layers import Embedding


def gensim_to_keras(model):
    '''converts a gensim word2vec model to a keras Embedding layer
    Args:
        model is a trained gensim word2vec models

    Returns: the trainable keras Embedding
    '''
    vocab = model.wv.vocab
    embedding_matrix = np.zeros((len(vocab), model.vector_size))

    for i in range(len(vocab)):
        embedding_vector = model.wv[model.wv.index2word[i]]
        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector

    return Embedding(
        input_dim=embedding_matrix.shape[0],
        output_dim=embedding_matrix.shape[1],
        weights=[embedding_matrix],
    )
