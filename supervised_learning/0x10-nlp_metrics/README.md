# 0x10. Natural Language Processing - Evaluation Metrics

## Resources :books:
Read or watch:
* [7 Applications of Deep Learning for Natural Language Processing](https://machinelearningmastery.com/applications-of-deep-learning-for-natural-language-processing/)
* [10 Applications of Artificial Neural Networks in Natural Language Processing](https://medium.com/@datamonsters/artificial-neural-networks-in-natural-language-processing-bcf62aa9151a)
* [A Gentle Introduction to Calculating the BLEU Score for Text in Python](https://machinelearningmastery.com/calculate-bleu-score-for-text-python/)
* [Bleu Score](https://www.youtube.com/watch?v=DejHQYAGb7Q)
* [Evaluating Text Output in NLP: BLEU at your own risk](https://towardsdatascience.com/evaluating-text-output-in-nlp-bleu-at-your-own-risk-e8609665a213)
* [ROUGE metric](https://towardsdatascience.com/the-ultimate-performance-metric-in-nlp-111df6c64460)
* [Evaluation and Perplexity](https://www.youtube.com/watch?v=BAN3NB_SNHY)

---
## Learning Objectives :bulb:
What you should learn from this project:

* What are the applications of natural language processing?
* What is a BLEU score?
* What is a ROUGE score?
* What is perplexity?
* When should you use one evaluation metric over another?

---

## Links to Files :file_folder:

### [0. Unigram BLEU score](./0-uni_bleu.py)
* Write the function def uni_bleu(references, sentence): that calculates the unigram BLEU score for a sentence:


### [1. N-gram BLEU score](./1-ngram_bleu.py)
* Write the function def ngram_bleu(references, sentence, n): that calculates the n-gram BLEU score for a sentence:


### [2. Cumulative N-gram BLEU score](./2-cumulative_bleu.py)
* Write the function def cumulative_bleu(references, sentence, n): that calculates the cumulative n-gram BLEU score for a sentence:

---

## Author
* **Gabriel Cifuentes** - [gcifuentess](https://github.com/gcifuentess)


---
---

# *HBTN PROJECT:*


Resources
---------


**Read or watch:**


* [7 Applications of Deep Learning for Natural Language Processing](https://intranet.hbtn.io/rltoken/EFeppnrszrEGza6nrymxgQ "7 Applications of Deep Learning for Natural Language Processing")
* [10 Applications of Artificial Neural Networks in Natural Language Processing](https://intranet.hbtn.io/rltoken/Pcs54fB9zpZZWlMH_OamfQ "10 Applications of Artificial Neural Networks in Natural Language Processing")
* [A Gentle Introduction to Calculating the BLEU Score for Text in Python](https://intranet.hbtn.io/rltoken/lC85P6iX492bGuBncUNwiw "A Gentle Introduction to Calculating the BLEU Score for Text in Python")
* [Bleu Score](https://intranet.hbtn.io/rltoken/lT-MBM6w7AjXPIiZoPKR_A "Bleu Score")
* [Evaluating Text Output in NLP: BLEU at your own risk](https://intranet.hbtn.io/rltoken/cjfXGBHKEfS9ObZKL99n0A "Evaluating Text Output in NLP: BLEU at your own risk")
* [ROUGE metric](https://intranet.hbtn.io/rltoken/b9LUGN2qt8KSh6rkCqB6rA "ROUGE metric")
* [Evaluation and Perplexity](https://intranet.hbtn.io/rltoken/Mgyoxa8c6WvpFJaHFxqlQQ "Evaluation and Perplexity")


**Definitions to skim**


* [BLEU](https://intranet.hbtn.io/rltoken/njmmpbMuP0cPnnWwbFpj3A "BLEU")
* [ROUGE](https://intranet.hbtn.io/rltoken/BJK2tEo1kVYXytMDoVF9fQ "ROUGE")
* [Perplexity](https://intranet.hbtn.io/rltoken/MayHONfLeczBB8qWvaDrkQ "Perplexity")


**References:**


* [BLEU: a Method for Automatic Evaluation of Machine Translation (2002)](https://intranet.hbtn.io/rltoken/EsAnXupX-J-y6YwoH6VUTw "BLEU: a Method for Automatic Evaluation of Machine Translation (2002)")
* [ROUGE: A Package for Automatic Evaluation of Summaries (2004)](https://intranet.hbtn.io/rltoken/A8PhjII-AIn5JCQzhXNQ2A "ROUGE: A Package for Automatic Evaluation of Summaries (2004)")


Learning Objectives
-------------------


At the end of this project, you are expected to be able to [explain to anyone](https://intranet.hbtn.io/rltoken/JaxyzfdRMwW4bxSoNku7aA "explain to anyone"), **without the help of Google**:


### General


* What are the applications of natural language processing?
* What is a BLEU score?
* What is a ROUGE score?
* What is perplexity?
* When should you use one evaluation metric over another?


Requirements
------------


### General


* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 16.04 LTS using `python3` (version 3.5)
* Your files will be executed with `numpy` (version 1.15)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/env python3`
* All of your files must be executable
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should follow the `pycodestyle` style (version 2.4)
* All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* You are not allowed to use the `nltk` module


 Quiz questions
---------------




#### Question #0



The BLEU score measures:



* A model’s accuracy
* A model’s precision -> asw
* A model’s recall
* A model’s perplexity







#### Question #1



The ROUGE score measures:



* A model’s accuracy
* A model’s precision -> asw
* A model’s recall -> asw
* A model’s perplexity







#### Question #2



Perplexity measures:



* The accuracy of a prediction
* The branching factor of a prediction -> asw
* A prediction’s recall
* A prediction’s accuracy







#### Question #3



The BLEU score was designed for:



* Sentiment Analysis
* Machine Translation -> asw
* Question-Answering
* Document Summarization







#### Question #4



What are the shortcomings of the BLEU score?



* It cannot judge grammatical accuracy -> asw
* It cannot judge meaning -> asw
* It does not work with languages that lack word boundaries -> asw
* A higher score is not necessarily indicative of a better translation -> asw





* A model’s accuracy
* A model’s precision
* A model’s recall
* A model’s perplexity

Tasks
-----

###  0. Unigram BLEU score

Write the function `def uni_bleu(references, sentence):` that calculates the unigram BLEU score for a sentence:

* `references` is a list of reference translations
	+ each reference translation is a list of the words in the translation
* `sentence` is a list containing the model proposed sentence
* Returns: the unigram BLEU score


```
$ cat 0-main.py
#!/usr/bin/env python3

uni_bleu = __import__('0-uni_bleu').uni_bleu

references = [["the", "cat", "is", "on", "the", "mat"], ["there", "is", "a", "cat", "on", "the", "mat"]]
sentence = ["there", "is", "a", "cat", "here"]

print(uni_bleu(references, sentence))
$ ./0-main.py
0.6549846024623855
$

```
###  1. N-gram BLEU score

Write the function `def ngram_bleu(references, sentence, n):` that calculates the n-gram BLEU score for a sentence:

* `references` is a list of reference translations
	+ each reference translation is a list of the words in the translation
* `sentence` is a list containing the model proposed sentence
* `n` is the size of the n-gram to use for evaluation
* Returns: the n-gram BLEU score


```
$ cat 1-main.py
#!/usr/bin/env python3

ngram_bleu = __import__('1-ngram_bleu').ngram_bleu

references = [["the", "cat", "is", "on", "the", "mat"], ["there", "is", "a", "cat", "on", "the", "mat"]]
sentence = ["there", "is", "a", "cat", "here"]

print(ngram_bleu(references, sentence, 2))
$ ./1-main.py
0.6140480648084865
$

```
###  2. Cumulative N-gram BLEU score

Write the function `def cumulative_bleu(references, sentence, n):` that calculates the cumulative n-gram BLEU score for a sentence:

* `references` is a list of reference translations
	+ each reference translation is a list of the words in the translation
* `sentence` is a list containing the model proposed sentence
* `n` is the size of the largest n-gram to use for evaluation
* All n-gram scores should be weighted evenly
* Returns: the cumulative n-gram BLEU score


```
$ cat 2-main.py
#!/usr/bin/env python3

cumulative_bleu = __import__('1-cumulative_bleu').cumulative_bleu

references = [["the", "cat", "is", "on", "the", "mat"], ["there", "is", "a", "cat", "on", "the", "mat"]]
sentence = ["there", "is", "a", "cat", "here"]

print(cumulative_bleu(references, sentence, 4))
$ ./2-main.py
0.5475182535069453
$

```
---
