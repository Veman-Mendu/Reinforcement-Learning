import gym, gym_2048
import random
import numpy as np

def check_observation(done, observation):
    ren = np.zeros((4,4))
    for i in range(4):
        for j in range(4):
            row = observation[i][j]
            for k in range(10):
                if row[k] == 1:
                    ren[i][j] = 2**(k+1)

    print(f"{ren}")
    for i in range(4):
        for j in range(4):
            if ren[i][j] !=0:
                if (j+1<=3) and (ren[i][j] == ren[i][j+1]):
                    observation, reward, done, info = env.step(1)
                    return done
                elif (i+1<=3) and (ren[i][j] == ren[i+1][j]):
                    observation, reward, done, info = env.step(2)
                    return done
            else:
                count = 0
                while count<4:
                    observation, reward, done, info = env.step(count)
                    if done:
                        count = count+1
                    else:
                        return done
    return done


env = gym.make('2048-v0')

env.reset()

done = False

print(env.action_space)
env.render()
while done==False:

    action = random.choice([0,1,2,3])
    print(action)
    observation, reward, done, info = env.step(action)
    env.render()
    #print(f'observation : {observation}')
    #print(f'1st row of observations : {observation[0][0]}')
    if done:
        done = check_observation(done, observation)
        

env.close()

