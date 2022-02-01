#!/usr/bin/env python3
"""Play"""
import numpy as np


def play(env, Q, max_steps=100):
    """has the trained agent play an episode
    Args:
        env is the FrozenLakeEnv instance
        Q is a numpy.ndarray containing the Q-tabl e
        max_steps is the maximum number of steps in the episode
        Each state of the board should be displayed via the console
        You should always exploit the Q-table

    Returns: the total rewards for the episode
    """
    rewards = 0
    state = env.reset()
    env.render()

    for i in range(max_steps):

        act = np.argmax(Q[state, :])
        new_state, reward, done, info = env.step(act)
        state = new_state
        rewards += reward
        env.render()

        if done:
            break

    return rewards
