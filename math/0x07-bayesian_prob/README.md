# 0x07. Bayesian Probability

## Resources :books:
Read or watch:
* [Bayesian probability](https://en.wikipedia.org/wiki/Bayesian_probability)
* [Bayesian statistics](https://en.wikipedia.org/wiki/Bayesian_statistics)
* [Bayes’ Theorem - The Simplest Case](https://www.youtube.com/watch?v=XQoLVl31ZfQ)
* [A visual guide to Bayesian thinking](https://www.youtube.com/watch?v=BrK7X_XlGB8)
* [Base Rates](https://onlinestatbook.com/2/probability/base_rates.html)
* [Bayesian statistics: a comprehensive course](https://www.youtube.com/playlist?list=PLFDbGp5YzjqXQ4oE4w9GVWdiokWB9gEpm)
* [Bayes’ rule - an intuitive explanation](https://www.youtube.com/watch?v=EbyUsf_jUjk&list=PLFDbGp5YzjqXQ4oE4w9GVWdiokWB9gEpm&index=14)
* [Bayes’ rule in statistics](https://www.youtube.com/watch?v=i567qvWejJA&list=PLFDbGp5YzjqXQ4oE4w9GVWdiokWB9gEpm&index=15)
* [Bayes’ rule in inference - likelihood](https://www.youtube.com/watch?v=c69a_viMRQU&list=PLFDbGp5YzjqXQ4oE4w9GVWdiokWB9gEpm&index=16)
* [Bayes’ rule in inference - the prior and denominator](https://www.youtube.com/watch?v=a5QDDZLGSXY&list=PLFDbGp5YzjqXQ4oE4w9GVWdiokWB9gEpm&index=17)
* [Bayes’ rule denominator: discrete and continuous](https://www.youtube.com/watch?v=QEzeLh6L9Tg&list=PLFDbGp5YzjqXQ4oE4w9GVWdiokWB9gEpm&index=24)
* [Bayes’ rule: why likelihood is not a probability](https://www.youtube.com/watch?v=sm60vapz2jQ&list=PLFDbGp5YzjqXQ4oE4w9GVWdiokWB9gEpm&index=25)

---
## Learning Objectives :bulb:
What you should learn from this project:

* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 16.04 LTS using python3 (version 3.5)
* Your files will be executed with numpy (version 1.15)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/env python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle style (version 2.5)
* All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* Unless otherwise noted, you are not allowed to import any module except import numpy as np
* All your files must be executable
* The length of your files will be tested using wc

---

## Links to Files :file_folder:

### [0. Likelihood](./0-likelihood.py)
* You are conducting a study on a revolutionary cancer drug and are looking to find the probability that a patient who takes this drug will develop severe side effects. During your trials, n patients take the drug and x patients develop severe side effects. You can assume that x follows a binomial distribution.


### [1. Intersection](./1-intersection.py)
* Based on 0-likelihood.py, write a function def intersection(x, n, P, Pr): that calculates the intersection of obtaining this data with the various hypothetical probabilities:


### [2. Marginal Probability](./2-marginal.py)
* Based on 1-intersection.py, write a function def marginal(x, n, P, Pr): that calculates the marginal probability of obtaining the data:


### [3. Posterior](./3-posterior.py)
* Based on 2-marginal.py, write a function def posterior(x, n, P, Pr): that calculates the posterior probability for the various hypothetical probabilities of developing severe side effects given the data:


### [4. Continuous Posterior](./100-continuous.py)
* Based on 3-posterior.py, write a function def posterior(x, n, p1, p2): that calculates the posterior probability that the probability of developing severe side effects falls within a specific range given the data:

---

## Author
* **Gabriel Cifuentes** - [gcifuentess](https://github.com/gcifuentess)


---
---

# *HBTN PROJECT:*


![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/8/8358e1144bbb1fcc51b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20211006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20211006T231613Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=023108d2ed92fc2c10b2a3776a1ad1c933be87da59c0f4b1e4da08a4624da5f7)


Resources
---------


**Read or watch**:


* [Bayesian probability](https://intranet.hbtn.io/rltoken/sTaD6jnhKs_TTfQZzJ3yhQ "Bayesian probability")
* [Bayesian statistics](https://intranet.hbtn.io/rltoken/1v-8Ekg3h0raamUXPhY2QQ "Bayesian statistics")
* [Bayes’ Theorem - The Simplest Case](https://intranet.hbtn.io/rltoken/VqWGh8Z-0EAiTxGbxOR3gw "Bayes' Theorem - The Simplest Case")
* [A visual guide to Bayesian thinking](https://intranet.hbtn.io/rltoken/oO_89xTL9ijXyB6d6TJUPg "A visual guide to Bayesian thinking")
* [Base Rates](https://intranet.hbtn.io/rltoken/JheEb1W71ompqRatlXHIzw "Base Rates")
* [Bayesian statistics: a comprehensive course](https://intranet.hbtn.io/rltoken/Kmv4IuCD4b2C1et6zDPHGA "Bayesian statistics: a comprehensive course")
	+ [Bayes’ rule - an intuitive explanation](https://intranet.hbtn.io/rltoken/wVw3Sust10jQDa3-BDDzUA "Bayes' rule - an intuitive explanation")
	+ [Bayes’ rule in statistics](https://intranet.hbtn.io/rltoken/wUhrdfFq0be4VH4strzaXQ "Bayes' rule in statistics")
	+ [Bayes’ rule in inference - likelihood](https://intranet.hbtn.io/rltoken/EhC5nfFrqlMxRG6a8YC3dw "Bayes' rule in inference - likelihood")
	+ [Bayes’ rule in inference - the prior and denominator](https://intranet.hbtn.io/rltoken/76IgPqJyHwanrMbxPld4qg "Bayes' rule in inference - the prior and denominator")
	+ [Bayes’ rule denominator: discrete and continuous](https://intranet.hbtn.io/rltoken/vO953V4kzEr6izhjVy2zqg "Bayes' rule denominator: discrete and continuous")
	+ [Bayes’ rule: why likelihood is not a probability](https://intranet.hbtn.io/rltoken/UGHHljv4xEmsSkF9r5h4wQ "Bayes' rule: why likelihood is not a probability")


Learning Objectives
-------------------


* What is Bayesian Probability?
* What is Bayes’ rule and how do you use it?
* What is a base rate?
* What is a prior?
* What is a posterior?
* What is a likelihood?


Requirements
------------


### General


* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 16.04 LTS using `python3` (version 3.5)
* Your files will be executed with `numpy` (version 1.15)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/env python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `pycodestyle` style (version 2.5)
* All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* Unless otherwise noted, you are not allowed to import any module except `import numpy as np`
* All your files must be executable
* The length of your files will be tested using `wc`


 Quiz questions
---------------




#### Question #0



Bayes’ rule states that `P(A | B) = P(B | A) * P(A) / P(B)`


What is `P(A | B)`?



* Likelihood
* Marginal probability
* Posterior probability -> asw
* Prior probability







#### Question #1



Bayes’ rule states that `P(A | B) = P(B | A) * P(A) / P(B)`


What is `P(B | A)`?



* Likelihood -> asw
* Marginal probability
* Posterior probability
* Prior probability







#### Question #2



Bayes’ rule states that `P(A | B) = P(B | A) * P(A) / P(B)`


What is `P(A)`?



* Likelihood
* Marginal probability
* Posterior probability
* Prior probability -> asw







#### Question #3



Bayes’ rule states that `P(A | B) = P(B | A) * P(A) / P(B)`


What is `P(B)`?



* Likelihood
* Marginal probability -> asw
* Posterior probability
* Prior probability





* Likelihood
* Marginal probability
* Posterior probability
* Prior probability

Tasks
-----

###  0. Likelihood

You are conducting a study on a revolutionary cancer drug and are looking to find the probability that a patient who takes this drug will develop severe side effects. During your trials, `n` patients take the drug and `x` patients develop severe side effects. You can assume that `x` follows a binomial distribution.

* `x` is the number of patients that develop severe side effects
* `n` is the total number of patients observed
* `P` is a 1D `numpy.ndarray` containing the various hypothetical probabilities of developing severe side effects
* If `n` is not a positive integer, raise a `ValueError` with the message `n must be a positive integer`
* If `x` is not an integer that is greater than or equal to `0`, raise a `ValueError` with the message `x must be an integer that is greater than or equal to 0`
* If `x` is greater than `n`, raise a `ValueError` with the message `x cannot be greater than n`
* If `P` is not a 1D `numpy.ndarray`, raise a `TypeError` with the message `P must be a 1D numpy.ndarray`
* If any value in `P` is not in the range `[0, 1]`, raise a `ValueError` with the message `All values in P must be in the range [0, 1]`
* Returns: a 1D `numpy.ndarray` containing the likelihood of obtaining the data, `x` and `n`, for each probability in `P`, respectively


```
alexa@ubuntu-xenial:0x07-bayesian_prob$ cat 0-main.py 
#!/usr/bin/env python3

if __name__ == '__main__':
    import numpy as np
    likelihood = __import__('0-likelihood').likelihood

    P = np.linspace(0, 1, 11) # [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    print(likelihood(26, 130, P))
alexa@ubuntu-xenial:0x07-bayesian_prob$ ./0-main.py 
[0.00000000e+00 2.71330957e-04 8.71800070e-02 3.07345706e-03
 5.93701546e-07 1.14387595e-12 1.09257177e-20 6.10151799e-32
 9.54415702e-49 1.00596671e-78 0.00000000e+00]
alexa@ubuntu-xenial:0x07-bayesian_prob$

```
###  1. Intersection

Based on `0-likelihood.py`, write a function `def intersection(x, n, P, Pr):` that calculates the intersection of obtaining this data with the various hypothetical probabilities:

* `x` is the number of patients that develop severe side effects
* `n` is the total number of patients observed
* `P` is a 1D `numpy.ndarray` containing the various hypothetical probabilities of developing severe side effects
* `Pr` is a 1D `numpy.ndarray` containing the prior beliefs of `P`
* If `n` is not a positive integer, raise a `ValueError` with the message `n must be a positive integer`
* If `x` is not an integer that is greater than or equal to `0`, raise a `ValueError` with the message `x must be an integer that is greater than or equal to 0`
* If `x` is greater than `n`, raise a `ValueError` with the message `x cannot be greater than n`
* If `P` is not a 1D `numpy.ndarray`, raise a `TypeError` with the message `P must be a 1D numpy.ndarray`
* If `Pr` is not a `numpy.ndarray` with the same shape as `P`, raise a `TypeError` with the message `Pr must be a numpy.ndarray with the same shape as P`
* If any value in `P` or `Pr` is not in the range `[0, 1]`, raise a `ValueError` with the message `All values in {P} must be in the range [0, 1]` where `{P}` is the incorrect variable
* If `Pr` does not sum to `1`, raise a `ValueError` with the message `Pr must sum to 1` **Hint: use [numpy.isclose](https://intranet.hbtn.io/rltoken/7pptg2vy0_-c0qQ9MnZu1w "numpy.isclose")**
* All exceptions should be raised in the above order
* Returns: a 1D `numpy.ndarray` containing the intersection of obtaining `x` and `n` with each probability in `P`, respectively


```
alexa@ubuntu-xenial:0x07-bayesian_prob$ cat 1-main.py 
#!/usr/bin/env python3

if __name__ == '__main__':
    import numpy as np
    intersection = __import__('1-intersection').intersection

    P = np.linspace(0, 1, 11)
    Pr = np.ones(11) / 11 # this prior assumes that everything is equally as likely
    print(intersection(26, 130, P, Pr))
alexa@ubuntu-xenial:0x07-bayesian_prob$ ./1-main.py 
[0.00000000e+00 2.46664506e-05 7.92545518e-03 2.79405187e-04
 5.39728678e-08 1.03988723e-13 9.93247059e-22 5.54683454e-33
 8.67650639e-50 9.14515194e-80 0.00000000e+00]
alexa@ubuntu-xenial:0x07-bayesian_prob$

```
###  2. Marginal Probability

Based on `1-intersection.py`, write a function `def marginal(x, n, P, Pr):` that calculates the marginal probability of obtaining the data:

* `x` is the number of patients that develop severe side effects
* `n` is the total number of patients observed
* `P` is a 1D `numpy.ndarray` containing the various hypothetical probabilities of patients developing severe side effects
* `Pr` is a 1D `numpy.ndarray` containing the prior beliefs about `P`
* If `n` is not a positive integer, raise a `ValueError` with the message `n must be a positive integer`
* If `x` is not an integer that is greater than or equal to `0`, raise a `ValueError` with the message `x must be an integer that is greater than or equal to 0`
* If `x` is greater than `n`, raise a `ValueError` with the message `x cannot be greater than n`
* If `P` is not a 1D `numpy.ndarray`, raise a `TypeError` with the message `P must be a 1D numpy.ndarray`
* If `Pr` is not a `numpy.ndarray` with the same shape as `P`, raise a `TypeError` with the message `Pr must be a numpy.ndarray with the same shape as P`
* If any value in `P` or `Pr` is not in the range `[0, 1]`, raise a `ValueError` with the message `All values in {P} must be in the range [0, 1]` where `{P}` is the incorrect variable
* If `Pr` does not sum to `1`, raise a `ValueError` with the message `Pr must sum to 1`
* All exceptions should be raised in the above order
* Returns: the marginal probability of obtaining `x` and `n`


```
alexa@ubuntu-xenial:0x07-bayesian_prob$ cat 2-main.py 
#!/usr/bin/env python3

if __name__ == '__main__':
    import numpy as np
    marginal = __import__('2-marginal').marginal

    P = np.linspace(0, 1, 11)
    Pr = np.ones(11) / 11
    print(marginal(26, 130, P, Pr))
alexa@ubuntu-xenial:0x07-bayesian_prob$ ./2-main.py 
0.008229580791426582
alexa@ubuntu-xenial:0x07-bayesian_prob$

```
###  3. Posterior

Based on `2-marginal.py`, write a function `def posterior(x, n, P, Pr):` that calculates the posterior probability for the various hypothetical probabilities of developing severe side effects given the data:

* `x` is the number of patients that develop severe side effects
* `n` is the total number of patients observed
* `P` is a 1D `numpy.ndarray` containing the various hypothetical probabilities of developing severe side effects
* `Pr` is a 1D `numpy.ndarray` containing the prior beliefs of `P`
* If `n` is not a positive integer, raise a `ValueError` with the message `n must be a positive integer`
* If `x` is not an integer that is greater than or equal to `0`, raise a `ValueError` with the message `x must be an integer that is greater than or equal to 0`
* If `x` is greater than `n`, raise a `ValueError` with the message `x cannot be greater than n`
* If `P` is not a 1D `numpy.ndarray`, raise a `TypeError` with the message `P must be a 1D numpy.ndarray`
* If `Pr` is not a `numpy.ndarray` with the same shape as `P`, raise a `TypeError` with the message `Pr must be a numpy.ndarray with the same shape as P`
* If any value in `P` or `Pr` is not in the range `[0, 1]`, raise a `ValueError` with the message `All values in {P} must be in the range [0, 1]` where `{P}` is the incorrect variable
* If `Pr` does not sum to `1`, raise a `ValueError` with the message `Pr must sum to 1`
* All exceptions should be raised in the above order
* Returns: the posterior probability of each probability in `P` given `x` and `n`, respectively


```
alexa@ubuntu-xenial:0x07-bayesian_prob$ cat 3-main.py 
#!/usr/bin/env python3

if __name__ == '__main__':
    import numpy as np
    posterior = __import__('3-posterior').posterior

    P = np.linspace(0, 1, 11)
    Pr = np.ones(11) / 11
    print(posterior(26, 130, P, Pr))
alexa@ubuntu-xenial:0x07-bayesian_prob$ ./3-main.py 
[0.00000000e+00 2.99729127e-03 9.63044824e-01 3.39513268e-02
 6.55839819e-06 1.26359684e-11 1.20692303e-19 6.74011797e-31
 1.05430721e-47 1.11125368e-77 0.00000000e+00]
alexa@ubuntu-xenial:0x07-bayesian_prob$

```
###  4. Continuous Posterior

Based on `3-posterior.py`, write a function `def posterior(x, n, p1, p2):` that calculates the posterior probability that the probability of developing severe side effects falls within a specific range given the data:

* `x` is the number of patients that develop severe side effects
* `n` is the total number of patients observed
* `p1` is the lower bound on the range
* `p2` is the upper bound on the range
* You can assume the prior beliefs of `p` follow a uniform distribution
* If `n` is not a positive integer, raise a `ValueError` with the message `n must be a positive integer`
* If `x` is not an integer that is greater than or equal to `0`, raise a `ValueError` with the message `x must be an integer that is greater than or equal to 0`
* If `x` is greater than `n`, raise a `ValueError` with the message `x cannot be greater than n`
* If `p1` or `p2` are not floats within the range `[0, 1]`, raise a`ValueError` with the message `{p} must be a float in the range [0, 1]` where `{p}` is the corresponding variable
* if `p2` <= `p1`, raise a `ValueError` with the message `p2 must be greater than p1`
* The only import you are allowed to use is `from scipy import special`
* Returns: the posterior probability that `p` is within the range `[p1, p2]` given `x` and `n`


```
alexa@ubuntu-xenial:0x07-bayesian_prob$ cat 100-main.py 
#!/usr/bin/env python3

if __name__ == '__main__':
    posterior = __import__('100-continuous').posterior

    print(posterior(26, 130, 0.17, 0.23))
alexa@ubuntu-xenial:0x07-bayesian_prob$ ./100-main.py 
0.6098093274896035
alexa@ubuntu-xenial:0x07-bayesian_prob$

```
---
