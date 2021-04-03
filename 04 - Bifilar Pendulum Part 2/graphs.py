import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math

g = 9.81 # meter per second per second
sns.set_style('darkgrid')

df_inclined = pd.read_csv("inclined_data.csv")

# R is the radius of the rod
# L is the length of the rod
# M is the mass of the rod
# H is the length of the string
# d is the distance from the center of mass
def theory_inclined(R,H,L,d):
    return 2*math.pi*(L/d)/math.sqrt(12)*math.sqrt((H-R)/g)


R = 0.005
M = 1
L = 0.215
d = 0.065 #confirm

vec_inclined = np.vectorize(theory_inclined)

H = np.linspace(0.1,0.7,200)

T_inclined = vec_inclined(R,H,L,d)

sns.relplot(data=df_inclined, x = 'string_length', y = 'period_ave', color = 'red', label = "Experimental Period")
plt.plot(H, T_inclined, color = 'blue', label = "Theoretical Period")
plt.errorbar(df_inclined['string_length'], df_inclined['period_ave'], df_inclined['error'], fmt = 'none', capsize = 3, color = 'red', label = 'Error')
plt.legend()
plt.title("Inclined Bifilar Pendulum (Torsional)")
plt.xlabel("Length of String (m)")
plt.ylabel("Period of Motion (s)")
plt.tight_layout()
plt.savefig("inclined_graph.png")
plt.show()
