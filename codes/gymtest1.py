import gym

env = gym.make('CartPole-v1')

"""Analyze the action space"""
print(f"Action Space: {env.action_space}")
"""The above print command gives output as 'Discrete(2). This means that there are 2 actions in the action space they are: GoLeft and GoRight.'"""

"""Analyze the Observation Space"""
print(f"Observation Space: {env.observation_space}")
"""The above print commands gives output as 'Box([low1, low2, low3, low4], [up1, up2, up3, up4], (4,), flaot32).'
This means that the observation space is a 4 Dimension space and all the low values represent the lower boundary of the space and all the up values represent the upper boudnaries of the space.
The first value in 4D array represents the Cart Position
Second value represents the Velocity of the cart
Third value represents pole angle between -0.4 radians and +0.4 radians
Fourth value represents pole angluar velocity."""

"""Below is the code for creating spaces and samples"""
from typing import Tuple
from gym import spaces

n: int = 5
discrete_space = spaces.Discrete(n=n)
print(f"Discrete Sample Space: {discrete_space.sample()}")
"""The above line gives output 'a integer'. Here the discrete_space.sample() method gives a random sample from the range [0,1,2,3,4] since we had the range to n=5"""

box_shape: Tuple[int,int] = (4,4)
box_space = spaces.Box(low=0, high=1, shape=box_shape)
print(f"Box Sample Space: {box_space.sample()}")
"""The output for the above line is a 4x4 matrix with values between defined lows and highs"""

"""The sample method gives a random example for each instance. In order to have a repetative sample every time. We can use seed() method"""
discrete_space.seed(0)
box_space.seed(0)
print(f"Discrete Sample Space with seed=0: {discrete_space.sample()}")
print(f"Box Sample Space with seed=0: {box_space.sample()}")

