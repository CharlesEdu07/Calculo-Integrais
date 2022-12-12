import matplotlib.pyplot as plt
import numpy as np
import cmath as cm
import os

from math import *

x_values = [9, 10, 11, 12, 13, 14, 15, 16]
y_values = [75.3, 77.0, 83.2, 84.8, 86.5, 86.4, 81.1, 78.6]

def f(x):
    f = np.interp(x, x_values, y_values)

    return f

def plot_func_graphic():
    plt.plot(x_values, y_values, color='purple', label='Function')

    conv_x = np.array(x_values, dtype=float)
    conv_y = np.array(y_values, dtype=float)
    
    plt.fill_between(conv_x, conv_y, color='purple', alpha=0.2)

    plt.grid(True)
    plt.show()

def trap_integration(a, b, trapezoids):
    accumulator = 0

    a = float(a)
    b = float(b)
    trapezoids = float(trapezoids)

    i = (b - a) / trapezoids

    x0 = a
    x1 = a + i

    while (a <= x1 <= b) or (a >= x1 >= b):
        area = (f(x0) + f(x1)) * i/2
        accumulator += area

        x1 += i
        x0 += i

    return accumulator

a = min(x_values)
b = max(x_values)

plot_func_graphic()

integration = trap_integration(a, b, 1000)

os.system('cls')

print("Temperatura media:", integration / len(x_values), "° F")