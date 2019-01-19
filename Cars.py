# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
df = pd.read_csv(url, delim_whitespace=True, names=['mpg', 'cylinders', 'displacement', 'horsepower', 
                           'weight', 'acceleration', 'model year', 'origin', 'car name'])
df = pd.DataFrame(df)
df = df.replace('?', np.nan)
df['horsepower'] = pd.to_numeric(df['horsepower'])
df = df.fillna(df.mean())
df['horsepower'].hist()

cols = ['mpg', 'displacement', 'horsepower']
_, axs = plt.subplots(3, 3)
for n, a in enumerate(cols):
    axs[n, 0].hist[df[a]]
    axs[n, 0].set_title(a)
    axs[n, 1].boxplot[df[a]]
    axs[n, 1].set_title(a)
plt.show()
    
        
    