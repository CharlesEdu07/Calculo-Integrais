import matplotlib.pyplot as plt
import numpy as np
import cmath as cm
import os

from math import *
from sympy import *

x = symbols('x')

f = (sin(x))**2 - sin(x)*cos(x) + 2*(cos(x))**2 / sin(x) + 2*cos(x)

res = integrate(f, x)

os.system('cls')

print("Integral: ", res)
