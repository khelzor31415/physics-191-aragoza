import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math

g = 9.81 # meter per second per second
sns.set_style('darkgrid')

df = pd.read_csv('torsional_d_data.csv')
def theory_torsional(R, H, L, d):
    return 2*math.pi*(L/d)/math.sqrt(12)*math.sqrt((H-R)/g)

R = 0.005
M = 1
L = 0.215
H = 0.2

vec_torsional = np.vectorize(theory_torsional)
d = np.linspace(0.01, 0.11, 200)
T_torsional_d = vec_torsional(R, H, L, d)

sns.relplot(data=df, x='d', y='period_ave', color = 'red', label = 'Experimental Period')
plt.plot(d, T_torsional_d, color = 'blue', label = 'Theoretical Period')
plt.errorbar(df['d'], df['period_ave'], df['error'], fmt = 'none', capsize = 3, color = 'red', label = 'Error')
plt.legend()
plt.title('Torsional Bifilar Pendulum (Changing d)')
plt.xlabel('Distance of Support Point from Center of Mass, d (m)')
plt.ylabel('Period of Motion (s)')
plt.tight_layout()
plt.savefig('torsional_d_graph.png')
plt.show()
