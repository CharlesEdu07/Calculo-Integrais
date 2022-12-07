import matplotlib.pyplot as plt
import numpy as np
import cmath as cm
import os

from math import *

x_values = []
y_values = []

def f(x):
    return x / (sqrt(x**2 + 9))

def func_generate(a, b):
    a = float(a)
    b = float(b)

    for i in np.arange(a, b, 0.1):
        x_values.append(i)
        y_values.append(f(i))

def plot_func_graphic():
    plt.plot(x_values, y_values, color='purple', label='Function')

    conv_x = np.array(x_values, dtype=float)
    conv_y = np.array(y_values, dtype=float)
    
    plt.fill_between(conv_x, conv_y, color='purple', alpha=0.2)

    plt.grid(True)
    plt.show()

def rect_integration(a, b, rectangles):
    accumulator = 0

    a = float(a)
    b = float(b)
    rectangles = float(rectangles)

    i = (b - a) / rectangles

    x0 = a
    x1 = a + i

    while (a <= x1 <= b) or (a >= x1 >= b):
        area = f((x0 + x1) / 2) * i
        accumulator += area

        x1 += i
        x0 += i

    return accumulator

a = 0
b = 3

func_generate(a, b)
plot_func_graphic()

os.system("cls")

print(rect_integration(a, b, 20))