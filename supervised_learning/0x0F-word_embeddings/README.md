# 0x0F. Natural Language Processing - Word Embeddings

## Resources :books:
Read or watch:
* [An Introduction to Word Embeddings](https://intranet.hbtn.io/rltoken/VwPShE6ysZELC-fCFhJ7kw)
* [Introduction to Word Embeddings](http://hunterheidenreich.com/blog/intro-to-word-embeddings/)
* [Natural Language Processing|Bag Of Words Intuition](https://www.youtube.com/watch?v=IKgBLTeQQL8&list=PLZoTAELRMXVMdJ5sqbCK2LiM0HhQVWNzm&index=5)
* [Natural Language Processing|TF-IDF Intuition| Text Prerocessing](https://www.youtube.com/watch?v=D2V1okCEsiE&list=PLZoTAELRMXVMdJ5sqbCK2LiM0HhQVWNzm&index=7)
* [Word Embedding - Natural Language Processing| Deep Learning](https://www.youtube.com/watch?v=pO_6Jk0QtKw&fbclid=IwAR3GeSWJUZKbvUJXXyy6rZTXsTkakS8znbhQ2uZsyakpBFWrk2ovBMG7c8Q)
* [Word2Vec Tutorial - The Skip-Gram Model](http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/)
* [Word2Vec Tutorial Part 2 - Negative Sampling](http://mccormickml.com/2017/01/11/word2vec-tutorial-part-2-negative-sampling/)
* [GloVe Explained](https://intranet.hbtn.io/rltoken/myPyzhsVpaxc3hftSRyuuw)
* [FastText: Under the Hood](https://intranet.hbtn.io/rltoken/8JTc7eoPMjKtaNosRvvYYw)
* [ELMo Explained](https://www.mihaileric.com/posts/deep-contextualized-word-representations-elmo/)

---
## Learning Objectives :bulb:
What you should learn from this project:

* What is natural language processing?
* What is a word embedding?
* What is bag of words?
* What is TF-IDF?
* What is CBOW?
* What is a skip-gram?
* What is an n-gram?
* What is negative sampling?
* What is word2vec, GloVe, fastText, ELMo?

---

## Links to Files :file_folder:

### [0. Bag Of Words](./0-bag_of_words.py)
* Write a function def bag_of_words(sentences, vocab=None): that creates a bag of words embedding matrix:


### [1. TF-IDF](./1-tf_idf.py)
* Write a function def tf_idf(sentences, vocab=None): that creates a TF-IDF embedding:


### [2. Train Word2Vec](./2-word2vec.py)
* Write a function def word2vec_model(sentences, size=100, min_count=5, window=5, negative=5, cbow=True, iterations=5, seed=0, workers=1): that creates and trains a gensim word2vec model:


### [3. Extract Word2Vec](./3-gensim_to_keras.py)
* Write a function def gensim_to_keras(model): that converts a gensim word2vec model to a keras Embedding layer:


### [4. FastText](./4-fasttext.py)
* Write a function def fasttext_model(sentences, size=100, min_count=5, negative=5, window=5, cbow=True, iterations=5, seed=0, workers=1): that creates and trains a genism fastText model:


### [5. ELMo](./5-elmo)
* When training an ELMo embedding model, you are training:

---

## Author
* **Gabriel Cifuentes** - [gcifuentess](https://github.com/gcifuentess)


---
---

# *HBTN PROJECT:*


![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/7/a2fa719214e8c81107842b9fcd97defd08ba3d82.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20211007%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20211007T190021Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=fe37bdb2232169c1e7a07c446f0bf75da3a633c418c6a7d3a592109d1c193bca)


Resources
---------


**Read or watch:**


* [An Introduction to Word Embeddings](https://intranet.hbtn.io/rltoken/VwPShE6ysZELC-fCFhJ7kw "An Introduction to Word Embeddings")
* [Introduction to Word Embeddings](https://intranet.hbtn.io/rltoken/XcXiOu4G1cQmPsMCSV6iKg "Introduction to Word Embeddings")
* [Natural Language Processing|Bag Of Words Intuition](https://intranet.hbtn.io/rltoken/MFWRUck_pP6wWTo-Hk-uNA "Natural Language Processing|Bag Of Words Intuition")
* [Natural Language Processing|TF-IDF Intuition| Text Prerocessing](https://intranet.hbtn.io/rltoken/wNtfvYw0_t9__T34QullnQ "Natural Language Processing|TF-IDF Intuition| Text Prerocessing")
* [Word Embedding - Natural Language Processing| Deep Learning](https://intranet.hbtn.io/rltoken/EDAtqjDC2WJsCmc9DJHBsA "Word Embedding - Natural Language Processing| Deep Learning")
* [Word2Vec Tutorial - The Skip-Gram Model](https://intranet.hbtn.io/rltoken/e2onm8dzf3tnjAzhbqmY7w "Word2Vec Tutorial - The Skip-Gram Model")
* [Word2Vec Tutorial Part 2 - Negative Sampling](https://intranet.hbtn.io/rltoken/Oor3scClDEHAjTzs2UcLDg "Word2Vec Tutorial Part 2 - Negative Sampling")
* [GloVe Explained](https://intranet.hbtn.io/rltoken/myPyzhsVpaxc3hftSRyuuw "GloVe Explained")
* [FastText: Under the Hood](https://intranet.hbtn.io/rltoken/8JTc7eoPMjKtaNosRvvYYw "FastText: Under the Hood")
* [ELMo Explained](https://intranet.hbtn.io/rltoken/dg0fuahVOnnmQsBzkUGtKw "ELMo Explained")


**Definitions to skim**


* [Natural Language Processing](https://intranet.hbtn.io/rltoken/NLdhMq0eP7RCBdgTC2xXng "Natural Language Processing")


**References:**


* [Efficient Estimation of Word Representations in Vector Space (Skip-gram, 2013)](https://intranet.hbtn.io/rltoken/o6Kw0bZixZlCgSp8kv_d_A "Efficient Estimation of Word Representations in Vector Space (Skip-gram, 2013)")
* [Distributed Representations of Words and Phrases and their Compositionality (Word2Vec, 2013)](https://intranet.hbtn.io/rltoken/ibPaFuTAg_iFEUnXw6fi9g "Distributed Representations of Words and Phrases and their Compositionality (Word2Vec, 2013)")
* [GloVe: Global Vectors for Word Representation (website)](https://intranet.hbtn.io/rltoken/r_s4n4jWmHnUKnzd35_ayA "GloVe: Global Vectors for Word Representation (website)")
* [GloVe: Global Vectors for Word Representation (2014)](https://intranet.hbtn.io/rltoken/m3mB2j5a1DLVtZs2yvjn9A "GloVe: Global Vectors for Word Representation (2014)")
* [fastText (website)](https://intranet.hbtn.io/rltoken/XMu3K4vgAU3gXwdWbMYA7w "fastText (website)")
* [Bag of Tricks for Efficient Text Classification (fastText, 2016)](https://intranet.hbtn.io/rltoken/gK1mwr5kB-fJL3aFab1lHQ "Bag of Tricks for Efficient Text Classification (fastText, 2016)")
* [Enriching Word Vectors with Subword Information (fastText, 2017)](https://intranet.hbtn.io/rltoken/QgTup8akJ4AXifvCTrNcYw "Enriching Word Vectors with Subword Information (fastText, 2017)")
* [Probabilistic FastText for Multi-Sense Word Embeddings (2018)](https://intranet.hbtn.io/rltoken/0mqEv_KsCH8LRGIa1YpaiQ "Probabilistic FastText for Multi-Sense Word Embeddings (2018)")
* [ELMo (website)](https://intranet.hbtn.io/rltoken/jAs-99Y2LO5u0ciCKLKOxw "ELMo (website)")
* [Deep contextualized word representations (ELMo, 2018)](https://intranet.hbtn.io/rltoken/Waz8-ebrM2X8VNlmuVK3EQ "Deep contextualized word representations (ELMo, 2018)")
* [sklearn.feature\_extraction.text.CountVectorizer](https://intranet.hbtn.io/rltoken/KWBPHJxFppnvEBAdAqyoOQ "sklearn.feature_extraction.text.CountVectorizer")
* [sklearn.feature\_extraction.text.TfidfVectorizer](https://intranet.hbtn.io/rltoken/L1tR8a5IxijX0iPSF9Zgdg "sklearn.feature_extraction.text.TfidfVectorizer")
* [genism.models.word2vec](https://intranet.hbtn.io/rltoken/-x-mXaagTBNvEUDbd1D84Q "genism.models.word2vec")
* [genism.models.fasttext](https://intranet.hbtn.io/rltoken/KvUoA9pXEKUOBaXb8Azd2g "genism.models.fasttext")


Learning Objectives
-------------------


At the end of this project, you are expected to be able to [explain to anyone](https://intranet.hbtn.io/rltoken/fRFysyMWOzXdRtrqWlWr6w "explain to anyone"), **without the help of Google**:


### General


* What is natural language processing?
* What is a word embedding?
* What is bag of words?
* What is TF-IDF?
* What is CBOW?
* What is a skip-gram?
* What is an n-gram?
* What is negative sampling?
* What is word2vec, GloVe, fastText, ELMo?


Requirements
------------


### General


* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 16.04 LTS using `python3` (version 3.5)
* Your files will be executed with `numpy` (version 1.15) and `tensorflow` (version 1.12)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/env python3`
* All of your files must be executable
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should follow the `pycodestyle` style (version 2.4)
* All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)


Download Gensim 3.8.x
---------------------



```
pip install --user gensim==3.8

```

Download Keras 2.2.5
--------------------



```
pip install --user keras==2.2.5

```

 Quiz questions
---------------




#### Question #0



Word2Vec uses:



* Character n-grams
* Skip-grams -> asw
* CBOW -> asw
* Co-occurrence matrices
* Negative sampling -> asw







#### Question #1



GloVe uses:



* Character n-grams
* Skip-grams
* CBOW
* Co-occurrence matrices -> asw
* Negative sampling







#### Question #2



FastText uses:



* Character n-grams -> asw
* Skip-grams -> asw
* CBOW -> asw
* Co-occurrence matrices
* Negative sampling -> asw







#### Question #3



ELMo uses:



* Character n-grams -> asw
* Skip-grams
* CBOW
* Co-occurrence matrices
* Negative sampling







#### Question #4



Which of the following can be used in conjunction with the others?



* Word2Vec
* GloVe
* FastText
* ELMo -> asw





* Character n-grams
* Skip-grams
* CBOW
* Co-occurrence matrices
* Negative sampling

Tasks
-----

###  0. Bag Of Words

Write a function `def bag_of_words(sentences, vocab=None):` that creates a bag of words embedding matrix:

* `sentences` is a list of sentences to analyze
* `vocab` is a list of the vocabulary words to use for the analysis
	+ If `None`, all words within `sentences` should be used
* Returns: `embeddings, features`
	+ `embeddings` is a `numpy.ndarray` of shape `(s, f)` containing the embeddings
		- `s` is the number of sentences in `sentences`
		- `f` is the number of features analyzed
	+ `features` is a list of the features used for `embeddings`


```
$ cat 0-main.py
#!/usr/bin/env python3

bag_of_words = __import__('0-bag_of_words').bag_of_words

sentences = ["Holberton school is Awesome!",
             "Machine learning is awesome",
             "NLP is the future!",
             "The children are our future",
             "Our children's children are our grandchildren",
             "The cake was not very good",
             "No one said that the cake was not very good",
             "Life is beautiful"]
E, F = bag_of_words(sentences)
print(E)
print(F)
$ ./0-main.py
[[0 1 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0]
 [0 1 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 1 0 0]
 [1 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0]
 [1 0 0 0 2 0 0 1 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0]
 [0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 1 1]
 [0 0 0 1 0 0 1 0 0 0 0 0 0 0 1 1 1 0 1 0 1 1 1 1]
 [0 0 1 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0]]
['are', 'awesome', 'beautiful', 'cake', 'children', 'future', 'good', 'grandchildren', 'holberton', 'is', 'learning', 'life', 'machine', 'nlp', 'no', 'not', 'one', 'our', 'said', 'school', 'that', 'the', 'very', 'was']
$

```
###  1. TF-IDF

Write a function `def tf_idf(sentences, vocab=None):` that creates a TF-IDF embedding:

* `sentences` is a list of sentences to analyze
* `vocab` is a list of the vocabulary words to use for the analysis
	+ If `None`, all words within `sentences` should be used
* Returns: `embeddings, features`
	+ `embeddings` is a `numpy.ndarray` of shape `(s, f)` containing the embeddings
		- `s` is the number of sentences in `sentences`
		- `f` is the number of features analyzed
	+ `features` is a list of the features used for `embeddings`


```
$ cat 1-main.py
#!/usr/bin/env python3

tf_idf = __import__('1-tf_idf').tf_idf

sentences = ["Holberton school is Awesome!",
             "Machine learning is awesome",
             "NLP is the future!",
             "The children are our future",
             "Our children's children are our grandchildren",
             "The cake was not very good",
             "No one said that the cake was not very good",
             "Life is beautiful"]
vocab = ["awesome", "learning", "children", "cake", "good", "none", "machine"]
E, F = tf_idf(sentences, vocab)
print(E)
print(F)
$ ./1-main.py
[[1.         0.         0.         0.         0.         0.
  0.        ]
 [0.5098139  0.60831315 0.         0.         0.         0.
  0.60831315]
 [0.         0.         0.         0.         0.         0.
  0.        ]
 [0.         0.         1.         0.         0.         0.
  0.        ]
 [0.         0.         1.         0.         0.         0.
  0.        ]
 [0.         0.         0.         0.70710678 0.70710678 0.
  0.        ]
 [0.         0.         0.         0.70710678 0.70710678 0.
  0.        ]
 [0.         0.         0.         0.         0.         0.
  0.        ]]
['awesome', 'learning', 'children', 'cake', 'good', 'none', 'machine']
$

```
###  2. Train Word2Vec

Write a function `def word2vec_model(sentences, size=100, min_count=5, window=5, negative=5, cbow=True, iterations=5, seed=0, workers=1):` that creates and trains a `gensim` `word2vec` model:

* `sentences` is a list of sentences to be trained on
* `size` is the dimensionality of the embedding layer
* `min_count` is the minimum number of occurrences of a word for use in training
* `window` is the maximum distance between the current and predicted word within a sentence
* `negative` is the size of negative sampling
* `cbow` is a boolean to determine the training type; `True` is for CBOW; `False` is for Skip-gram
* `iterations` is the number of iterations to train over
* `seed` is the seed for the random number generator
* `workers` is the number of worker threads to train the model
* Returns: the trained model


```
$ cat 2-main.py
#!/usr/bin/env python3

from gensim.test.utils import common_texts
word2vec_model = __import__('2-word2vec').word2vec_model

print(common_texts[:2])
w2v = word2vec_model(common_texts, min_count=1)
print(w2v.wv["computer"])
$ ./2-main.py
[['human', 'interface', 'computer'], ['survey', 'user', 'computer', 'system', 'response', 'time']]
[-3.0043968e-03  1.5343886e-03  4.0832465e-03  3.7239199e-03
  4.9583608e-04  4.8461729e-03 -1.0620747e-03  8.2803884e-04
  9.7367732e-04 -6.7797926e-05 -1.5526683e-03  1.8058836e-03
 -4.3851901e-03  4.7258494e-04  2.8616134e-03 -2.2246949e-03
  2.7494587e-03 -3.5267104e-03  3.0259083e-03  2.7240592e-03
  2.6110576e-03 -4.5409841e-03  4.9135066e-03  8.2884904e-04
  2.7018311e-03  1.5654180e-03 -1.5859824e-03  9.3057036e-04
  3.7275942e-03 -3.6502020e-03  2.8285771e-03 -4.2384453e-03
  3.2712172e-03 -1.9101484e-03 -1.8624340e-03 -5.6956144e-04
 -1.5617535e-03 -2.3851227e-03 -1.4313431e-05 -4.3398165e-03
  3.9115595e-03 -3.0616210e-03  1.7589398e-03 -3.4103722e-03
  4.7280011e-03  1.9380470e-03 -3.3873315e-03  8.4065803e-04
  2.6089977e-03  1.7012059e-03 -2.7421617e-03 -2.2240754e-03
 -5.3690566e-04  2.9577864e-03  2.3726511e-03  3.2704175e-03
  2.0853498e-03 -1.1927494e-03 -2.1565862e-03 -9.0970926e-04
 -2.8641665e-04 -3.4961947e-03  1.1104723e-03  1.2320089e-03
 -5.9017556e-04 -3.0594901e-03  3.6974431e-03 -1.8557351e-03
 -3.8218759e-03  9.2711346e-04 -4.3113795e-03 -4.4118706e-03
  4.7748778e-03 -4.5557776e-03 -2.2665847e-03 -8.2379003e-04
 -7.9581753e-04 -1.3048936e-03  1.9261248e-03  3.1299898e-03
 -1.9034051e-03 -2.0335305e-03 -2.6451424e-03  1.7377195e-03
  6.7217485e-04 -2.4134698e-03  4.3735080e-03 -3.2599240e-03
 -2.2431149e-03  4.4288361e-03  1.4923669e-04 -2.2144278e-03
 -8.9370424e-04 -2.7281314e-04 -1.7176758e-03  1.2485087e-03
  1.3230384e-03  1.7001784e-04  3.5425189e-03 -1.7469387e-04]
$

```
###  3. Extract Word2Vec

Write a function `def gensim_to_keras(model):` that converts a `gensim` `word2vec` model to a `keras` Embedding layer:

* `model` is a trained `gensim` `word2vec` models
* Returns: the trainable `keras` Embedding


```
$ cat 3-main.py
#!/usr/bin/env python3

from gensim.test.utils import common_texts
word2vec_model = __import__('2-word2vec').word2vec_model
gensim_to_keras = __import__('3-gensim_to_keras').gensim_to_keras

print(common_texts[:2])
w2v = word2vec_model(common_texts, min_count=1)
print(gensim_to_keras(w2v))
$ ./3-main.py
[['human', 'interface', 'computer'], ['survey', 'user', 'computer', 'system', 'response', 'time']]
Using TensorFlow backend.
<keras.layers.embeddings.Embedding object at 0x7f72e2c1bd30>
$

```
###  4. FastText

Write a function `def fasttext_model(sentences, size=100, min_count=5, negative=5, window=5, cbow=True, iterations=5, seed=0, workers=1):` that creates and trains a `genism` `fastText` model:

* `sentences` is a list of sentences to be trained on
* `size` is the dimensionality of the embedding layer
* `min_count` is the minimum number of occurrences of a word for use in training
* `window` is the maximum distance between the current and predicted word within a sentence
* `negative` is the size of negative sampling
* `cbow` is a boolean to determine the training type; `True` is for CBOW; `False` is for Skip-gram
* `iterations` is the number of iterations to train over
* `seed` is the seed for the random number generator
* `workers` is the number of worker threads to train the model
* Returns: the trained model


```
$ cat 4-main.py
#!/usr/bin/env python3

from gensim.test.utils import common_texts
fasttext_model = __import__('4-fasttext').fasttext_model

print(common_texts[:2])
ft = fasttext_model(common_texts, min_count=1)
print(ft.wv["computer"])
$ ./4-main.py
[['human', 'interface', 'computer'], ['survey', 'user', 'computer', 'system', 'response', 'time']]
[-2.3464665e-03 -1.4542247e-04 -3.9549544e-05 -1.5817649e-03
 -2.1579072e-03  4.5148263e-04  9.9494774e-04  3.2517681e-05
  1.7035202e-04  6.8571279e-04 -2.0803163e-04  5.3083687e-04
  1.2990861e-03  3.5418154e-04  2.1087916e-03  1.1022155e-03
  6.2364555e-04  1.8612258e-05  1.8982493e-05  1.3051173e-03
 -6.0260214e-04  1.6334689e-03 -1.0172457e-06  1.4247939e-04
  1.1081318e-04  1.8327738e-03 -3.3656979e-04 -3.7365756e-04
  8.0635358e-04 -1.2945861e-04 -1.1031038e-04  3.4695750e-04
 -2.1932719e-04  1.4800908e-03  7.7851227e-04  8.6328381e-04
 -9.7545242e-04  6.0775197e-05  7.1560958e-04  3.6474539e-04
  3.3428212e-05 -1.0499550e-03 -1.2412234e-03 -1.8492664e-04
 -4.8664736e-04  1.9178988e-04 -6.3863385e-04  3.3325219e-04
 -1.5724128e-03  1.0003068e-03  1.7905374e-04  7.8452297e-04
  1.2625050e-04  8.1183662e-04 -4.9907330e-04  1.0475471e-04
  1.4351985e-03  4.9145994e-05 -1.4620423e-03  3.1466845e-03
  2.0059240e-05  1.6659468e-03 -4.3319576e-04  1.3077060e-03
 -2.0228853e-03  5.7626975e-04 -1.4056480e-03 -4.2292831e-04
  6.4076332e-04 -8.5614284e-04  1.9028617e-04  6.0735084e-04
  2.6121829e-04 -1.0566596e-03  1.0602509e-03  1.2843860e-03
  7.9715136e-04  2.8305652e-04  1.9187009e-04 -1.0519206e-03
 -8.2213630e-04 -2.1762338e-04 -1.7580058e-04  1.2764390e-04
 -1.5695200e-03  1.3364316e-03 -1.5765150e-03  1.4802803e-03
  1.5476452e-03  2.1928034e-04 -9.3281898e-04  3.2964293e-04
 -1.0146293e-03 -1.3567278e-03  1.8070930e-03 -4.2649341e-04
 -1.9074128e-03  7.1639987e-04 -1.3686880e-03  3.7073060e-03]
$

```
###  5. ELMo

When training an ELMo embedding model, you are training:

* A. 1, 2, 3
* B. 1, 2
* C. 2, 3
* D. 1, 3
* E. 1
* F. 2
* G. 3
* H. None of the above
---
