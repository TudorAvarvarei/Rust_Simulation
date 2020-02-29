import numpy as np
import pygame as pg
import time
def Ground_Function(z):
    x=0.5*np.sin(z)
    return x
alpha_1=np.pi/2
alpha_2=np.pi/2
L_1=0.5
L_3=0.2
L_2=L_1-L_3
k=1*10**3
c=40
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
               [np.arcsin(-(Ground_Function(z-L_2*np.sin(alpha_1/2-np.array(X)[1][0])-L_3*np.sin(alpha_1/2-np.array(X)[2][0])))-(Ground_Function(z-L_2*np.sin(alpha_1/2-np.array(X)[1][0])+L_3*np.sin(alpha_1/2-np.array(X)[2][0]))))],
               [np.arcsin(-(Ground_Function(z-L_2*np.sin(alpha_1/2-np.array(X)[1][0])))-(Ground_Function(z+L_1*np.sin(alpha_1/2+np.array(X)[1][0]))))]])
t=0
dt=0.001

K_matrix=np.mat([[-3*k, 2*k*np.sin(alpha_1/2)*L_3, 0],
                 [-k*L_1*np.sin(alpha_1/2)+k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*np.array(X)[2][0]))+k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*np.array(X)[2][0])), -k*(L_1*np.sin(alpha_1/2))**2-k*(np.sin(alpha_1/2)*L_2)*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*np.array(X)[2][0]))-k*np.sin(alpha_1/2)*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*np.array(X)[2][0])), -2*np.sin(alpha_2/2)*L_3*np.cos(alpha_2/2)*np.array(X)[2][0]*L_3],
                 [0, 0, -k*2*(L_3*np.sin(alpha_2/2))**2]])
C_matrix=np.mat([[-3*c, 2*c*np.sin(alpha_1/2)*L_3, 0],
                 [-c*L_1*np.sin(alpha_1/2)+c*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*np.array(X)[2][0]))+c*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*np.array(X)[2][0])), -c*(L_1*np.sin(alpha_1/2))**2-c*(np.sin(alpha_1/2)*L_2)*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*np.array(X)[2][0]))-c*np.sin(alpha_1/2)*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*np.array(X)[2][0])), -2*np.sin(alpha_2/2)*L_3*np.cos(alpha_2/2)*np.array(X)[2][0]*L_3],
                 [0, 0, -c*2*(L_3*np.sin(alpha_2/2))**2]])
B_matrix=-1*np.mat([[-k, -k, -k],
                    [-k*L_1*np.sin(alpha_1/2), k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*np.array(X)[2][0])), k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*np.array(X)[2][0]))],
                    [0, -k*L_3*np.sin(alpha_2/2), k*L_3*np.sin(alpha_2/2)]])
I_matrix=-1*np.mat([[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]])
M_matrix=np.mat([[mass_of_rover_body, 0, 0],
                 [0, m_wheel*(2*L_3**2)+2*m_wheel*L_2**2+m_wheel*L_1**2+J_body, 0],
                 [0, 0, m_wheel*(2*L_3**2)]])
M_matrix_inv=np.linalg.inv(M_matrix)
x_lst=[]
z_lst=[]
x_base_lst=[]
while z<10 and t<100:
    X_dot_dot=M_matrix_inv*(K_matrix*X+C_matrix*X_dot+B_matrix*X_base+0*g*I_matrix)
    X_base=np.mat([[Ground_Function(z)],
                   [np.arcsin(-(Ground_Function(z-L_2*np.sin(alpha_1/2-np.array(X)[1][0])-L_3*np.sin(alpha_1/2-np.array(X)[2][0])))-(Ground_Function(z-L_2*np.sin(alpha_1/2-np.array(X)[1][0])+L_3*np.sin(alpha_1/2-np.array(X)[2][0]))))],
                   [np.arcsin(-(Ground_Function(z-L_2*np.sin(alpha_1/2-np.array(X)[1][0])))-(Ground_Function(z+L_1*np.sin(alpha_1/2+np.array(X)[1][0]))))]])
    K_matrix=np.mat([[-3*k, 2*k*np.sin(alpha_1/2)*L_3, 0],
                     [-k*L_1*np.sin(alpha_1/2)+k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*np.array(X)[2][0]))+k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*np.array(X)[2][0])), -k*(L_1*np.sin(alpha_1/2))**2-k*(np.sin(alpha_1/2)*L_2)*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*np.array(X)[2][0]))-k*np.sin(alpha_1/2)*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*np.array(X)[2][0])), -2*np.sin(alpha_2/2)*L_3*np.cos(alpha_2/2)*np.array(X)[2][0]*L_3],
                     [0, 0, -k*2*(L_3*np.sin(alpha_2/2))**2]])
    C_matrix=np.mat([[-3*c, 2*c*np.sin(alpha_1/2)*L_3, 0],
                     [-c*L_1*np.sin(alpha_1/2)+c*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*np.array(X)[2][0]))+c*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*np.array(X)[2][0])), -c*(L_1*np.sin(alpha_1/2))**2-c*(np.sin(alpha_1/2)*L_2)*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*np.array(X)[2][0]))-c*np.sin(alpha_1/2)*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*np.array(X)[2][0])), -2*np.sin(alpha_2/2)*L_3*np.cos(alpha_2/2)*np.array(X)[2][0]*L_3],
                     [0, 0, -c*2*(L_3*np.sin(alpha_2/2))**2]])
    B_matrix=-1*np.mat([[-k, -k, -k],
                        [-k*L_1*np.sin(alpha_1/2), k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)+np.cos(alpha_2/2)*np.array(X)[2][0])), k*(L_2*np.sin(alpha_1/2)-L_3*(np.sin(alpha_2/2)-np.cos(alpha_2/2)*np.array(X)[2][0]))],
                        [0, -k*L_3*np.sin(alpha_2/2), k*L_3*np.sin(alpha_2/2)]])
    z=z+z_dot*dt
    X=X+X_dot*dt
    X_dot=X_dot+X_dot_dot*dt
    x_lst.append(np.array(X))
    x_base_lst.append(np.array(X_base)[0][0])
    z_lst.append(z)
    t=t+dt







