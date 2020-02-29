import numpy as np
from matplotlib import pyplot as plt
"""
This is a simulation of a four wheel rover diluted to a 2D model with inaccurate values.

"""
__author__="David Canosa Ybarra"



wheel_stiffness=1*10**3                                                             #[N/m]
wheel_mass=1                                                                        #[kg]
mass_of_rover_body=50                                                               #[kg]
rover_body_height=0.2                                                               #[m]
rover_body_width=0.5                                                                #[m]
I_rover_body=mass_of_rover_body*(rover_body_height**2
+rover_body_width**2)/12                                                            #[m^3]
arm_length=0.5                                                                      #[m]
I_drive_train=2*wheel_mass*arm_length**2                                            #[m^3]
joint_angle=np.pi/3                                                                 #[rad]
wheel_distance=2*arm_length*np.sin(joint_angle/2)                                   #[m]
I_rover=I_rover_body+I_drive_train                                                  #[m^3]
mass_total=mass_of_rover_body+2*wheel_mass                                          #[kg]
mass_matrix=np.mat([[mass_total,0],[0,I_rover]])                                    #[kg]
stiffness_matrix=np.mat([[-2*wheel_stiffness,0],[0,-2\
*wheel_stiffness*(arm_length**2)*(np.sin(joint_angle/2))**2]])                      #[N/m]
base_stiffness=np.mat([[wheel_stiffness, wheel_stiffness\
],[-wheel_stiffness*arm_length*np.sin(joint_angle/2),\
wheel_stiffness*arm_length*np.sin(joint_angle/2)]])                                 #[N/m]
velocity_max=0.5                                                                    #[m/s]
dampning_coefficient=0
dampning_matrix=dampning_coefficient*np.mat([[-1, 0], [0, -1]])
x=np.mat([[0],[0]])
x_dot=np.mat([[0],[0]])
x_dot_dot=np.mat([[0],[0]])
inv_mass=np.linalg.inv(mass_matrix)
# Time start - Time step
t=0
dt=0.001
# Empty lists for plotting
x_tab=[]
t_tab=[]



# ground definition
def ground_function(t):
    x=0.1*np.sin(1*t)
    return x

def ground_wheel(t, num, spacing, ground_function, velocity_max):
    if num==1:
        return ground_function(t)
    elif num==2:
        return np.arcsin((ground_function(t+spacing/velocity_max)-ground_function(t))/spacing)





while t<10:
    base_function=np.mat([[ground_wheel(t, 1, 2*np.sin(joint_angle/2), ground_function, velocity_max)], [ground_wheel(t, 2, 2*np.sin(joint_angle/2), ground_function, velocity_max)]])
    x_dot_dot=inv_mass*(stiffness_matrix*(x-base_function)+dampning_matrix*x_dot)
    x_dot=x_dot+x_dot_dot*dt
    x=x+x_dot*dt
    x_tab.append(float(x[0][0]))
    t_tab.append(t)
    loading=(t/20)*100
    print(str(round(loading))+"% done")
    t=t+dt

# Plot results for verification
t_lin=np.linspace(0,10,101)
ground_height=ground_wheel(t_lin, 1, 2*np.sin(joint_angle/2), ground_function, velocity_max)
plt.plot(t_lin, ground_height, "r", label="Ground Height")
plt.plot(t_tab, x_tab, "g--", label="Vehicle Response")
plt.legend()
plt.show()
