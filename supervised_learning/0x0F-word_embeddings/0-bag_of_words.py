#!/usr/bin/env python3
'''Bag Of Words module'''
from sklearn.feature_extraction.text import CountVectorizer


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
    CV_instance = CountVectorizer(vocabulary=vocab)
    embeddings = CV_instance.fit_transform(sentences)
    features = CV_instance.get_feature_names()

    return embeddings.toarray(), features
