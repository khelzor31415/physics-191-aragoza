import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math

g = 9.81 # meter per second per second
df_lateral = pd.read_csv("lateral_data.csv")
df_swing = pd.read_csv("swing_data.csv")
df_torsional = pd.read_csv("torsional_data.csv")

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


R = 0.005
M = 1
L = 0.215
d = 0.071 #confirm

vec_swing = np.vectorize(theory_swing)
vec_lateral = np.vectorize(theory_lateral)
vec_torsional = np.vectorize(theory_torsional)

H = np.linspace(0.1,0.6,200)

T_swing = vec_swing(R, H)
T_lateral = vec_lateral(R, H)
T_torsional = vec_torsional(R,H,L,d)

plt.plot(H, T_swing)
plt.scatter(df_swing.string_length, df_swing.period_ave)
plt.xlabel("String Length (m)")
plt.ylabel("Period (s)")
plt.title('Swingin')
plt.show()

plt.plot(H, T_lateral)
plt.scatter(df_lateral.string_length, df_lateral.period_ave)
plt.xlabel("String Length (m)")
plt.ylabel("Period (s)")
plt.title('Lateral')
plt.show()

plt.plot(H, T_torsional)
plt.scatter(df_torsional.string_length, df_torsional.period_ave)
plt.xlabel("String Length (m)")
plt.ylabel("Period (s)")
plt.title('Torsional')
plt.show()