import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs('./logs', exist_ok=True)


sarsa_logs = pd.read_csv('./logs/rewards_sarsa.csv', index_col=False).iloc[:, 1]
q_logs = pd.read_csv('./logs/rewards_qlearning.csv', index_col=False).iloc[:, 1]


#MJTODO 가시화 잘 하려면, x축이랑 y축에 알맞는 제목이 붙으면 좋을 것 같은데 고민해보고 달아보기
plt.figure(figsize=(16, 8))
plt.plot(q_logs.cumsum() / (pd.Series(np.arange(q_logs.shape[0])) + 1), label="QLearning")
plt.plot(sarsa_logs.cumsum() / (pd.Series(np.arange(sarsa_logs.shape[0])) + 1), label="SARSA")
plt.xlabel('Episode')
plt.ylabel('Average Reward per Episode')
plt.legend()
plt.show()