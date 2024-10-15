# Reinforcement Learning Results and Code Overview
 **MiniGrid-Empty-6x6**과 **MiniGrid-Crossing** 두 환경에서 수행된 강화 학습 실험의 결과와 코드가 포함되어 있습니다. 결과는 각 작업(task)별로 정리했습니다.


## Repository Structure
- **empty_6x6/**
  - MiniGrid-Empty-6x6 환경에서 수행된 실험 결과가 포함되어 있습니다.
  -각 실험의 에이전트 수행 영상, 학습된 Q-값, 보상 그래프
  -보상 그래프는 에피소드 수에 따라 나뉘어 있어 에이전트의 학습 경과를 비교할 수 있습니다.


- **crossing/**
  -MiniGrid-Crossing 환경에서 수행된 실험 결과가 포함되어 있습니다.
  -에이전트 수행 영상, 학습된 Q-값, 보상 그래프
  -보상 그래프는 다양한 하이퍼파라미터와 에피소드 수에 따른 최적 구성을 비교하여 보여줍니다.


- **code/**
  - 모든 실험에 사용된 소스 코드가 포함되어 있습니다.
  -각 환경 및 실험 설정에 대한 개별 Python 스크립트가 있으며, SARSA와 Q-learning 구현이 포함되어 있습니다.

### Code
  -SARSA와 Q-learning: MiniGrid 환경에서 에이전트를 학습시키기 위한 SARSA와 Q-learning 알고리즘의 구현이 포함되어 있습니다.

