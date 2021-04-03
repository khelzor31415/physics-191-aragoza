import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math

g = 9.81 # meter per second per second
sns.set_style('darkgrid')

df_data = pd.read_csv("large_angle_data.csv")

def theory_small_angle(L):
    return 2*math.pi*math.sqrt(L/g)

# Experiments
# 1. One 1-peso coin
# 2. Two 1-peso coins
# 3. Five 1-peso coins
# 4. 10 1-peso coins

L = 0.25
m_peso = 0.006
