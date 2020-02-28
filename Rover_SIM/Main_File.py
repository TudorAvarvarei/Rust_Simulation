import numpy as np
#wheel ranging from 1 to 3 when the small joint is on the left side and they are numbered from left to right making wheel 3 the front wheel
mass_of_wheels=np.array([1,1,1])

mass_of_rover_body=50
rover_body_height=0.2
rover_body_width=0.5
#the arm of the smallest joint
arm_1=0.2
#the arm of the largest joint
arm_2=0.5

arm_lengths=np.array([arm_1,arm_2,arm_2-arm_1])
#mass moments of inertia
I_rover_body=mass_of_rover_body*(rover_body_height**2+rover_body_width**2)/12
I_small_joint=mass_of_wheels[0]*arm_lengths[0]**2+mass_of_wheels[1]*arm_lengths[1]**2
I_large_joint=I_small_joint*arm_lengths[3]**2+mass_of_wheels[2]*arm_lengths[2]**2

small_joint_angle=np.pi/3
small_joint_angle=np.pi/3

