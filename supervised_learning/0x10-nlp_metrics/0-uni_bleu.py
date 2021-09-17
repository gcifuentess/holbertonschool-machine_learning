#!/usr/bin/env python3
'''Unigram BLEU score'''
import numpy as np


def uni_bleu(references, sentence):
    '''calculates the unigram BLEU score for a sentence
    Args:
        references is a list of reference translations
            - each reference translation is a list of the words in the
              translation
        sentence is a list containing the model proposed sentence

    Returns: the unigram BLEU score
    '''
    count = {}
    count_clip = {}
    len_refs = []

    for word in set(sentence):
        count[word] = sentence.count(word)

    for reference in references:
        len_refs.append(len(reference))

        for word in set(reference):
            if word in sentence:
                if word in count_clip.keys():
                    count_clip[word] = max(count_clip[word],
                                           reference.count(word))
                else:
                    count_clip[word] = reference.count(word)

    for word in count.keys():
        if word in count_clip.keys():
            count_clip[word] = min(count[word], count_clip[word])

    Pn = sum(count_clip.values()) / sum(count.values())

    len_refs.sort()
    c = len(sentence)
    r = len_refs[0]
    if (c > r):
        bp = 1  # brevity penalty
    else:
        bp = np.exp(1 - r / c)

    return bp * np.exp(np.log(Pn))  # BLUE score
