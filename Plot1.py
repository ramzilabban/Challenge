### Ramzi Roy Labban
### Plot #1 from Q3

import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('Plot1.csv', low_memory=False)
y = df['State']
x1 = df['PP1N1'] # Physicians per 100,000 population - normalized
x2 = df['IPCN1'] # Income per capita - normalized
fig, axes = plt.subplots(ncols=2, sharey=True)
axes[0].barh(y, x1, align='center', color='green')
axes[1].barh(y, x2, align='center', color='blue')
axes[0].invert_yaxis()  # labels read top-to-bottom
axes[0].set_xlabel('Physicians per 100,000 population - normalized', fontsize=8)
axes[1].set_xlabel('Income per capita - normalized', fontsize=8)
fig.suptitle('Physicians vs Income per Capita', fontsize=10)
axes[0].set_yticklabels(y,fontsize=6)
plt.show()
