import matplotlib.pyplot as plt
import numpy as np
import cmath as cm
import os

from math import *
from sympy import *

x = symbols('x')

a = 1
b = 5

f = x**5

res = integrate(f, (x, a, b))

os.system('cls')

print("Integral: ", res)
