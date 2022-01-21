# Pommerman Dueling

A single-agent environment for dueling with the rule-based Pommerman agent (`SimpleAgent` or `RandomAgent`)

For more information on Pommerman, check out: <https://github.com/MultiAgentLearning/playground>

## Install

```shell
git clone
cd pommerman-dueling
pip install -e .
```

## Getting Started

```python
import gym
import pommerman_dueling

env = gym.make('PommermanDuelingSimple-v0')
print(env.observation_space)
print(env.action_space)

for _ in range(10):
    state = env.reset()
    done = False

    while not done:
        env.render()
        state, done, reward, info = env.step(env.action_space.sample())
        print(state)
env.close()
```