import matplotlib.pyplot as plt
import numpy as np

import matplotlib
import matplotlib as mpl

import matplotlib.colors as mcolors
from matplotlib.gridspec import GridSpec

from parameters import colors, chirps, ts, raw_data, datamap

aa = np.ones(raw_data.shape)
ts1 = [x for x in ts]
range1 = ['...'] * len(ts)
for i in range(len(ts)):
    if ts[i] != "...":
        ts1[i] = "ts" + ts[i]
        range1[i] = 'range' + ts[i]

chirps1 = [x for x in chirps]
for i in range(len(chirps1)):
    if chirps1[i] != "...":
        chirps1[i] = "chirp" + chirps1[i]

fig = plt.figure(figsize=(10, 10))
gs1 = GridSpec(1, 6, top=0.98, bottom=0.5, wspace=0.05)
axs = [0] * 6
for i in range(6):
    axs[i] = fig.add_subplot(gs1[0,i])
gs2 = GridSpec(1, 1, top=0.48, bottom=0.10, left=0.05, right=0.48)
ax7 = fig.add_subplot(gs2[0,0])
gs3 = GridSpec(8, 1, top=0.48, bottom=0.05, left=0.5, right=0.98)
ax8 = fig.add_subplot(gs3[:-1,:])
ax9 = fig.add_subplot(gs3[-1,:])
# ax1 = fig.add_subplot(gs1[0,0])
# ax1=plt.subplot(261)
# ax2=plt.subplot(262)
# ax3=plt.subplot(263)
# ax4=plt.subplot(264)
# ax5=plt.subplot(265)
# ax6=plt.subplot(266)
# ax7=plt.subplot(223)
# ax8=plt.subplot(324)
# ax9=plt.subplot(326)
# axs = (ax1, ax2, ax3, ax4, ax5, ax6)

for i in range(6):
    cmap = mcolors.LinearSegmentedColormap.from_list("my_cmap", [(0.5,0.5,0.5)]+colors[i]+[(1.0,1.0,1.0)], N=4)
    datamap(axs[i], np.vstack((raw_data[0], aa[2:-1]*1.5)), "Rx"+str(i+1), cmap=cmap)
    axs[i].set_xticks(range(len(ts)), labels=ts,
              rotation=45, ha="right", rotation_mode="anchor")
    axs[i].set_yticks([])
axs[0].set_yticks([0], labels=['1'])

new_raw_data = np.zeros(raw_data.shape)
for i in range(6):
    new_raw_data[i] = raw_data[0]+i
new_raw_data[:, 4:6] = 0.0
#print(new_raw_data)
cmap = mcolors.LinearSegmentedColormap.from_list("my_cmap", [(0.5,0.5,0.5)]+colors[0]+colors[1]+colors[2]+colors[3]+colors[4]+colors[5])# N=13)
ax = ax7
datamap(ax, new_raw_data[0:6].T, "Rearange data for range FFT (14 bits)",cmap=cmap)

# for i in range(4):
#     for j in range(len(ts)):
#         if chirps[i] != "...":
#             text = ax.text(j, i, ts[j],
#                            ha="center", va="center", color="w")
#         else:
#             text = ax.text(j, i, "...",
#                            ha="center", va="center", color="w")
ax.set_yticks(range(len(ts1)), labels=ts1)
#              rotation=45, ha="right", rotation_mode="anchor")
ax.set_xticks(range(6), labels=['Rx1', 'Rx2', 'Rx3', 'Rx4', 'Rx5', 'Rx6'])
ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
ax = ax8
datamap(ax, new_raw_data[0:6].T, "After range FFT - mantissa (16 bits)",cmap=cmap)
ax.set_xticks(range(6), labels=['Rx1', 'Rx2', 'Rx3', 'Rx4', 'Rx5', 'Rx6'])
ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
ax.set_yticks(range(len(ts1)), labels=range1)
ax = ax9
cmap = mcolors.LinearSegmentedColormap.from_list("my_cmap", [colors[0][1],colors[1][1],colors[2][1],colors[3][1],colors[4][1],colors[5][1]])# N=13)
datamap(ax, np.array([[1,2,3,4,5,6]]), "",cmap=cmap)
ax.set_xticks([])
ax.set_yticks([0], labels=['exponent'])
#ax.colorbar(label='exponent')
fig.tight_layout()
plt.savefig("range_fft.png")
plt.show()
exit()

fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(10,10))
new_raw_data = np.zeros(raw_data.shape)
for i in range(6):
    new_raw_data[:,i] = raw_data[:, 0]+i
new_raw_data[8:10, :] = 0.0
#print(new_raw_data)
#ax1=plt.subplot(121)
datamap(ax1, new_raw_data[:, 0:6], "Range1 for 6 antennas", cmap=cmap)
ax1.set_xticks(range(6), labels=['Rx1', 'Rx2', 'Rx3', 'Rx4', 'Rx5', 'Rx6'])
ax1.set_yticks(range(len(chirps1)), labels= chirps1)
#ax1.title()
#ax2=plt.subplot(122)
doppler = [x for x in chirps]
for i in range(len(doppler)):
    if doppler[i] != "...":
        doppler[i] = "doppler" + doppler[i]
datamap(ax2, new_raw_data[:, 0:6], "Doppler for 6 antennas", cmap=cmap)
ax2.set_xticks(range(6), labels=['Rx1', 'Rx2', 'Rx3', 'Rx4', 'Rx5', 'Rx6'])
ax2.set_yticks(range(len(chirps1)), labels= doppler)
fig.tight_layout()
plt.savefig("figur4.png")
plt.show()
