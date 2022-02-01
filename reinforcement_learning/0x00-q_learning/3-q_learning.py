#!/usr/bin/env python3
"""Q-learning"""
import numpy as np


def train(env, Q, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99,
          epsilon=1, min_epsilon=0.1, epsilon_decay=0.05):
    """performs Q-learning:
    Args:
        env is the FrozenLakeEnv instance
        Q is a numpy.ndarray containing the Q-table
        episodes is the total number of episodes to train over
        max_steps is the maximum number of steps per episode
        alpha is the learning rate
        gamma is the discount rate
        epsilon is the initial threshold for epsilon greedy
        min_epsilon is the minimum value that epsilon should decay to
        epsilon_decay is the decay rate for updating epsilon between episodes
        When the agent falls in a hole, the reward should be updated to be -1

    Returns: Q, total_rewards
        Q is the updated Q-table
        total_rewards is a list containing the rewards per episode
    """
    max_epsilon = epsilon
    rewards = []

    for i in range(episodes):

        current_rew = 0
        state = env.reset()
        done = False

        for j in range(max_steps):

            act = epsilon_greedy(Q, state, epsilon)
            new_state, reward, done, info = env.step(act)

            if done and reward == 0:
                reward = -1

            Q[state, act] = (
                Q[state, act] * (1 - alpha) + alpha *
                (reward + gamma * np.max(Q[new_state, :]))
            )
            current_rew += reward

            if done:
                break

            state = new_state

        epsilon = (
            min_epsilon + (max_epsilon - min_epsilon) *
            np.exp(-epsilon_decay * i)
        )
        rewards.append(current_rew)

    return Q, rewards


def epsilon_greedy(Q, state, epsilon):
    """uses epsilon-greedy to determine the next action
    Args:
        Q is a numpy.ndarray containing the q-table
        state is the current state
        epsilon is the epsilon to use for the calculation
        You should sample p with numpy.random.uniformn to determine if your
            algorithm should explore or exploit
        If exploring, you should pick the next action with
            numpy.random.randint from all possible actions

    Returns: the next action index
    """
    limit = np.random.uniform(0, 1)

    if epsilon < limit:
        idx = np.argmax(Q[state, :])
    else:
        idx = np.random.randint(Q.shape[1])

    return idx
