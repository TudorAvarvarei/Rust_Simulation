from math import *
from matplotlib import pyplot as plt
from random import *
import numpy as np
lst=[]

n=150
array=np.zeros(n*6)
#x=range(n, n*6+1)
x=range(1, n*6+1)
amount_of_tries=100000
for j in range(amount_of_tries):
    a=0
    print(str((j/amount_of_tries)*100)+" % Done")
    for i in range(n):
        a=a+randint(1,6)

        
    array[a-1]=array[a-1]+1
#array=np.trim_zeros(array)
axis=[]
for number in range(n,n*6+1):
    axis.append(number)
    
#plt.axis([n-5, n*6+5, 0, 0.015])
#plt.ylim(0, max(array/amount_of_tries)*1.5)
#plt.plot(x,array/amount_of_tries)
#plt.show()

print(axis)
print(x)
print(len(x))
print(array)
print(len(array))
plt.bar(x,array/amount_of_tries, align='center',alpha=0.5)
#plt.xticks(x,axis)
plt.xlim(n,n*6+1)
plt.show()

