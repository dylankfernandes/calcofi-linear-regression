# This file is compatible with the Hydrogen extension for Atom (think Jupyter notebook integrated into Atom)
# A jupyter notebook of this file is also available.

# %% Import necessary packages
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np
import math

# %% Read data
df = pd.read_csv('./bottle.csv')
df = df[['T_degC', 'Salnty']] # we only need the temperature and salinity columns
df.columns = ['Temp', 'Salnty']
df.head()

# %% Plotting the data
df['Sal'] = df['Salnty'].apply(math.log)
sns.scatterplot('Salnty', 'Temp', data=df)

# %% Plotting the residuals - confirming heteroscedasticity
sns.residplot('Salnty', 'Temp', data=df)
