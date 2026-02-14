import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import LogNorm
import matplotlib.colors as mcolors
from parameters import colors

N = 8
x_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
y_labels = ['Hypothesis'+str(x+1) for x in range(N)]
txs = ['TX'+str(x+1) for x in range(6)]
txs.append('0')
txs.append('0')
# Fixing random state for reproducibility
#np.random.seed(19680801)

Z = np.zeros((N, N))
for i in range(N):
    Z[:,i] = i

fig, ax = plt.subplots(1, 1)

#c = ax0.pcolor(Z)
#ax0.set_title('default: no edges')
print(Z)
cmap = mcolors.LinearSegmentedColormap.from_list("my_cmap", [colors[0][1],colors[1][1],colors[2][1],colors[3][1],colors[4][1],colors[5][1],(0.4,0.4,0.4),(0.6,0.6,0.6)])
c = ax.pcolor(Z, edgecolors='k', linewidths=2, cmap=cmap)
for i in range(len(y_labels)):
    for j in range(len(x_labels)):
        text = ax.text((i+j)%8+0.5, i+0.5, txs[j],
                       ha="center", va="center", color="w")

ax.set_title('Different Hypothesis Corresponding to Different Empty Band Locations')
ax.set_xticks(np.arange(len(x_labels))+0.5, labels=x_labels)
ax.set_yticks(np.arange(len(y_labels))+0.5, labels=y_labels)

fig.tight_layout()
plt.savefig("ddma_map")
plt.show()
