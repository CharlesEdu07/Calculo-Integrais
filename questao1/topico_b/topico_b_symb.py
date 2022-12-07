import matplotlib.pyplot as plt
import numpy as np
import cmath as cm
import os

from math import *
from sympy import *

x = symbols('x')

a = 1
b = 2

f = 1 / (x * (x + 1)**2)

res = integrate(f, (x, a, b))

os.system('cls')

print("Integral: ", res)
