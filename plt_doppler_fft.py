import matplotlib.pyplot as plt
import numpy as np

import matplotlib
import matplotlib as mpl

import matplotlib.colors as mcolors
from matplotlib.gridspec import GridSpec

from parameters import colors, chirps, ts, raw_data, datamap

aa = np.ones(raw_data.shape)
ts1 = [x for x in ts]
new_raw_data = np.zeros(raw_data.shape)
for i in range(6):
    new_raw_data[:,i] = raw_data[:,0]+i
new_raw_data[8:10, :] = 0.0

fig = plt.figure(figsize=(10, 10))

ax1=plt.subplot(441)
ax2=plt.subplot(442)
ax3=plt.subplot(443)
ax4=plt.subplot(444)
ax5=plt.subplot(445)
ax6=plt.subplot(446)
ax7=plt.subplot(448)
ax8=plt.subplot(223)
ax9=plt.subplot(224)

axs = (ax1, ax2, ax3, ax4, ax5, ax6, ax7)
for i in range(6):
    cmap = mcolors.LinearSegmentedColormap.from_list("my_cmap", [(0.5,0.5,0.5)]+colors[i])
    datamap(axs[i], raw_data, "Rx"+str(i+1)+ " mantissa (8 bits)", cmap=cmap)
    axs[i].set_xticks([0, 1, 2, 3, 7], labels=['r1', 'r2', 'r3', 'r4', 'r256'])#range(len(ts)), labels=ts,
#              rotation=45, ha="right", rotation_mode="anchor")
    axs[i].set_yticks([0,11], labels=['chirp1','chirp1024'])
    #axs[i].set_title
cmap = mcolors.LinearSegmentedColormap.from_list("my_cmap", [(0.5,0.5,0.5),(0.5, 0.3137, 0.03137),(1, 0.6275, 0.06275)])
datamap(axs[6], raw_data, "Exponent", cmap=cmap)
axs[6].set_xticks([0, 1, 2, 3,  7], labels=['r1', 'r2', 'r3', 'r4', 'r256'])
axs[6].set_yticks([0,11], ['chirp1','chirp1024'])

cmap = mcolors.LinearSegmentedColormap.from_list("my_cmap", [(0.5,0.5,0.5)]+colors[0]+colors[1]+colors[2]+colors[3]+colors[4]+colors[5])# N=13)
datamap(ax8, new_raw_data[:, 0:6], "Decompress data for Dopper FFT (16 bits)", cmap=cmap)
ax8.set_xticks(range(6), labels=['Rx1', 'Rx2', 'Rx3', 'Rx4', 'Rx5', 'Rx6'])
ax8.set_yticks([0,11], labels=['chirp1','chirp1024'])#range(len(chirps1)), labels= chirps1)
#ax1.title()
#ax2=plt.subplot(122)
doppler = [x for x in chirps]
for i in range(len(doppler)):
    if doppler[i] != "...":
        doppler[i] = "doppler" + doppler[i]
datamap(ax9, new_raw_data[:, 0:6], "Data after Doppler FFT", cmap=cmap)
ax9.set_xticks(range(6), labels=['Rx1', 'Rx2', 'Rx3', 'Rx4', 'Rx5', 'Rx6'])
ax9.set_yticks([0,11], labels=['doppler1','doppler1024'])#range(len(chirps1)), labels= doppler)
fig.tight_layout()
plt.savefig("doppler_fft.png")

plt.show()
