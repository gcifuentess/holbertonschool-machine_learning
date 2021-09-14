#!/usr/bin/env python3
'''TF-IDF module'''
from sklearn.feature_extraction.text import TfidfVectorizer


def tf_idf(sentences, vocab=None):
    '''creates a TF-IDF embedding
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
    TfidfV_instance = TfidfVectorizer(vocabulary=vocab)
    embeddings = TfidfV_instance.fit_transform(sentences)
    features = TfidfV_instance.get_feature_names()

    return embeddings.toarray(), features
