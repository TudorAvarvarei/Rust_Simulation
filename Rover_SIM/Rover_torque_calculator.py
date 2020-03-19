
"""
This program will take the angle required to traverse and the tire friction coefficient and give a power required and a
torque required from the motor

"""
__author__="David Canosa Ybarra" \
           "Student Number: 4839277" \
           "Email: dcanosaybarra@gmail.com"
from math import atan, sin, pi
friction_coefficient = 0.5
mass_rover = 60
gravitational_acceleration = 9.81
wheel_radius = 0.1
rover_velocity = 0.5
max_hill_angle = atan(friction_coefficient)
force_required = mass_rover*gravitational_acceleration*sin(max_hill_angle)

torque_required = force_required*wheel_radius
power_required = force_required*rover_velocity
print("Torque: "+str(torque_required)+"\n"+
      "Power: "+str(power_required)+"\n"+
      "Torque 1 motor (ONE ENGINE FAILURE): "+str(torque_required/5)+"\n"+
      "Power 1 motor (ONE ENGINE FAILURE): "+str(power_required/5))

