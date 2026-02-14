import matplotlib.pyplot as plt
import numpy as np

import matplotlib
import matplotlib as mpl

import matplotlib.colors as mcolors
from parameters import colors, chirps, ts, raw_data, datamap
#cmap = mcolors.LinearSegmentedColormap.from_list("my_cmap", ["red", "green", "blue"])

chirps1 = [x for x in chirps]
ts1 = [x for x in ts]
for i in range(len(chirps1)):
    if chirps1[i] != "...":
        chirps1[i] = "chirp" + chirps1[i]

for i in range(len(ts)):
    if ts[i] != "...":
        ts1[i] = "ts" + ts[i]  

aa = np.ones(raw_data.shape)

fig, ax = plt.subplots(figsize=(10, 10))

cmap = mcolors.LinearSegmentedColormap.from_list("my_cmap", [(0.5,0.5,0.5)]+ colors[0], N=3)
datamap(ax, raw_data, "Raw Data on Rx1 (14 bits)", cmap=cmap)
ax.set_xticks(range(len(ts1)), labels=ts1)
ax.set_yticks(range(len(chirps1)), labels=chirps1)

# Loop over data dimensions and create text for i in range(len(chirps)):
for i in range(len(chirps)):
    for j in range(len(ts)):
        if chirps[i] != "...":
            text = ax.text(j, i, ts[j],
                           ha="center", va="center", color="w")
        else:
            text = ax.text(j, i, "...",
                           ha="center", va="center", color="w")


fig.tight_layout()
plt.savefig("raw_data_rx1.png")

fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, figsize=(10, 10))
cmaps = ('Greens', 'Blues', 'Reds', 'Oranges', 'Purples', 'Greys')
axs = (ax1, ax2, ax3, ax4, ax5, ax6)
for i in range(6):
    cmap = mcolors.LinearSegmentedColormap.from_list("my_cmap", [(0.5,0.5,0.5)]+ colors[i], N=3)
    datamap(axs[i], raw_data, "Rx"+str(i+1), cmap=cmap)
    axs[i].set_xticks(range(len(ts)), labels=ts,
                     rotation=45, ha="right", rotation_mode="anchor")
    axs[i].set_yticks(range(len(chirps)), labels=chirps)
fig.tight_layout()
plt.savefig("raw_data_6ants.png")
plt.show()
#exit()
#datamap(ax2, raw_data, "Rx2", cmap=cmaps[1])
#datamap(ax3, raw_data, "Rx3", cmap=cmaps[2])
#datamap(ax4, raw_data, "Rx4", cmap=cmaps[3])
#datamap(ax5, raw_data, "Rx5", cmap=cmaps[4])
#datamap(ax6, raw_data, "Rx6", cmap=cmaps[5])


