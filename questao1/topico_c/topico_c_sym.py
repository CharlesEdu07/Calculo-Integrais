import matplotlib.pyplot as plt
import numpy as np
import cmath as cm
import os

from math import *
from sympy import *

x = symbols('x')

a = 0
b = 3

f = x / (sqrt(x**2 + 9))

res = integrate(f, (x, a, b))

os.system('cls')

print("Integral: ", res)
