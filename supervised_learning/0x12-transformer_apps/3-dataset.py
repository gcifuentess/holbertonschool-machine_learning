#!/usr/bin/env python3
'''Dataset module'''
import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds


class Dataset():
    ''' loads and preps a dataset for machine translation'''

    def __init__(self, batch_size, max_len):
        '''Dataset class constructor
        Args:
            batch_size is the batch size for training/validation
            max_len is the maximum number of tokens allowed per example
                    sentence

        creates the instance attributes:
               data_train, which contains the ted_hrlr_translate/pt_to_en
                           tf.data.Dataset train split, loaded as_supervised
               data_valid, which contains the ted_hrlr_translate/pt_to_en
                           tf.data.Dataset validate split, loaded as_supervised
               tokenizer_pt is the Portuguese tokenizer created from the
                            training set
               tokenizer_en is the English tokenizer created from the training
                            set
        '''
        self.data_train = tfds.load(
            name='ted_hrlr_translate/pt_to_en',
            split='train',
            as_supervised=True,
        )
        self.data_valid = tfds.load(
            name='ted_hrlr_translate/pt_to_en',
            split='validation',
            as_supervised=True,
        )
        self.tokenizer_pt, self.tokenizer_en = self.tokenize_dataset(
            self.data_train
        )

        # --- PIPELINE ---
        def filter_max_len(pt, en, max_len=max_len):
            '''checks if the len of pt and en are <= than max_len
            Args:
                pt is the tf.Tensor containing the Portuguese sentence
                en is the tf.Tensor containing the corresponding English
                   sentence
                max_len is the maximum number of tokens allowed per example
                        sentence

            Returns: A Tensor of type bool.
            '''
            return tf.logical_and(tf.size(pt) <= max_len,
                                  tf.size(en) <= max_len)

        full_size = len(self.data_train)
        self.data_train = (self.data_train.map(self.tf_encode)
                           .filter(filter_max_len)
                           .cache()
                           .shuffle(full_size)
                           .padded_batch(
                               batch_size,
                               padded_shapes=([None], [None]),
                               )
                           .prefetch(tf.data.experimental.AUTOTUNE)
                           )

        self.data_valid = (self.data_valid.map(self.tf_encode)
                           .filter(filter_max_len)
                           .padded_batch(
                               batch_size,
                               padded_shapes=([None], [None]),
                               )
                           )
        # ---

    def tokenize_dataset(self, data):
        '''creates sub-word tokenizers for our dataset
        Args:
            data is a tf.data.Dataset whose examples are formatted as a
                 tuple (pt, en)
                - pt is the tf.Tensor containing the Portuguese sentence
                - en is the tf.Tensor containing the corresponding English
                     sentence

        Important: The maximum vocab size will be set to 2**15

        Returns: tokenizer_pt, tokenizer_en
            - tokenizer_pt is the Portuguese tokenizer
            - tokenizer_en is the English tokenizer
        '''
        en_data = []
        pt_data = []
        for pt, en in data:
            en_data.append(en.numpy())
            pt_data.append(pt.numpy())

        SubwordTextEncoder = tfds.deprecated.text.SubwordTextEncoder

        tokenizer_pt = SubwordTextEncoder.build_from_corpus(
            corpus_generator=pt_data,
            target_vocab_size=2**15,
        )

        tokenizer_en = SubwordTextEncoder.build_from_corpus(
            corpus_generator=en_data,
            target_vocab_size=2**15,
        )

        return tokenizer_pt, tokenizer_en

    def encode(self, pt, en):
        '''encodes a translation into tokens
        Args:
            pt is the tf.Tensor containing the Portuguese sentence
            en is the tf.Tensor containing the corresponding English sentence

        Important:
            The tokenized sentences will include the start and end of
                sentence tokens
            The start token will be indexed as vocab_size
            The end token will be indexed as vocab_size + 1

        Returns: pt_tokens, en_tokens
            pt_tokens is a np.ndarray containing the Portuguese tokens
            en_tokens is a np.ndarray. containing the English tokens
        '''
        pt_tokens = [self.tokenizer_pt.vocab_size] + \
            self.tokenizer_pt.encode(pt.numpy()) + \
            [self.tokenizer_pt.vocab_size+1]

        en_tokens = [self.tokenizer_en.vocab_size] + \
            self.tokenizer_en.encode(en.numpy()) + \
            [self.tokenizer_en.vocab_size+1]

        return pt_tokens, en_tokens

    def tf_encode(self, pt, en):
        '''a tensorflow wrapper for the encode instance method
        Args:
            pt is a np.ndarray containing the Portuguese tokens
            en is a np.ndarray. containing the English tokens

        Returns: a tensorflow wrapper

        '''
        return tf.py_function(self.encode, [pt, en], [tf.int64, tf.int64])
