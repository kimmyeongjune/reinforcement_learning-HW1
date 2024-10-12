# Reinforcement Learning Results and Code Overview

This repository contains the results and code for reinforcement learning experiments conducted in two environments: **MiniGrid-Empty-6x6** and **MiniGrid-Crossing**. The results are organized by task, and the repository structure is designed to make it easy to navigate between the different experimental outcomes and the corresponding code.

## Repository Structure

- **empty_6x6/**
  - Contains results from experiments conducted in the **MiniGrid-Empty-6x6** environment.
  - **Videos** of agent performances, **Q-values** after training, and **reward plots** for each experiment are provided.
  - Reward plots are separated based on the number of episodes, allowing for comparison of agent learning over time.

- **crossing/**
  - Contains results from experiments conducted in the **MiniGrid-Crossing** environment.
  - Includes **videos** of the agent's performance, **Q-values** from training, and **reward plots**.
  - Reward plots highlight comparisons between **different hyperparameters** and the **number of episodes** to showcase the optimal configuration for this environment.

- **code/**
  - Contains the source code used for all the experiments.
  - Separate Python scripts for each environment and experiment setup, including SARSA and Q-learning implementations.

## Contents Overview

### Empty 6x6 Environment
The **empty_6x6** folder includes visual and numerical results of reinforcement learning agents trained using different numbers of episodes. This allows for a detailed comparison of how the agents' performance evolves over time. You can find:

- **Episode Reward Plots**: Graphs showing reward trends as episodes progress.
- **Performance Videos**: Demonstrations of the agent's learned behavior.
- **Q-Values**: The learned Q-values, which provide insights into the agent's decision-making process.

### Crossing Environment
The **crossing** folder presents the outcomes of reinforcement learning agents trained in a more complex environment. The focus of these experiments was on finding optimal hyperparameters for effective training. The folder includes:

- **Hyperparameter Comparisons**: Plots showing the effect of different hyperparameter settings and episode counts.
- **Performance Videos**: Visual demonstration of agent behavior when using optimal configurations.
- **Q-Values**: Information on how the Q-values evolved during training.

### Code
The **code** folder provides all the scripts used in these experiments, including those for:

- **Environment Wrappers**: Custom wrappers to modify the environments.
- **SARSA and Q-Learning**: Implementations of both SARSA and Q-learning algorithms for training agents in the MiniGrid environments.

## Usage
To explore the results:
1. **Navigate** to the respective folders (`empty_6x6/` or `crossing/`) to see the outcomes from each environment.
2. **Run the Code**: You can use the scripts in the `code/` folder to reproduce the experiments or modify the settings for further exploration.

Feel free to contribute by suggesting improvements, running new experiments, or submitting pull requests!

