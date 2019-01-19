# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load the dataset:
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
df = pd.read_csv(url, delim_whitespace=True, names=['mpg', 'cylinders', 'displacement', 'horsepower', 
                           'weight', 'acceleration', 'model year', 'origin', 'car name'])
df = pd.DataFrame(df)
#missed values:
df = df.replace('?', np.nan) #to NaN
df['horsepower'] = pd.to_numeric(df['horsepower'])
#column average:
df = df.fillna(df.mean())

#vizualisation:
cols = ['mpg', 'horsepower']
plt.style.use('classic')
fig, axs = plt.subplots(2, 2, figsize=(6, 6))
for n, a in enumerate(cols):
    axs[n, 0].hist(df[a])
    axs[n, 0].set_title(a+)
    axs[n, 1].boxplot(df[a])
    axs[n, 1].set_title(a+' box')
    fig.subplots_adjust(hspace=0.4)
axs[0, 0].set_xlabel('Miles Per Gallon')
axs[1, 0].set_xlabel('Horses')
fig.suptitle('Muscle cars').set_size(20)
fig.savefig('1.jpeg', dpi = 600)
plt.show()
    
        
    