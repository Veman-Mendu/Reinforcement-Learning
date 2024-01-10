import gym, gym_2048
import randomagent as ra
import numpy as np

env = gym.make('2048-v0')
env.reset()

done = False

env.render()

while done == False:
    action = ra.rand_action()
    print(action)
    observation, reward, done, info = env.step(action)
    env.render()

    if done:
        observation, reward, done, info = env.step(ra.check_observation(done, observation))
        if ra.c < 4:
            done = False

env.close()