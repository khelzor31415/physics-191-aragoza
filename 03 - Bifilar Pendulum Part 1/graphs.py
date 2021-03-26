import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math

g = 9.81 # meter per second per second

# R is the radius of the rod
# L is the length of the rod
# M is the mass of the rod
# H is the length of the string
# d is the distance from the center of mass
def theory_swing(R, H):
    return 2*math.pi*math.sqrt((0.5*R**2+H**2)/(g*H))
def theory_lateral(R,H):
    return 2*math.pi*math.sqrt((H-R)/g)
def theory_torsional(R,H,L,d):
    return 2*math.pi*(L/d)/math.sqrt(12)*math.sqrt((H-R)/g)

# Insert lenghts used
# L = {{}}

R = 1
M = 1
L = 1
d = 1

vec_swing = np.vectorize(theory_swing)
vec_lateral = np.vectorize(theory_lateral)
vec_torsional = np.vectorize(theory_torsional)

H = np.linspace(10,30,200)

T_swing = vec_swing(R, H)
T_lateral = vec_lateral(R, H)
T_torsional = vec_torsional(R,H,L,d)

plt.plot(H, T_swing)
plt.title('Swingin')
plt.show()

plt.plot(H, T_lateral)
plt.title('Lateral')
plt.show()

plt.plot(H, T_torsional)
plt.title('Torsional')
plt.show()