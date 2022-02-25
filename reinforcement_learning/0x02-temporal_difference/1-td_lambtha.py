#!/usr/bin/env python3
'''TD lampda'''
import numpy as np


def td_lambtha(env, V, policy, lambtha, episodes=5000,
               max_steps=100, alpha=0.1, gamma=0.99):
    '''performs the TD(λ) algorithm:
    Args:
        env is the openAI environment instance
        V is a numpy.ndarray of shape (s,) containing the value estimate
        policy is a function that takes in a state and returns the next action
               to take
        lambtha is the eligibility trace factor
        episodes is the total number of episodes to train over
        max_steps is the maximum number of steps per episode
        alpha is the learning rate
        gamma is the discount rate

    Returns: V, the updated value estimate
        states = V.shape[0]
        elig = np.zeros(states)
    '''

    states = V.shape[0]
    elig = np.zeros(states)

    for i in range(episodes):
        s = env.reset()

        for j in range(max_steps):
            action = policy(s)
            new, reward, done, info = env.step(action)

            elig[s] += 1.0

            delta = reward + gamma * V[new] - V[s]

            V += alpha * delta * elig
            elig *= lambtha * gamma
            if done:
                break
            else:
                s = new

        return V
