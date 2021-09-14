#!/usr/bin/env python3
'''Bag Of Words module'''
import numpy as np


def bag_of_words(sentences, vocab=None):
    '''creates a bag of words embedding matrix
    Args:
        sentences is a list of sentences to analyze
        vocab is a list of the vocabulary words to use for the analysis
              - If None, all words within sentences should be used

    Returns: embeddings, features
        embeddings is a numpy.ndarray of shape (s, f) containing the embeddings
            - s is the number of sentences in sentences
            - f is the number of features analyzed
        features is a list of the features used for embeddings
    '''
    loops = 1
    if vocab is None:
        loops = 2

    s_vocab = []  # vocabulary from sentences
    features = []

    # first loop to build the vocabulary if None
    # second loop to build the embeddings
    for i in range(loops):

        if vocab is not None:
            embeddings = np.zeros((len(sentences), len(vocab)), dtype=np.int32)

        for j, sentence in enumerate(sentences):
            sentence = sentence.lower()
            words = sentence.split(' ')

            for word in words:
                p_word = ''  # processed word

                for l in word:
                    if l.isalpha():  # check for special chars
                        p_word += l
                    else:
                        break

                if vocab is None and p_word not in s_vocab:
                    s_vocab.append(p_word)

                if vocab is not None:
                    idx = vocab.index(p_word)
                    embeddings[j][idx] += 1
                    if i == 0:
                        feature = vocab[idx]
                        if feature not in features:
                            features.append(feature)

        if vocab is None:
            s_vocab.sort()
            vocab = s_vocab.copy()
            features = s_vocab

    return embeddings, features
