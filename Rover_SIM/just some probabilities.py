from math import *
from matplotlib import pyplot as plt
from random import *
import numpy as np
lst=[]
n=6
for j in range(100000):
    a=0
    for i in range(n):
        a=a+randint(1,6)
        
    lst.append(a)
lst.sort()
tab=[0]*(6*n*n) #<-
for k in range(len(lst)):
    #print(lst[k])
    tab[lst[k]]=tab[lst[k]]+1

array=np.array(tab)
array=np.trim_zeros(array)
x=[]
for q in range(n,6*n+1):
    x.append(q)
print(len(x))
print(len(array))
plt.plot(x,array)
plt.show()

    
