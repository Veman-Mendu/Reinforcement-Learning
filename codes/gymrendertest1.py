import gym

env = gym.make("CartPole-v1", render_mode="human")
env.reset()

env.action_space.seed(0)

n_steps = 100
for i in range(n_steps):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    env.render()

env.close()

"""This is a very first sample run for rendering a visualization in open ai gym for reinforcement learning. 
In order to run this simulation in a same loop in order to record rewards for same situation with different actions."""