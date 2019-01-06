# %% Import necessary packages
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np


# %% Read data
df = pd.read_csv('./bottle.csv')
df = df[['T_degC', 'Salnty']]
df.columns = ['Temp', 'Sal']
df.columns
