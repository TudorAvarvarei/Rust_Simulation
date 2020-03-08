from math import *
from matplotlib import pyplot as plt
from random import *
import numpy as np
lst=[]

n=256
array=np.zeros(n*6)
x=range(1, n*6+1)
amount_of_tries=1000000
for j in range(amount_of_tries):
    a=0
    print(str((j/amount_of_tries)*100)+" % Done")
    for i in range(n):
        a=a+randint(1,6)

        
    array[a-1]=array[a-1]+1


plt.axis([750, 1000, 0, 0.015])
plt.plot(x,array/amount_of_tries)
plt.show()

