import numpy as np
from matplotlib import pyplot as plt
#from Ground_Function_File import Ground_Function
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
g=9.81
m_wheel=1
# Initial Conditions
X=np.mat([[0],
          [0],
          [0]])
X_dot=np.mat([[0],
              [0],
              [0]])
X_dot_dot=np.mat([[0],
                  [0],
                  [0]])

K_matrix=np.mat([[-3*k, 2*k*np.sin(alpha_1/2)*L_3, 0],
                 [-k*L_1*np.sin(alpha_1/2)+k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*X[0][2]))+k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*X[0][2])), -k*(L_1*np.sin(alpha_1/2))**2-k*(np.sin(alpha_1/2)*L_2)*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*X[0][2]))-k*np.sin(alpha_1/2)*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*X[0][2])), -2*np.sin(alpha_2/2)*L_3*np.cos(alpha_2/2)*X[0][2]*L_3],
                 [0, 0, -k*2*(L_3*np.sin(alpha_2/2))**2]])
B_matrix=-1*np.mat([[-k, -k, -k],
                    [-k*L_1*np.sin(alpha_1/2), k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*X[0][2])), k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*X[0][2]))],
                    [0, -k*L_3*np.sin(alpha_2/2), k*L_3*np.sin(alpha_2/2)]])
I_matrix=-1*np.mat([[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]])
M_matrix=np.mat()