#Starting pygame
pg.init()
#Setting resoloution
reso=(800,500)
screen=pg.display.set_mode(reso)
#Start condition running
running=True
#Colours
blue=(50,200,255)
grey=(100,100,100)
black=(0, 0, 0)
#Finishing time and starting times
seconds_end=50
time_elapsed=0
t_lst=[0]
next_dt=False

def draw_rover(x, theta_1, theta_2, screen=screen, reso=reso, black=black, width=25, height=10, thickness=2, L_1=100*L_1, L_2=100*L_2, L_3=100*L_3):
    center=np.array([reso[0]/2, reso[1]/2])
    top_right=np.array([+width, -height])
    bottom_right=np.array([+width, +height])
    top_left=np.array([-width, -height])
    bottom_left=np.array([-width, +height])
    joint=np.array([-L_2*np.sin(alpha_1/2), +L_2*np.cos(alpha_1/2)])
    w_1=np.array([L_1*np.sin(alpha_1/2), L_1*np.cos(alpha_1/2)])
    w_2=np.array([-L_2*np.sin(alpha_1/2)-L_3*np.sin(alpha_2/2), +L_2*np.cos(alpha_1/2)+L_3*np.cos(alpha_2/2)])
    w_3=np.array([-L_2*np.sin(alpha_1/2)+L_3*np.sin(alpha_2/2), +L_2*np.cos(alpha_1/2)+L_3*np.cos(alpha_2/2)])
    rotation_matrix=np.mat([[np.cos(theta_1), -np.sin(theta_1)], [np.sin(theta_1), np.cos(theta_1)]])
    rotation_matrix_lower=np.mat([[np.cos(theta_2), -np.sin(theta_2)], [np.sin(theta_2), np.cos(theta_2)]])
    top_right=np.transpose(np.array(rotation_matrix*np.transpose(np.mat(top_right))))
    top_left=np.transpose(np.array(rotation_matrix*np.transpose(np.mat(top_left))))
    bottom_left=np.transpose(np.array(rotation_matrix*np.transpose(np.mat(bottom_left))))
    bottom_right=np.transpose(np.array(rotation_matrix*np.transpose(np.mat(bottom_right))))
    joint=np.transpose(np.array(rotation_matrix*np.transpose(np.mat(joint))))
    w_1=np.transpose(np.array(rotation_matrix*np.transpose(np.mat(w_1))))
    w_2=np.transpose(np.array(rotation_matrix_lower*rotation_matrix*np.transpose(np.mat(w_2))))
    w_3=np.transpose(np.array(rotation_matrix_lower*rotation_matrix*np.transpose(np.mat(w_3))))
    x_to_add=np.array([0, -x])
    top_right=top_right[0]+center+x_to_add
    top_left=top_left[0]+center+x_to_add
    bottom_right=bottom_right[0]+center+x_to_add
    bottom_left=bottom_left[0]+center+x_to_add
    joint=joint[0]+center+x_to_add
    w_1=w_1[0]+center+x_to_add
    w_2=w_2[0]+center+x_to_add
    w_3=w_3[0]+center+x_to_add
    pg.draw.line(screen,black,top_right,bottom_right,thickness)
    pg.draw.line(screen,black,top_right,top_left,thickness)
    pg.draw.line(screen,black,bottom_left,bottom_right,thickness)
    pg.draw.line(screen,black,bottom_left,top_left,thickness)
    pg.draw.line(screen,black,center,joint,thickness)
    pg.draw.line(screen,black,center,w_1,thickness)
    pg.draw.line(screen,black,w_2,joint,thickness)
    pg.draw.line(screen,black,w_3,joint,thickness)
counter=0



while time_elapsed>=0 and time_elapsed<=seconds_end and running:
    pg.event.pump()
    keys=pg.key.get_pressed()

    time_elapsed=time.perf_counter()
    t=(time_elapsed//dt)*dt
    t_lst.append(t)
    #Test if time changes
    if t_lst[-1]!=t_lst[-2] or len(t_lst)==2:
        next_dt=True
        counter=counter+1


    while running and next_dt:


        screen.fill(blue)
        draw_rover(x_lst[counter][0][0], x_lst[counter][0][1], x_lst[counter][0][2])
        #Flip screen
        pg.display.flip()
        next_dt=False
        #Setting escape to quit
        if keys[pg.K_ESCAPE]:
            running=False
        #Making the cross close window
        for event in pg.event.get():



            if event.type==pg.QUIT:
                print("Quit event")
                running=False

#Stopping pygame after the simulation
pg.quit()
