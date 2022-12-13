#!/usr/bin/env python3
"""
Program: .py
Programmer: Aamir Alaud Din, PhD
Date: 2022.11.13

"""

import math as m
import matplotlib.pyplot as plt

# Enthalpy

mass = 2.0 # kg
sp_heat = 4.2 # kJ/kg-C
temp_i = 20.0 # C
temp_f = 25.0 # C

enthalpy = mass*sp_heat*(temp_f - temp_i)
print("Enthalpy = {0:.2f} kJ".format(enthalpy))

# Mass to energy conversion

mass = 1.0 # g
light_speed = 3.0E+8 # m/s
energy = mass*light_speed**2
print("Energy = {0:.2E} J".format(energy))


# Bond length

oxygen_1 = [2.0021, -3.6211, 1.2325]
oxygen_2 = [2.5101, -4.0280, 0.1987]
bond_length = m.sqrt((oxygen_1[0] - oxygen_2[0])**2 + (oxygen_1[1] - oxygen_2[1])**2 + (oxygen_1[2] - oxygen_2[2])**2)
print("The O-O bond length is {0:.4f} angstrom".format(bond_length))


# Wave Equation

amplitude = 1.50 # m
theta = []
wave = []
angle = 0.00
while angle <= 2*m.pi:
	wave.append(amplitude*m.sin(angle))
	theta.append(angle)
	angle += 0.005

plt.figure(figsize=(10, 6))
plt.plot(theta, wave, '-k', linewidth=3)
plt.plot([min(theta) - 0.2, max(theta) + 0.2], [0.0, 0.0], '-b')
plt.plot([0.0, 0.0], [min(wave) - 0.2, max(wave) + 0.2], '-b')
plt.xlim([min(theta) - 0.2, max(theta) + 0.2])
plt.ylim([min(wave) - 0.2, max(wave) + 0.2])
plt.xlabel("Angle (radians)", fontsize=12, weight='bold')
plt.ylabel("Height (m)", fontsize=12, weight='bold')
plt.title("Plot of sine wave", fontsize=16, weight='bold')
plt.xticks(fontsize=12, weight='bold')
plt.yticks(fontsize=12, weight='bold')
plt.grid()
plt.show()
