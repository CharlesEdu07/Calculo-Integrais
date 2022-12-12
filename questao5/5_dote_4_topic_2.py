import matplotlib.pyplot as plt
import numpy as np
import cmath as cm
import os

from math import *
from sympy import *

x = symbols('x')

a = 0
b = 1

f = asin(sqrt(x)) / sqrt(x*(1-x))

res = integrate(f, (x, a, b))

os.system('cls')

print("Integral: ", res)
