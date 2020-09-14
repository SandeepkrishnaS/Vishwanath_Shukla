# Written by Sandeepkrishna S (16PH20032)

import numpy as np
import matplotlib.pyplot as plt

def RandomWalk(n):

  time = [0]       #Initial position is at 0 at time 0
  pos = [0] 
  x=0
  t=0
  for i in range(1,n+1):
    step = np.random.uniform(-1,1)  #generates random values for the walker
    if (step <= 0):    
        x += 1  
    else :    
        x += -1

    t+=1
    time.append(t)
    pos.append(x)

  return [time,pos]

RW1 = RandomWalk(5000)
RW2 = RandomWalk(5000)
plt.plot(RW1[0],RW1[1],'r-', label = "Random_Walk_1")
plt.plot(RW2[0],RW2[1],'b-', label = "Random_Walk_2")
plt.title("1-D Random Walks of a drunk person")
plt.xlabel("Time")
plt.ylabel("Displacement")
plt.legend(loc='upper center', bbox_to_anchor=(0.5,-0.1), fancybox=True, shadow=True)
plt.show()
