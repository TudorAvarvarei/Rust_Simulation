from math import *
from matplotlib import pyplot as plt
from random import *
import numpy as np
lst=[]

n=6
array=np.zeros(n*6)
x=range(1, n*6+1)
for j in range(100000):
    a=0
    for i in range(n):
        a=a+randint(1,6)

        
    array[a-1]=array[a-1]+1


print(len(array))
plt.plot(x,array)
plt.show()

    
