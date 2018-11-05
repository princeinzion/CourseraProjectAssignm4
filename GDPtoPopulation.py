import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('https://raw.githubusercontent.com/princeinzion/NigeriaGDPtoPopulation/master/API_NGA_DS2_en_csv_v2_10185307.csv', skiprows=4)

df = data.loc[[620, 1168], '1999':'2017']

df = df.T

dfp = df.pct_change()

dfp = dfp.reset_index()
dfp.columns = ['Years', 'Population', 'GDP']
dfp

fig = plt.figure(figsize=(20,10))

ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

dfp.plot(kind='line',x='Years',y='GDP', color='red', ax=ax1)
dfp.plot(kind='line',x='Years',y='Population', color='blue', ax=ax2)

plt.show()
