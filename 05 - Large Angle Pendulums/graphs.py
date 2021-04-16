import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math

sns.set_style('darkgrid')

df_data = pd.read_csv("large_angle_data.csv")

def deg_to_rad(deg):
    return deg*math.pi/180
def theory_small_angle(L, theta):
    return 2*math.pi*math.sqrt(L/g)
def theory_large_angle(L, theta):
    return 2*math.pi*math.sqrt(L/(g*math.cos(deg_to_rad(theta)/2)))

# Experiments
# 1. One 1-peso coin
# 2. Two 1-peso coins
# 3. Five 1-peso coins
# 4. 10 1-peso coins

g = 9.81 # meters per second per second
L = 0.24 # meters

vec_theory = np.vectorize(theory_small_angle)
vec_large_ang = np.vectorize(theory_large_angle)
theta = np.linspace(5,65,200)
T_theoretical_small_angle = vec_theory(L, theta)
T_theoretical_large_angle = vec_large_ang(L, theta)

sns.relplot(data = df_data, x = 'angle', y = 'period_ave', color = 'red', label = 'Experimental Period')
plt.plot(theta, T_theoretical_small_angle, color = 'blue', label = 'Theoretical Period (Small Angle Approximation)')
plt.plot(theta, T_theoretical_large_angle, color = 'green', label = 'Theoretical Period (Large Angle Approximation)')
plt.errorbar(df_data['angle'], df_data['period_ave'], df_data['error'], fmt = 'none', capsize = 3, color = 'red', label = 'Error')
plt.legend()
plt.title('Large Angle Pendulum')
plt.xlabel('Angle (Degrees)')
plt.ylabel('Period of Motion (s)')
plt.tight_layout()
plt.savefig('large_angle_graph.png')
plt.show()
