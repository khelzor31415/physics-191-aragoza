import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math

global g = 9.81 # meter per second per second
global unequal_data_df = pd.read_csv('unequal_data.csv')
global padded_data_df = pd.read_csv('padded_data.csv')
sns.set_style('darkgrid')

# measured quantities; cylinder mass m, cylinder length l,
# length of string 1 h1, length of string h2, and distance to com d

m = 1.0
l = 1.0
h2 = 1.0
d = 1.0
m_paddle = 1.0
paddle_width = 1.0
a = 1.0

# evaluation

def hEff(h1, h2):
    return 2*h1*h2/(h1+h2)
def epsil_(h1, h2):
    return (h1-h2)/(2*hEff(h1, h2))
def omega_0(h1, h2):
    return math.sqrt(g/hEff(h1, h2))
def I_unpadded(m, l):
    return m*l**2/12
def I_padded(m, l, m_paddle, paddle_width, a):
    # a is the distance of the edge of card to the center of mass
    I_paddle = 2*(m_paddle*paddle_width**2/3 + m_paddle*a**2)
    return I_unpadded(m, l) + I_paddle
def lambda_period(cond, d, m, l, m_paddle = 0.0, paddle_width = 0.0, a = 0.0):
    if cond == 'unpadded':
        return m*d**2/I_unpadded(m, l)
    if cond == 'padded':
        return m*d**2/I_padded(m, l, m_paddle, paddle_width, a)
def period(cond, h1, h2, d, m, l, m_paddle = 0.0, paddle_width = 0.0, a = 0.0):
    w_0 = omega_0(h1, h2)
    eps = epsil_(h1, h2)
    if cond == 'unpadded':
        lambda_ = lambda_period('unpadded', d, m, l)
    elif cond == 'padded':
        lambda_ = lambda_period('padded', d, m, l, m_paddle, paddle_width, a)

    w_plus = math.sqrt((w_0)**2*(0.5*(1+lambda_)+math.sqrt(4*(1-lambda_)**2 + lambda_*eps**2)))
    w_min = math.sqrt((w_0)**2*(0.5*(1+lambda_)-math.sqrt(4*(1-lambda_)**2 + lambda_*eps**2)))
    return (2*math.pi/w_plus, 2*math.pi/w_min)

# plot

vec_period = np.vectorize(period)
def plot_unpadded_graph():
    h1 = np.linspace(0.1, 1, 500)
    T_theo = period('unpadded', h1, h2, d, m, l)

    sns.relplot(data = unequal_data_df, x = 'h1', y = 'period_ave', color = 'red', label = "Experimental Period")
    plt.errorbar(unequal_data_df['h1'], unequal_data_df['period_ave'], unequal_data_df['error'], fmt = 'none', capsize = 3, color = 'red', label = 'Error')
    plt.plot(h1, T_theo[0], color = 'blue', label = "Theoretical Period $T_+$")
    plt.plot(h1, T_theo[1], color = 'green', label = "Theoretical Period $T_-$")

    plt.legend()
    plt.title("Unequal Bifilar Pendulum for $H_1 = $")
    plt.xlabel("Length of String (m)")
    plt.ylabel("Period of Motion (s)")

    plt.tight_layout()
    plt.savefig("unequal.png")
    plt.show()
def plot_padded_graph():
    h1 = np.linspace(0.1, 1, 500)
    T_theo = period('padded', h1, h2, d, m, l, m_paddle, paddle_width, a)

    sns.relplot(data = padded_data_df, x = 'h1', y = 'period_ave', color = 'red', label = "Experimental Period")
    plt.errorbar(padded_data_df['h1'], padded_data_df['period_ave'], padded_data_df['error'], fmt = 'none', capsize = 3, color = 'red', label = 'Error')
    plt.plot(h1, T_theo[0], color = 'blue', label = "Theoretical Period $T_+$")
    plt.plot(h1, T_theo[1], color = 'green', label = "Theoretical Period $T_-$")

    plt.legend()
    plt.title("Padded Unequal Bifilar Pendulum for $H_1 = $")
    plt.xlabel("Length of String (m)")
    plt.ylabel("Period of Motion (s)")

    plt.tight_layout()
    plt.savefig("unequal_padded.png")
    plt.show()
