import numpy as np
import matplotlib as mpl
from matplotlib import cm
import matplotlib.pyplot as plt

cmap=cm.RdYlGn


file1 = np.genfromtxt(r'data.csv',delimiter=',',names=True,dtype=None,)

a1 = file1['ratio']
a2 = file1['RT']
easiness = file1['easyness']

c = cm.ScalarMappable(cmap=cmap,norm=mpl.colors.Normalize(vmin=-1,vmax=1))
colors = c.to_rgba(easiness)

plt.scatter(a1,a2,c=colors,alpha=0.25)
plt.ylim(0,3000)
plt.savefig("fig1")
plt.show()

