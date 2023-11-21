import gym

env = gym.make("CartPole-v1", render_mode="human")

n_episodes = 10
n_steps = 100

for episode in range(n_episodes):
    observation = env.reset()

    for step in range(n_steps):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, truncated, info = env.step(action)

        if done:
            print(f"Episode Number: {episode}, Time Steps taken: {step}")
            break

env.close()

"""This example shows how to run a task as a episode and record values related to the task.
Here the observation, reward, done, truncated, info are the variables used to record information of each step in every episode 1 after another."""