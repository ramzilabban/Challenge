### Ramzi Roy Labban
### Q3 - Plot 1

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('Plot2.csv', low_memory=False)
y = df['State']
x1 = df['BP10000N'] # Beds per 10,000 population - normalized
x2 = df['INCOMEN'] # Income per capita - normalized
N = len(y)
ind = np.arange(N)
width = 0.4      
fig, ax = plt.subplots()
rectsA = ax.barh(ind,x1, width, color='yellow')
rectsB = ax.barh( ind + width,x2,width, color='blue')
ax.set_title('Staffed Hospital Beds vs Income per Capita')
ax.set_yticks(ind + width / 2)
ax.set_yticklabels(y,fontsize=6)
ax.invert_yaxis()  # labels read top-to-bottom
ax.legend((rectsA[0], rectsB[0]), ('Staffed Beds', 'Income'))
plt.show()
