# first intro post script
# how to display the sinusiodal voltage

# importing the required libraries
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, sin, pi

# time vector
t = np.linspace(0, 0.1, 100)

# rms value of the voltage
U = 230

# frequency
f = 50

# Voltage wave

u = [sqrt(2)*U*sin(2*pi*f*k) for k in t]

# plotting the voltage
%matplotlib inline
plt.plot(t, u);
