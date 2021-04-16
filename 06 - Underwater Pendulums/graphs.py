import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

def g_water():
    return g*(1-(density_water/density_bob))
def m_water():
    return mass_bob*(1 + 0.5*(density_water/density_bob))
def period_theo(L):
    return 4*math.pi**2*m_water()*L/(mass_bob*g_water())

df = pd.read_csv('underwater_data.csv')

g = 9.81 # meters per second per second
density_water = 1000 # kilograms per meter cubed
density_bob = 7044.53 # kilograms per meter cubed
mass_bob = 0.06 # kilograms
L = np.linspace(0.1, 0.4, 500)

vec_period = np.vectorize(period_theo)
T_theo = vec_period(L)

sns.relplot(data = df, x = 'string_length', y = 'period_ave', color = 'red', label = 'Experimental Period')
plt.plot(L, T_theo, color = 'blue', label = 'Theoretical Period')
plt.errorbar(df['string_length'], df['period_ave'], df['error'], fmt = 'none', capsize = 3, color = 'red', label = 'Error')
plt.legend()
plt.title('Underwater Pendulum')
plt.xlabel('String Length (m)')
plt.ylabel('Period of Motion (s)')
plt.tight_layout()
plt.savefig('underwater_graph.png')
plt.show()
