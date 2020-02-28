import numpy as np
from matplotlib import pyplot as plt
"""
This is a simulation of a six wheel rover diluted to a 2D model with inaccurate values.

"""
__author__="David Canosa Ybarra"

alpha_1=np.pi/3
alpha_2=np.pi/3
L_1=0.5
L_3=0.2
L_2=L_1-L_3
k=1*10**3

K_matrix=np.mat([[-3*k, 2*k*np.sin(alpha_1/2)*L_3, 0], \
                 [-k*L_1*np.sin(alpha_1/2)+\
                  k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*theta_2))+\
                  k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*theta_2)), \
                  -k*(np.sin(alpha_1)*L_2*((L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*theta_2))+(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*theta_2)))), \
                  0], \
                 [,,]])