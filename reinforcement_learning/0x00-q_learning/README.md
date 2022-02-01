# 0x00. Q-learning

## Resources :books:
Read or watch:
* [An introduction to Reinforcement Learning](https://www.youtube.com/watch?v=JgvyzIkgxF0)
* [Simple Reinforcement Learning: Q-learning](https://intranet.hbtn.io/rltoken/xKv23nvnS3U44xH4RObU4Q)
* [Markov Decision Processes (MDPs) - Structuring a Reinforcement Learning Problem](https://www.youtube.com/watch?v=my207WNoeyA&feature=youtu.be&t=18)
* [Expected Return - What Drives a Reinforcement Learning Agent in an MDP](https://www.youtube.com/watch?v=a-SnJtmBtyA&feature=youtu.be&list=PLZbbT5o_s2xoWNVdDudn51XM8lOuZ_Njv&t=23)
* [Policies and Value Functions - Good Actions for a Reinforcement Learning Agent](https://www.youtube.com/watch?v=eMxOGwbdqKY&feature=youtu.be&list=PLZbbT5o_s2xoWNVdDudn51XM8lOuZ_Njv&t=23)
* [What do Reinforcement Learning Algorithms Learn - Optimal Policies](https://www.youtube.com/watch?v=rP4oEpQbDm4&feature=youtu.be&list=PLZbbT5o_s2xoWNVdDudn51XM8lOuZ_Njv&t=20)
* [Q-Learning Explained - A Reinforcement Learning Technique](https://www.youtube.com/watch?v=qhRNvCVVJaA&feature=youtu.be&list=PLZbbT5o_s2xoWNVdDudn51XM8lOuZ_Njv&t=26)
* [Exploration vs. Exploitation - Learning the Optimal Reinforcement Learning Policy](https://www.youtube.com/watch?v=mo96Nqlo1L8&feature=youtu.be&list=PLZbbT5o_s2xoWNVdDudn51XM8lOuZ_Njv&t=24)
* [OpenAI Gym and Python for Q-learning - Reinforcement Learning Code Project](https://www.youtube.com/watch?v=QK_PP_2KgGE&feature=youtu.be&list=PLZbbT5o_s2xoWNVdDudn51XM8lOuZ_Njv&t=25)
* [Train Q-learning Agent with Python - Reinforcement Learning Code Project](https://www.youtube.com/watch?v=HGeI30uATws&feature=youtu.be&list=PLZbbT5o_s2xoWNVdDudn51XM8lOuZ_Njv&t=24)
* [Markov Decision Processes](https://www.youtube.com/watch?v=KovN7WKI9Y0)

---
## Learning Objectives :bulb:
What you should learn from this project:

* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 16.04 LTS using python3 (version 3.5)
* Your files will be executed with numpy (version 1.15), and gym (version 0.7)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/env python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle style (version 2.4)
* All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* All your files must be executable
* Your code should use the minimum number of operations

---

## Links to Files :file_folder:

### [0. Load the Environment](./0-load_env.py)
* Write a function def load_frozen_lake(desc=None, map_name=None, is_slippery=False): that loads the pre-made FrozenLakeEnv evnironment from OpenAI’s gym:


### [1. Initialize Q-table](./1-q_init.py)
* Write a function def q_init(env): that initializes the Q-table:


### [2. Epsilon Greedy](./2-epsilon_greedy.py)
* Write a function def epsilon_greedy(Q, state, epsilon): that uses epsilon-greedy to determine the next action:


### [3. Q-learning](./3-q_learning.py)
* Write the function def train(env, Q, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99, epsilon=1, min_epsilon=0.1, epsilon_decay=0.05): that performs Q-learning:


### [4. Play](./4-play.py)
* Write a function def play(env, Q, max_steps=100): that has the trained agent play an episode:

---

## Author
* **Gabriel Cifuentes** - [gcifuentess](https://github.com/gcifuentess)


---
---

# *HBTN PROJECT:*


![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/8/5478322429e44f196aff6896f42ce2ea0741ba36.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220201%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220201T022203Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4d1b942250d3a15cd3514de757215c7f33e5568142fc1dc84dfb7209be1bd34d)


Resources
---------


**Read or watch**:


* [An introduction to Reinforcement Learning](https://intranet.hbtn.io/rltoken/uSJcrn4-wamVCfbQQtI9EA "An introduction to Reinforcement Learning")
* [Simple Reinforcement Learning: Q-learning](https://intranet.hbtn.io/rltoken/xKv23nvnS3U44xH4RObU4Q "Simple Reinforcement Learning: Q-learning")
* [Markov Decision Processes (MDPs) - Structuring a Reinforcement Learning Problem](https://intranet.hbtn.io/rltoken/km2Nyp6zyAast1k5v9P_wQ "Markov Decision Processes (MDPs) - Structuring a Reinforcement Learning Problem")
* [Expected Return - What Drives a Reinforcement Learning Agent in an MDP](https://intranet.hbtn.io/rltoken/mM6iGVu8uSr7siZJCM-D-Q "Expected Return - What Drives a Reinforcement Learning Agent in an MDP")
* [Policies and Value Functions - Good Actions for a Reinforcement Learning Agent](https://intranet.hbtn.io/rltoken/HgOMxHB7SipUwDk6s3ZhUA "Policies and Value Functions - Good Actions for a Reinforcement Learning Agent")
* [What do Reinforcement Learning Algorithms Learn - Optimal Policies](https://intranet.hbtn.io/rltoken/Pd4kGKXr9Pd0qQ4RO93Xww "What do Reinforcement Learning Algorithms Learn - Optimal Policies")
* [Q-Learning Explained - A Reinforcement Learning Technique](https://intranet.hbtn.io/rltoken/vj2E0Jizi5qUKn6hLUnVSQ "Q-Learning Explained - A Reinforcement Learning Technique")
* [Exploration vs. Exploitation - Learning the Optimal Reinforcement Learning Policy](https://intranet.hbtn.io/rltoken/zQNxN36--R7hzP0ktiKOsg "Exploration vs. Exploitation - Learning the Optimal Reinforcement Learning Policy")
* [OpenAI Gym and Python for Q-learning - Reinforcement Learning Code Project](https://intranet.hbtn.io/rltoken/GMcf0lCJ-SlaF6FSUKaozA "OpenAI Gym and Python for Q-learning - Reinforcement Learning Code Project")
* [Train Q-learning Agent with Python - Reinforcement Learning Code Project](https://intranet.hbtn.io/rltoken/GE2nKBHgehHdd_XN7lK0Gw "Train Q-learning Agent with Python - Reinforcement Learning Code Project")
* [Markov Decision Processes](https://intranet.hbtn.io/rltoken/Dz37ih49PpmrJicq_IP3aA "Markov Decision Processes")


**Definitions to skim:**


* [Reinforcement Learning](https://intranet.hbtn.io/rltoken/z1eKcn91HbmHYtdwYEEXOQ "Reinforcement Learning")
* [Markov Decision Process](https://intranet.hbtn.io/rltoken/PCdKyrHQRNARmxeSUCiOYQ "Markov Decision Process")
* [Q-learning](https://intranet.hbtn.io/rltoken/T80msozXZ3wlSmq0ScCvrQ "Q-learning")


**References**:


* [OpenAI Gym](https://intranet.hbtn.io/rltoken/P8gDRc_PRTeK4okeztvmDQ "OpenAI Gym")
* [OpenAI Gym: Frozen Lake env](https://github.com/openai/gym/blob/master/gym/envs/toy_text/frozen_lake.py "OpenAI Gym: Frozen Lake env")


Learning Objectives
-------------------


* What is a Markov Decision Process?
* What is an environment?
* What is an agent?
* What is a state?
* What is a policy function?
* What is a value function? a state-value function? an action-value function?
* What is a discount factor?
* What is the Bellman equation?
* What is epsilon greedy?
* What is Q-learning?


Requirements
------------


### General


* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 16.04 LTS using `python3` (version 3.5)
* Your files will be executed with `numpy` (version 1.15), and `gym` (version 0.7)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/env python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `pycodestyle` style (version 2.4)
* All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* All your files must be executable
* **Your code should use the minimum number of operations**


Installing OpenAI’s Gym
-----------------------



```
pip install --user gym

```

 Quiz questions
---------------




#### 
 
 Question #0



What is reinforcement learning?



* A type of supervised learning, because the rewards supervise the learning
* A type of unsupervised learning, because there are no labels for each action
* Its own subcategory of machine learning -> asw







#### 
 
 Question #1



What is an environment?



* The place in which actions can be performed -> asw
* A description of what the agent sees
* A list of actions that can be performed
* A description of which actions the agent should perform







#### 
 
 Question #2



An agent chooses its action based on:



* The current state -> asw
* The value function -> asw
* The policy function -> asw
* The previous reward -> asw







#### 
 
 Question #3



What is a policy function?



* A description of how the agent should be rewarded
* A description of how the agent should behave -> asw
* A description of how the agent could be rewarded in the future
* A function that is learned -> asw
* A function that is set at the beginning







#### 
 
 Question #4



What is a value function?



* A description of how the agent should be rewarded
* A description of how the agent should behave
* A description of how the agent could be rewarded in the future -> asw
* A function that is learned -> asw
* A function that is set at the beginning







#### 
 
 Question #5



What is epsilon-greedy?



* A type of policy function
* A type of value function
* A way to balance policy and value functions
* A balance exploration and exploitation -> asw







#### 
 
 Question #6



What is Q-learning?



* A reinforcement learning algorithm -> asw
* A deep reinforcement learning algorithm
* A value-based learning algorithm -> asw
* A policy-based learning algorithm
* A model-based approach





* A type of supervised learning, because the rewards supervise the learning
* A type of unsupervised learning, because there are no labels for each action
* Its own subcategory of machine learning

Tasks
-----

###  0. Load the Environment

Write a function `def load_frozen_lake(desc=None, map_name=None, is_slippery=False):` that loads the pre-made `FrozenLakeEnv` evnironment from OpenAI’s `gym`:

* `desc` is either `None` or a list of lists containing a custom description of the map to load for the environment
* `map_name` is either `None` or a string containing the pre-made map to load
* *Note: If both `desc` and `map_name` are `None`, the environment will load a randomly generated 8x8 map*
* `is_slippery` is a boolean to determine if the ice is slippery
* Returns: the environment


```
$ cat 0-main.py
#!/usr/bin/env python3

load_frozen_lake = __import__('0-load_env').load_frozen_lake
import numpy as np

np.random.seed(0)
env = load_frozen_lake()
print(env.desc)
print(env.P[0][0])
env = load_frozen_lake(is_slippery=True)
print(env.desc)
print(env.P[0][0])
desc = [['S', 'F', 'F'], ['F', 'H', 'H'], ['F', 'F', 'G']]
env = load_frozen_lake(desc=desc)
print(env.desc)
env = load_frozen_lake(map_name='4x4')
print(env.desc)
$ ./0-main.py
[[b'S' b'F' b'F' b'F' b'F' b'F' b'F' b'H']
 [b'H' b'F' b'F' b'F' b'F' b'H' b'F' b'F']
 [b'F' b'H' b'F' b'H' b'H' b'F' b'F' b'F']
 [b'F' b'F' b'F' b'H' b'F' b'F' b'F' b'F']
 [b'F' b'F' b'F' b'F' b'F' b'F' b'H' b'F']
 [b'F' b'F' b'F' b'F' b'F' b'F' b'F' b'F']
 [b'F' b'F' b'F' b'F' b'H' b'F' b'F' b'F']
 [b'F' b'F' b'F' b'F' b'F' b'F' b'F' b'G']]
[(1.0, 0, 0.0, False)]
[[b'S' b'F' b'H' b'F' b'H' b'F' b'H' b'F']
 [b'H' b'F' b'F' b'F' b'F' b'F' b'F' b'F']
 [b'F' b'F' b'F' b'F' b'F' b'F' b'F' b'F']
 [b'F' b'H' b'F' b'F' b'F' b'F' b'F' b'F']
 [b'F' b'F' b'H' b'F' b'F' b'F' b'F' b'H']
 [b'F' b'F' b'F' b'F' b'F' b'H' b'F' b'H']
 [b'F' b'F' b'H' b'F' b'H' b'F' b'H' b'F']
 [b'F' b'F' b'H' b'F' b'F' b'F' b'F' b'G']]
[(0.3333333333333333, 0, 0.0, False), (0.3333333333333333, 0, 0.0, False), (0.3333333333333333, 8, 0.0, True)]
[[b'S' b'F' b'F']
 [b'F' b'H' b'H']
 [b'F' b'F' b'G']]
[[b'S' b'F' b'F' b'F']
 [b'F' b'H' b'F' b'H']
 [b'F' b'F' b'F' b'H']
 [b'H' b'F' b'F' b'G']]
$

```
###  1. Initialize Q-table

Write a function `def q_init(env):` that initializes the Q-table:

* `env` is the `FrozenLakeEnv` instance
* Returns: the Q-table as a `numpy.ndarray` of zeros


```
$ cat 1-main.py
#!/usr/bin/env python3

load_frozen_lake = __import__('0-load_env').load_frozen_lake
q_init = __import__('1-q_init').q_init

env = load_frozen_lake()
Q = q_init(env)
print(Q.shape)
env = load_frozen_lake(is_slippery=True)
Q = q_init(env)
print(Q.shape)
desc = [['S', 'F', 'F'], ['F', 'H', 'H'], ['F', 'F', 'G']]
env = load_frozen_lake(desc=desc)
Q = q_init(env)
print(Q.shape)
env = load_frozen_lake(map_name='4x4')
Q = q_init(env)
print(Q.shape)
$ ./1-main.py
(64, 4)
(64, 4)
(9, 4)
(16, 4)
$

```
###  2. Epsilon Greedy

Write a function `def epsilon_greedy(Q, state, epsilon):` that uses epsilon-greedy to determine the next action:

* `Q` is a `numpy.ndarray` containing the q-table
* `state` is the current state
* `epsilon` is the epsilon to use for the calculation
* You should sample `p` with `numpy.random.uniformn` to determine if your algorithm should explore or exploit
* If exploring, you should pick the next action with `numpy.random.randint` from all possible actions
* Returns: the next action index


```
$ cat 2-main.py
#!/usr/bin/env python3

load_frozen_lake = __import__('0-load_env').load_frozen_lake
q_init = __import__('1-q_init').q_init
epsilon_greedy = __import__('2-epsilon_greedy').epsilon_greedy
import numpy as np

desc = [['S', 'F', 'F'], ['F', 'H', 'H'], ['F', 'F', 'G']]
env = load_frozen_lake(desc=desc)
Q = q_init(env)
Q[7] = np.array([0.5, 0.7, 1, -1])
np.random.seed(0)
print(epsilon_greedy(Q, 7, 0.5))
np.random.seed(1)
print(epsilon_greedy(Q, 7, 0.5))
$ ./2-main.py
2
0
$

```
###  3. Q-learning

Write the function `def train(env, Q, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99, epsilon=1, min_epsilon=0.1, epsilon_decay=0.05):` that performs Q-learning:

* `env` is the `FrozenLakeEnv` instance
* `Q` is a `numpy.ndarray` containing the Q-table
* `episodes` is the total number of episodes to train over
* `max_steps` is the maximum number of steps per episode
* `alpha` is the learning rate
* `gamma` is the discount rate
* `epsilon` is the initial threshold for epsilon greedy
* `min_epsilon` is the minimum value that `epsilon` should decay to
* `epsilon_decay` is the decay rate for updating `epsilon` between episodes
* When the agent falls in a hole, the reward should be updated to be `-1`
* Returns: `Q, total_rewards`
	+ `Q` is the updated Q-table
	+ `total_rewards` is a list containing the rewards per episode


```
$ cat 3-main.py
#!/usr/bin/env python3

load_frozen_lake = __import__('0-load_env').load_frozen_lake
q_init = __import__('1-q_init').q_init
train = __import__('3-q_learning').train
import numpy as np

np.random.seed(0)
desc = [['S', 'F', 'F'], ['F', 'H', 'H'], ['F', 'F', 'G']]
env = load_frozen_lake(desc=desc)
Q = q_init(env)

Q, total_rewards  = train(env, Q)
print(Q)
split_rewards = np.split(np.array(total_rewards), 10)
for i, rewards in enumerate(split_rewards):
    print((i+1) * 500, ':', np.mean(rewards))
$ ./3-main.py
[[ 0.96059593  0.970299    0.95098488  0.96059396]
 [ 0.96059557 -0.77123208  0.0094072   0.37627228]
 [ 0.18061285 -0.1         0.          0.        ]
 [ 0.97029877  0.9801     -0.99999988  0.96059583]
 [ 0.          0.          0.          0.        ]
 [ 0.          0.          0.          0.        ]
 [ 0.98009763  0.98009933  0.99        0.9702983 ]
 [ 0.98009922  0.98999782  1.         -0.99999952]
 [ 0.          0.          0.          0.        ]]
500 : 0.812
1000 : 0.88
1500 : 0.9
2000 : 0.9
2500 : 0.88
3000 : 0.844
3500 : 0.892
4000 : 0.896
4500 : 0.852
5000 : 0.928
$

```
###  4. Play

Write a function `def play(env, Q, max_steps=100):` that has the trained agent play an episode:

* `env` is the `FrozenLakeEnv` instance
* `Q` is a `numpy.ndarray` containing the Q-table
* `max_steps` is the maximum number of steps in the episode
* Each state of the board should be displayed via the console
* You should always exploit the Q-table
* Returns: the total rewards for the episode


```
$ cat 4-main.py
#!/usr/bin/env python3

load_frozen_lake = __import__('0-load_env').load_frozen_lake
q_init = __import__('1-q_init').q_init
train = __import__('3-q_learning').train
play = __import__('4-play').play

import numpy as np

np.random.seed(0)
desc = [['S', 'F', 'F'], ['F', 'H', 'H'], ['F', 'F', 'G']]
env = load_frozen_lake(desc=desc)
Q = q_init(env)

Q, total_rewards  = train(env, Q)
print(play(env, Q))
$ ./4-main.py

`S`FF
FHH
FFG
  (Down)
SFF
`F`HH
FFG
  (Down)
SFF
FHH
`F`FG
  (Right)
SFF
FHH
F`F`G
  (Right)
SFF
FHH
FF`G`
1.0
$

```
---
