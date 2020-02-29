import numpy as np
from matplotlib import pyplot as plt
#from Ground_Function_File import Ground_Function
"""
This is a simulation of a six wheel rover diluted to a 2D model with inaccurate values.

"""
__author__="David Canosa Ybarra"
def Ground_Function(z):
    if z<2:
        x=0
    else:
        x=0.1*np.sin(z-2)
    return x
alpha_1=np.pi/3
alpha_2=np.pi/3
L_1=0.5
L_3=0.2
L_2=L_1-L_3
k=170*10**3
c=1213
g=9.81
m_wheel=1
mass_of_rover_body=50
rover_body_height=0.2
rover_body_width=0.5
J_body=mass_of_rover_body*(rover_body_height**2+rover_body_width**2)/12
# Initial Conditions
z=0
z_dot=0.5
X=np.mat([[0],
          [0],
          [0]])
X_dot=np.mat([[0],
              [0],
              [0]])
X_dot_dot=np.mat([[0],
                  [0],
                  [0]])
X_base=np.mat([[Ground_Function(z)-L_1*np.cos(alpha_1/2)],
               [np.arcsin(-(Ground_Function(z-L_2*np.sin(alpha_1/2-np.array(X)[1][0])-L_3*np.sin(alpha_1/2-np.array(X)[2][0])))-(Ground_Function(z-L_2*np.sin(alpha_1/2-np.array(X)[1][0])+L_3*np.sin(alpha_1/2-np.array(X)[2][0]))))],
               [np.arcsin(-(Ground_Function(z-L_2*np.sin(alpha_1/2-np.array(X)[1][0])))-(Ground_Function(z+L_1*np.sin(alpha_1/2+np.array(X)[1][0]))))]])
t=0
dt=0.001

K_matrix=np.mat([[-3*k, 2*k*np.sin(alpha_1/2)*L_3, 0],
                 [-k*L_1*np.sin(alpha_1/2)+k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*np.sin(np.array(X)[2][0])))+k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*np.sin(np.array(X)[2][0]))), -k*(L_1*np.sin(alpha_1/2))**2-k*(np.sin(alpha_1/2)*L_2)*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*np.sin(np.array(X)[2][0])))-k*np.sin(alpha_1/2)*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*np.sin(np.array(X)[2][0]))), -2*np.sin(alpha_2/2)*L_3*np.cos(alpha_2/2)*np.sin(np.array(X)[2][0])*L_3],
                 [0, 0, -k*2*(L_3*np.sin(alpha_2/2))**2]])
C_matrix=np.mat([[-3*c, 2*c*np.sin(alpha_1/2)*L_3, 0],
                 [-c*L_1*np.sin(alpha_1/2)+c*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*np.sin(np.array(X)[2][0])))+c*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*np.sin(np.array(X)[2][0]))), -c*(L_1*np.sin(alpha_1/2))**2-c*(np.sin(alpha_1/2)*L_2)*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*np.sin(np.array(X)[2][0])))-c*np.sin(alpha_1/2)*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*np.sin(np.array(X)[2][0]))), -2*np.sin(alpha_2/2)*L_3*np.cos(alpha_2/2)*np.sin(np.array(X)[2][0])*L_3],
                 [0, 0, -c*2*(L_3*np.sin(alpha_2/2))**2]])
B_matrix=-1*np.mat([[-k, -k, -k],
                    [-k*L_1*np.sin(alpha_1/2), k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*np.sin(np.array(X)[2][0]))), k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*np.array(X)[2][0]))],
                    [0, -k*L_3*np.sin(alpha_2/2), k*L_3*np.sin(alpha_2/2)]])
I_matrix=-1*np.mat([[1],
                    [0],
                    [0]])
M_matrix=np.mat([[mass_of_rover_body, 0, 0],
                 [0, m_wheel*(2*L_3**2)+2*m_wheel*L_2**2+m_wheel*L_1**2+J_body, 0],
                 [0, 0, m_wheel*(2*L_3**2)]])
M_matrix_inv=np.linalg.inv(M_matrix)
x_lst=[]
z_lst=[]
x_w_1=[]
z_w_1=[]
x_base_lst=[]
while z<10 and t<20:
    X_dot_dot=M_matrix_inv*(K_matrix*X+C_matrix*X_dot+B_matrix*X_base+mass_of_rover_body*g*I_matrix)
    X_base=np.mat([[Ground_Function(z)],
                   [np.arcsin(-(Ground_Function(z-L_2*np.sin(alpha_1/2-np.array(X)[1][0])-L_3*np.sin(alpha_1/2-np.array(X)[2][0])))-(Ground_Function(z-L_2*np.sin(alpha_1/2-np.array(X)[1][0])+L_3*np.sin(alpha_1/2-np.array(X)[2][0]))))],
                   [np.arcsin(-(Ground_Function(z-L_2*np.sin(alpha_1/2-np.array(X)[1][0])))-(Ground_Function(z+L_1*np.sin(alpha_1/2+np.array(X)[1][0]))))]])
    K_matrix=np.mat([[-3*k, 2*k*np.sin(alpha_1/2)*L_3, 0],
                     [-k*L_1*np.sin(alpha_1/2)+k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*np.sin(np.array(X)[2][0])))+k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*np.sin(np.array(X)[2][0]))), -k*(L_1*np.sin(alpha_1/2))**2-k*(np.sin(alpha_1/2)*L_2)*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*np.sin(np.array(X)[2][0])))-k*np.sin(alpha_1/2)*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*np.sin(np.array(X)[2][0]))), -2*np.sin(alpha_2/2)*L_3*np.cos(alpha_2/2)*np.sin(np.array(X)[2][0])*L_3],
                     [0, 0, -k*2*(L_3*np.sin(alpha_2/2))**2]])
    C_matrix=np.mat([[-3*c, 2*c*np.sin(alpha_1/2)*L_3, 0],
                     [-c*L_1*np.sin(alpha_1/2)+c*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*np.sin(np.array(X)[2][0])))+c*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*np.sin(np.array(X)[2][0]))), -c*(L_1*np.sin(alpha_1/2))**2-c*(np.sin(alpha_1/2)*L_2)*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*np.sin(np.array(X)[2][0])))-c*np.sin(alpha_1/2)*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*np.sin(np.array(X)[2][0]))), -2*np.sin(alpha_2/2)*L_3*np.cos(alpha_2/2)*np.sin(np.array(X)[2][0])*L_3],
                     [0, 0, -c*2*(L_3*np.sin(alpha_2/2))**2]])
    B_matrix=-1*np.mat([[-k, -k, -k],
                        [-k*L_1*np.sin(alpha_1/2), k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*np.sin(np.array(X)[2][0]))), k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*np.array(X)[2][0]))],
                        [0, -k*L_3*np.sin(alpha_2/2), k*L_3*np.sin(alpha_2/2)]])
    z=z+z_dot*dt
    X=X+X_dot*dt
    X_dot=X_dot+X_dot_dot*dt
    x_lst.append(np.array(X)[0][0]+L_1*np.cos(alpha_1/2))
    x_base_lst.append(np.array(X_base)[0][0])
    z_lst.append(z)
    x_w_1.append(np.array(X_base)[0][0]+L_1*np.sin(alpha_1/2)*np.sin(np.array(X_base)[1][0]))
    z_w_1.append(z+np.sin(alpha_1/2)*L_1*np.cos(np.array(X_base)[1][0]))
    t=t+dt

plt.plot(z_lst, x_lst, label="Body")
plt.plot(z_lst, x_base_lst, label="Ground")
plt.plot(z_w_1, x_w_1, label="Wheel_1")
plt.legend()
plt.show()