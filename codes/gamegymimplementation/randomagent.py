import numpy as np
import random

c = 0

def rand_action():
    act = random.choice([0,1,2,3])
    print(f"act from ra : {act}")
    return act

def check_observation(done,observation):
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
                    return 1
                elif (i+1<=3) and (ren[i][j] == ren[i+1][j]):
                    return 2
            else:
                count = -1
                while count<4:
                    if count<4 and done:
                        count = count + 1
                        c = count
                        return count
                    else:
                        c = count
                        return count