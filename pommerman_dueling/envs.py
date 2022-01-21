# TODO: Fix the pommerman bug with PR and upgrade the gym version
import gym
from pommerman import make
from pommerman.agents import BaseAgent, SimpleAgent, RandomAgent
from pommerman.constants import Action

__all__ = ['PommermanDuelingSimple', 'PommermanDuelingRandom']


class DummyAgent(BaseAgent):
    def act(self, obs, action_space):
        return Action.Stop


class PommermanDueling(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, enemy):
        agent_index = 0  # TODO: Randomize the initial position
        agents = [DummyAgent() if i == agent_index else enemy for i in range(2)]

        self.env = make('OneVsOne-v0', agents)
        self.env.set_training_agent(agent_index)
        self.action_space = self.env.action_space
        self.observation_space = self.env.observation_space

    def step(self, action):
        obs = self.env.get_observations()
        all_actions = self.env.act(obs)
        all_actions.insert(self.env.training_agent, action)

        states, rewards, done, info = self.env.step(all_actions)

        agent_state = self.env.featurize(states[self.env.training_agent])
        agent_reward = rewards[self.env.training_agent]
        return agent_state, done, agent_reward, info

    def reset(self):
        obs = self.env.reset()
        agent_obs = self.env.featurize(obs[0])
        return agent_obs

    def render(self, *args, **kwargs):
        self.env.render(*args, **kwargs)


class PommermanDuelingSimple(PommermanDueling):
    def __init__(self):
        super().__init__(SimpleAgent())


class PommermanDuelingRandom(PommermanDueling):
    def __init__(self):
        super().__init__(RandomAgent())


if __name__ == "__main__":
    def main():
        for env in [PommermanDuelingRandom(), PommermanDuelingSimple()]:
            print(env.observation_space())
            print(env.observation_space)
            print(env.action_space)

            env.reset()
            done = False

            while not done:
                state, done, reward, info = env.step(env.action_space.sample())
                env.render()


    main()
