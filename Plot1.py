import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('Plot1.csv', low_memory=False)
y = df['State']
x1 = df['PP1N1'] # Physicians per 100,000 population - normalized
x2 = df['IPCN1'] # Income per capita - normalized
N = len(y)
ind = np.arange(N)
width = 0.4      
fig, ax = plt.subplots()
rectsA = ax.barh(ind,x1, width, color='orange')
rectsB = ax.barh( ind + width,x2,width, color='green')
ax.set_title('Physicians vs Income per Capita')
ax.set_yticks(ind + width / 2)
ax.set_yticklabels(y,fontsize=6)
ax.invert_yaxis()  # labels read top-to-bottom
ax.legend((rectsA[0], rectsB[0]), ('Physicians', 'Income'))
plt.show()
