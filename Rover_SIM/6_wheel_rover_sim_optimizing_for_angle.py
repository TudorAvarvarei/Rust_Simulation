import numpy as np
from matplotlib import pyplot as plt
import time
from operator import itemgetter
#from Ground_Function_File import Ground_Function
"""
This is a simulation of a six wheel rover diluted to a 2D model with inaccurate values.

"""
__author__="David Canosa Ybarra" \
           "Student Number: 4839277" \
           "Email: dcanosaybarra@gmail.com"
start_time = time.time()
cg_height=0.5
angles=np.linspace(np.pi/3,(np.pi*7/9),17)
small_bump_size=0.05
big_bump_size=0.5
F_on_wheels_max=[]
for alpha_1 in angles:
    for alpha_2 in angles:
        def Ground_Function(z):
            if z<2:
                x=0
            elif z>=2:
                x=0.05*(np.cos(5*(z-2))-1)+0.5*(np.cos((z-2))-1)
            else:
                pass
            return x

        L_1=cg_height/np.cos(alpha_1/2)
        lengths_L_3=np.linspace(0.3, L_1-0.3, 3)
        for L_3 in lengths_L_3:
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
            X_base=np.mat([[Ground_Function(z)],
                           [Ground_Function(z-L_1*np.sin(alpha_1/2))],
                           [Ground_Function(z-L_1*np.sin(alpha_1/2)-2*L_3*np.sin(alpha_2/2))]])
            t=0
            dt=0.001

            K_matrix=np.mat([[-3*k, 2*k*L_2*np.sin(alpha_1/2)-k*L_1*np.sin(alpha_1/2), 0],
                             [2*k*L_2*np.sin(alpha_1/2)-k*L_1*np.sin(alpha_1/2), -k*(L_1*np.sin(alpha_1/2))**2-2*k*(L_2*np.sin(alpha_2/2))**2, 0],
                             [0, 0, -k*2*(L_3*np.sin(alpha_2/2))**2]])
            C_matrix=np.mat([[-3*c, 2*c*L_2*np.sin(alpha_1/2)-c*L_1*np.sin(alpha_1/2), 0],
                             [2*c*L_2*np.sin(alpha_1/2)-c*L_1*np.sin(alpha_1/2), -c*(L_1*np.sin(alpha_1/2))**2-2*c*(L_2*np.sin(alpha_2/2))**2, 0],
                             [0, 0, -c*2*(L_3*np.sin(alpha_2/2))**2]])
            B_matrix=np.mat([[k, k, k],
                             [k*L_1*np.sin(alpha_1/2), -k*L_2*np.sin(alpha_1/2), -k*L_2*np.sin(alpha_1/2)],
                             [0, k*L_3*np.sin(alpha_2/2), -k*L_3*np.sin(alpha_2/2)]])
            M_matrix=np.mat([[mass_of_rover_body, 0, 0],
                             [0, m_wheel*(2*L_3**2)+2*m_wheel*L_2**2+m_wheel*L_1**2+J_body, 0],
                             [0, 0, m_wheel*(2*L_3**2)]])
            M_matrix_inv=np.linalg.inv(M_matrix)
            x_lst=[]
            z_lst=[]
            x_base_lst=[]
            x_dot_dot=[]
            t_lst=[]
            x_lst.append(np.array(X)[0][0]+L_1*np.cos(alpha_1/2))
            x_base_lst.append(np.array(X_base)[0][0])
            z_lst.append(z)
            t_lst.append(t)
            F_on_wheels_1=[]
            F_on_wheels_2=[]
            F_on_wheels_3=[]
            x_dot_dot.append(np.array(X_dot_dot)[0][0])
            F_on_wheels_1.append(k*(np.array(X)[0][0]-np.array(X_base)[0][0]+np.array(X)[1][0]*L_1*np.sin(alpha_1/2))-(mass_of_rover_body+3*m_wheel)*g/3)
            F_on_wheels_2.append(k*(np.array(X)[0][0]-np.array(X_base)[1][0]-np.array(X)[1][0]*L_2*np.sin(alpha_1/2)+np.array(X)[2][0]*L_3*np.sin(alpha_2/2))-(mass_of_rover_body+3*m_wheel)*g/3)
            F_on_wheels_3.append(k*(np.array(X)[0][0]-np.array(X_base)[2][0]-np.array(X)[1][0]*L_2*np.sin(alpha_1/2)-np.array(X)[2][0]*L_3*np.sin(alpha_2/2))-(mass_of_rover_body+3*m_wheel)*g/3)
            count=0
            while z<10:
                X_dot_dot=M_matrix_inv*(K_matrix*X+C_matrix*X_dot+B_matrix*X_base)


                z=z+z_dot*dt
                X_base=np.mat([[Ground_Function(z+L_1*np.sin(alpha_1/2))],
                               [Ground_Function(z)],
                               [Ground_Function(z+2*L_3*np.sin(alpha_2/2))]])

                # Finding forces on arms
                F_on_wheels_1.append(k*(np.array(X)[0][0]-np.array(X_base)[0][0]+np.array(X)[1][0]*L_1*np.sin(alpha_1/2))-(mass_of_rover_body+3*m_wheel)*g/3)
                F_on_wheels_2.append(k*(np.array(X)[0][0]-np.array(X_base)[1][0]-np.array(X)[1][0]*L_2*np.sin(alpha_1/2)+np.array(X)[2][0]*L_3*np.sin(alpha_2/2))-(mass_of_rover_body+3*m_wheel)*g/3)
                F_on_wheels_3.append(k*(np.array(X)[0][0]-np.array(X_base)[2][0]-np.array(X)[1][0]*L_2*np.sin(alpha_1/2)-np.array(X)[2][0]*L_3*np.sin(alpha_2/2))-(mass_of_rover_body+3*m_wheel)*g/3)
                X=X+X_dot*dt
                X_dot=X_dot+X_dot_dot*dt
                x_lst.append(np.array(X)[0][0]+L_1*np.cos(alpha_1/2))
                x_base_lst.append(np.array(X_base)[0][0])
                z_lst.append(z)
                t_lst.append(t)
                x_dot_dot.append(np.array(X_dot_dot)[0][0])
                count=count+1
                t=t+dt
            F_on_wheels_max.append([max([max((np.array(F_on_wheels_1)**2)**0.5), max((np.array(F_on_wheels_2)**2)**0.5), max((np.array(F_on_wheels_3)**2)**0.5)]), str(alpha_1/np.pi)+" Pi", str(alpha_2/np.pi)+" Pi", L_1, L_2, L_3])



    print("ONE SET OF ALPHA_2 DONE "+str((time.time() - start_time)))
Final=sorted(F_on_wheels_max, key = itemgetter(0))
print("Maximum compressive force: "+str(Final[0][0])+"\n"+
      "Angle on the bigger joint: "+str(Final[0][1])+"\n"+
      "Angle on the secondary joint: "+str(Final[0][2])+"\n"+
      "Length of arm 1: "+str(Final[0][3])+"\n"+
      "Length of arm 2: "+str(Final[0][4])+"\n"+
      "Length of arm 3: "+str(Final[0][5]))




