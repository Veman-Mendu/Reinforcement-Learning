import abc
import numpy as np
import gym

"""The below Agent class represents how the continuous and Discrete agents should be.
The pi class represents the policy of the agent"""

class Agent:
    def __init__(self, action_space: gym.spaces.Space):
        raise NotImplementedError("This class cannot be instantiated")
    
    @abc.abstractmethod
    def pi(self, state: np.ndarray) -> np.ndarray:
        pass

"""The below class is for a continuous agent.
in the init function we perform the check if the environment is Box space or not
If the agent is in correct space based on the dimensions of the space we define differnet policies
we call these policies in the pi function"""

class ContinuousAgent(Agent):
    def __init__(self, action_space: gym.spaces.Space, seed=46):
        np.random.seed(seed)

        if not isinstance(action_space, gym.spaces.Box):
            raise ValueError("This is a continuous agent pass as input a Box Space")
        
        if(action_space.low == -np.inf) and (action_space.high == np.inf):
            self._pi = lambda: np.random.normal(loc=0, scale=1, size=action_space.shape)

            return
        
        if(action_space.low != -np.inf) and (action_space.high != np.inf):
            self._pi = lambda: np.random.uniform(low=action_space.low, high=action_space.high, size=action_space.shape)
            return
        
        if(action_space.low == -np.inf):
            self._pi = (lambda: -np.random.exponential(size=action_space.shape)+action_space.high)
            return
        
        if(action_space.high == np.inf):
            self._pi = (lambda: np.random.exponential(size=action_space.shape))
            return
        
    def pi(self, observation: np.ndarray) -> np.ndarray:
        return self._pi()

"""The below is the Discrete Agent class. Same as Continuous agent"""

class DiscreteAgent(Agent):
    def __init__(self, action_space: gym.spaces.Space, seed=46):
        np.random.seed(seed)

        if not isinstance(action_space, gym.spaces.Discrete):
            raise ValueError("THis is a Discrete Agent Pass as input a Discrete Space")
        
        self._pi = lambda: np.random.randint(low=0, high=action_space.n)

    def pi(self, state: np.ndarray) -> np.ndarray:
        return self._pi()
    
"""The below function helps in making agents based on the environment space"""

def make_agent(action_space: gym.spaces.Space, seed=46):
    if isinstance(action_space, gym.spaces.Discrete):
        return DiscreteAgent(action_space, seed)
    
    if isinstance(action_space, gym.spaces.Box):
        return ContinuousAgent(action_space, seed)
    
    raise ValueError("Only Box space and Discrete Space are allowed")