#!/usr/bin/env python3
'''SARSA(λ)'''
import numpy as np


def sarsa_lambtha(env, Q, lambtha, episodes=5000,
                  max_steps=100, alpha=0.1, gamma=0.99,
                  epsilon=1, min_epsilon=0.1, epsilon_decay=0.05):
    '''performs SARSA(λ):

    Args:
        env is the openAI environment instance
        Q is a numpy.ndarray of shape (s,a) containing the Q table
        lambtha is the eligibility trace factor
        episodes is the total number of episodes to train over
        max_steps is the maximum number of steps per episode
        alpha is the learning rate
        gamma is the discount rate
        epsilon is the initial threshold for epsilon greedy
        min_epsilon is the minimum value that epsilon should decay to
        epsilon_decay is the decay rate for updating epsilon between episodes

    Returns: Q, the updated Q table
'''
    init_epsilon = epsilon
    states = Q.shape[0]
    elig = np.zeros(Q.shape)

    for i in range(episodes):
        s = env.reset()

        action = 0
        if np.random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[s, :])

        for j in range(max_steps):
            s_new, reward, done, info = env.step(action)

            greedy = 0
            if np.random.uniform(0, 1) < epsilon:
                greedy = env.action_space.sample()
            else:
                greedy = np.argmax(Q[s, :])

            elig *= gamma * epsilon
            elig[s, action] += (1.0)

            delta = reward + gamma * Q[s_new, greedy] - Q[s, action]
            Q += alpha * delta * elig

            if done:
                break

            s = s_new

        if epsilon < min_epsilon:
            epsilon = min_epsilon
        else:
            epsilon *= init_epsilon * np.exp(-epsilon_decay * i)

    return Q
