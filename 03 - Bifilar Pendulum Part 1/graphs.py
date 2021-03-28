import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math

g = 9.81 # meter per second per second
sns.set_style('darkgrid')

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

sns.relplot(data=df_swing, x = 'string_length', y = 'period_ave', color = 'red', label = "Experimental Period")
plt.plot(H, T_swing, color = 'blue', label = "Theoretical Period")
plt.errorbar(df_swing['string_length'], df_swing['period_ave'], df_swing['error'], fmt = 'none', capsize = 3, color = 'red', label = 'Error')
plt.legend()
plt.title("Swinging Bifilar Pendulum")
plt.xlabel("Length of String (m)")
plt.ylabel("Period of Motion (s)")
plt.tight_layout()
plt.savefig("swinging_graph.png")
plt.show()

sns.relplot(data=df_lateral, x = 'string_length', y = 'period_ave', color = 'red', label = "Experimental Period")
plt.plot(H, T_lateral, color = 'blue', label = "Theoretical Period")
plt.errorbar(df_lateral['string_length'], df_lateral['period_ave'], df_lateral['error'], fmt = 'none', capsize = 3, color = 'red', label = 'Error')
plt.legend()
plt.title("Lateral Bifilar Pendulum")
plt.xlabel("Length of String (m)")
plt.ylabel("Period of Motion (s)")
plt.tight_layout()
plt.savefig("lateral_graph.png")
plt.show()

sns.relplot(data=df_torsional, x = 'string_length', y = 'period_ave', color = 'red', label = "Experimental Period")
plt.plot(H, T_torsional, color = 'blue', label = "Theoretical Period")
plt.errorbar(df_torsional['string_length'], df_torsional['period_ave'], df_torsional['error'], fmt = 'none', capsize = 3, color = 'red', label = 'Error')
plt.legend()
plt.title("Torsional Bifilar Pendulum")
plt.xlabel("Length of String (m)")
plt.ylabel("Period of Motion (s)")
plt.tight_layout()
plt.savefig("torsional_graph.png")
plt.show()
