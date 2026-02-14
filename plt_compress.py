import matplotlib.pyplot as plt
import numpy as np

import matplotlib
import matplotlib as mpl

import matplotlib.colors as mcolors
from matplotlib.gridspec import GridSpec

from parameters import colors, chirps, ts, raw_data, datamap

new_raw_data = np.zeros(raw_data.shape)
for i in range(6):
    new_raw_data[i] = raw_data[0]+i
new_raw_data[:, 4:6] = 0.0
range1 = ['...'] * len(ts)
for i in range(len(ts)):
    if ts[i] != "...":
        range1[i] = 'range' + ts[i]

fig = plt.figure(figsize=(10,10))
ax1 = plt.subplot(1, 2, 1)
ax2 = plt.subplot(7, 2, 2)
ax3 = plt.subplot(7, 2, 4)
ax4 = plt.subplot(7, 2, 6)
ax5 = plt.subplot(7, 2, 8)
ax6 = plt.subplot(7, 2, 10)
ax7 = plt.subplot(7, 2, 12)
ax8 = plt.subplot(7, 2, 14)


ax = ax1
cmap = mcolors.LinearSegmentedColormap.from_list("my_cmap", [(0.5,0.5,0.5)]+colors[0]+colors[1]+colors[2]+colors[3]+colors[4]+colors[5])# N=13)
datamap(ax, np.vstack((new_raw_data[0:6].T, [0.5,1.5,2.5,3.5,4.5,5.5])), "Mantissa (16 bits) and Exponent", cmap=cmap)
ax.set_xticks(range(6), labels=['Rx1', 'Rx2', 'Rx3', 'Rx4', 'Rx5', 'Rx6'])
ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
ax.set_yticks(range(len(range1)+1), labels=range1+['Exponent'])

axs = (ax2, ax3, ax4, ax5, ax6, ax7, ax8)
aa = np.ones(raw_data.shape)

for i in range(6):
    cmap = mcolors.LinearSegmentedColormap.from_list("my_cmap", [(0.5,0.5,0.5)]+colors[i]+[(1.0,1.0,1.0)], N=4)
    datamap(axs[i],np.vstack((raw_data[0], aa[2:4]*1.5)), "", cmap=cmap, aspect=0.3)#"Rx"+str(i+1)+" (8 bits)"
    axs[i].set_xticks([])#range(len(ts)), labels=ts,
#              rotation=45, ha="right", rotation_mode="anchor")
    axs[i].set_yticks([1], ['Rx'+str(i+1)])

cmap = mcolors.LinearSegmentedColormap.from_list("my_cmap", [(0.5,0.5,0.5),(0.5, 0.3137, 0.03137),(1, 0.6275, 0.06275), (1.0,1.0,1.0)])
datamap(axs[6],np.vstack((raw_data[0], aa[2:4]*1.5)), "", cmap=cmap, aspect=0.3)#"Rx"+str(i+1)+" (8 bits)"
axs[6].set_xticks([0, 1, 2, 3, 6, 7], labels=['r1', 'r2', 'r3', 'r4', 'r255', 'r256'])
axs[6].set_yticks([1], ['exp'])
fig.text(0.72, 0.9, 'Compressed data, mantissa (8 bits) and exponent', ha='center', va='center', fontsize=14)
plt.savefig('compress.png')
plt.show()
#ax = ax2
#cmap = mcolors.LinearSegmentedColormap.from_list("my_cmap", [colors[0][1],colors[1][1],colors[2][1],colors[3][1],colors[4][1],colors[5][1]])# N=13)
#datamap(ax, np.array([[1,2,3,4,5,6]]), "",cmap=cmap)
#ax.set_xticks([])
#ax.set_yticks([0], labels=['exponent'])
