env_name = "CartPole-v0"
episodes = 10
timesteps = 100
gamma = 1
seed = 46

import gym
import sampleagent
import numpy as np

env = gym.make(env_name)

agent = sampleagent.make_agent(env.action_space, seed)

episode_returns = []

for episode_number in range(episodes):
    gamma_cum = 1
    episode_return = 0

    observation = env.reset()

    for time_step in range(timesteps):
        env.render()
        action = agent.pi(observation)
        observation, reward, done, truncated, info = env.step(action)

        episode_return += reward*gamma_cum
        gamma_cum = gamma_cum*gamma

        if done:
            print(f"Episode Number: {episode_number}, Timesteps: {time_step}, Return: {episode_return}")
            break

    episode_returns.append(episode_return)

env.close()

avg_return = np.mean(episode_returns)
std_return = np.std(episode_returns)
var_return = std_return**2

print(f"Statistics on Return Average: {avg_return}, Variance: {var_return}")