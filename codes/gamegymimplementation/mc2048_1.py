import gym, gym_2048
import numpy as np

env = gym.make('2048-v0')

#Since it is always important to look at the observation and action space
print(f'observation space: {env.observation_space}')
print(f'action space : {env.action_space}')

for game_num in range(10):
    print(f'Start Game : {game_num}')
    state = env.reset()

    for i in range(10):
        #The agent taking all random actions for all games
        env.render()
        action = env.action_space.sample()
        state, reward, done, info = env.step(action)
        print(f'reward : {reward}')

        if done:
            print(f'Game done : {game_num}')
            break

'''So the 2 loops here represent the following
The game_num loop represents the game we are playing
The i loop represents the number of steps we are taking in a game.

The reward from the game is the sum of all the combinations done for the action taken
The state we recieve contains all the 16 values from the grid. 

One condition to improve the game can be to make the agent try to achieve the score >= 16 if 8 is the max number in the grid and repeat the same by making 16 as the max number and achieving 32.'''
