# 0x02. Hidden Markov Models

## Resources:books:
Read or watch:
* [Markov property](https://intranet.hbtn.io/rltoken/F7v-6UX8GSo7tcrLuj3pTg)
* [Markov Chain](https://intranet.hbtn.io/rltoken/pJySWk8zYyiFBbXha1v9Uw)
* [Properties of Markov Chains](https://intranet.hbtn.io/rltoken/tJPuYPGZmTCCiajHOHzHPg)
* [Markov Chains](https://intranet.hbtn.io/rltoken/ek3QosV9fS9Ep7hF7Z8UNA)
* [Markov Matrices](https://intranet.hbtn.io/rltoken/ismECln2KQ_NWqlhDi4SOA)
* [1.3 Convergence of Regular Markov Chains](https://intranet.hbtn.io/rltoken/-P79YH94sPDmW3witwXEgA)
* [Markov Chains, Part 1](https://intranet.hbtn.io/rltoken/Gphacn9fdFCQFGMeMyYxlg)
* [Markov Chains, Part 2](https://intranet.hbtn.io/rltoken/flDg5iw0va1FhUjsMFHgdg)
* [Markov Chains, Part 3](https://intranet.hbtn.io/rltoken/zRg0ddD8arH7F1hiOlaNiA)
* [Markov Chains, Part 4](https://intranet.hbtn.io/rltoken/AD3VcrR0vmdPkLIHFCWd2Q)
* [Markov Chains, Part 5](https://intranet.hbtn.io/rltoken/V7XdIdjg5NJpuWgV_tVk3A)
* [Markov Chains, Part 7](https://intranet.hbtn.io/rltoken/Iyup5UA69u1UYzIsgcn4Fg)
* [Markov Chains, Part 8](https://intranet.hbtn.io/rltoken/wXvkFVOTl3NOKWgT63odOw)
* [Markov Chains, Part 9](https://intranet.hbtn.io/rltoken/UC94QIzIwcX280YAvJTJUA)
* [Hidden Markov model](https://intranet.hbtn.io/rltoken/Qg8C9pzP1Yr4P8bxECb7pQ)
* [Hidden Markov Models](https://intranet.hbtn.io/rltoken/D4kPhrRbShrDWSANnlJdkQ)
* [(ML 14.1) Markov models - motivating examples](https://intranet.hbtn.io/rltoken/CpcwO0SbMD05S7IOfc3jeA)
* [(ML 14.2) Markov chains (discrete-time) (part 1)](https://intranet.hbtn.io/rltoken/C-TgJ6CKgBUbL3yxfvJHqA)
* [(ML 14.3) Markov chains (discrete-time) (part 2)](https://intranet.hbtn.io/rltoken/zMjTTG-qtP0QfcbYXFujUg)
* [(ML 14.4) Hidden Markov models (HMMs) (part 1)](https://intranet.hbtn.io/rltoken/tMsk_K-n0mYOtsthhBrQcg)
* [(ML 14.5) Hidden Markov models (HMMs) (part 2)](https://intranet.hbtn.io/rltoken/2k8q4yyclHlMoE83WhKf8g)
* [(ML 14.6) Forward-Backward algorithm for HMMs](https://intranet.hbtn.io/rltoken/Qljf3X5iH7oaKWuF2I165A)
* [(ML 14.7) Forward algorithm (part 1)](https://intranet.hbtn.io/rltoken/Tc6D_BMgvdxMWGoBtvo-Nw)
* [(ML 14.8) Forward algorithm (part 2)](https://intranet.hbtn.io/rltoken/AMUSX-wBTAeTsvJKFlOiIQ)
* [(ML 14.9) Backward algorithm](https://intranet.hbtn.io/rltoken/GuKHZZ4HNUS-xnbwBf8YsQ)
* [(ML 14.10) Underflow and the log-sum-exp trick](https://intranet.hbtn.io/rltoken/uZ3KdzsuS0YmbvxDD2G-NQ)
* [(ML 14.11) Viterbi algorithm (part 1)](https://intranet.hbtn.io/rltoken/UAmz_LJdG5w3sS_8xSAsGg)
* [(ML 14.12) Viterbi algorithm (part 2)](https://intranet.hbtn.io/rltoken/c0LxuyQ8HeprSObqEVkTQA)

---
## Learning Objectives:bulb:
What you should learn from this project:

* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 16.04 LTS using python3 (version 3.5)
* Your files will be executed with numpy (version 1.15)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/env python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle style (version 2.4)
* All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* Unless otherwise noted, you are not allowed to import any module except import numpy as np
* All your files must be executable

---
---

## Author
* **Gabriel Cifuentes** - [gcifuentess](https://github.com/gcifuentess)