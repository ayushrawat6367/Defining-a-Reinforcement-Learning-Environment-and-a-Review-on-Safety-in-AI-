# Defining a Reinforcement Learning Environment and a Review on Safety in AI

This project involves defining a custom reinforcement learning (RL) environment using the OpenAI Gym framework. Additionally, it includes a review of safety considerations in AI, particularly in the context of reinforcement learning.

## Project Overview

The main components of this project are:
1. **Custom Grid Environment:** An RL environment where an agent navigates a grid to reach a goal while avoiding obstacles.
2. **Safety Review in AI:** A review on the importance of safety in AI, with a focus on RL applications.

## Custom Grid Environment

The custom environment, `GridEnv`, is a 4x4 grid where the agent starts at position (0, 0) and aims to reach the goal at position (3, 3). The agent receives rewards or penalties based on its actions and the resulting state.

### Environment Details

- **Observation Space:** 16 discrete states representing the flattened grid.
- **Action Space:** 4 discrete actions (0: down, 1: up, 2: right, 3: left).
- **Rewards:**
  - Reaching the goal: +10
  - Specific positions have additional rewards/penalties:
    - (0, 1): -3
    - (0, 4): +2
    - (2, 3): -2
    - (3, 2): +5
- **Termination:** The episode ends after 10 timesteps or when the goal is reached.

### Key Functions

- **reset():** Resets the environment to the initial state.
- **step(action):** Takes an action and returns the new state, reward, done flag, and additional info.
- **render():** Visualizes the current state of the grid.
