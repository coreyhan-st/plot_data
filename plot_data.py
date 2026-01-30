import matplotlib.pyplot as plt
import numpy as np

import matplotlib
import matplotlib as mpl

chirps = ["1", "2", "3", "4", "5", "6", "7", "8", "...", "...", "1023", "1024"]
ts = ["1", "2", "3", "4", "...", "...", "511", "512"]
ts1 = [x for x in ts]
for i in range(len(chirps)):
    if chirps[i] != "...":
        chirps[i] = "chirps" + chirps[i]

for i in range(len(ts)):
    if ts[i] != "...":
        ts1[i] = "ts" + ts[i]   

raw_data = np.array([[1.0, 0.8, 1.0, 0.8, 0.5, 0.5, 0.8, 1.0],
                     [0.8, 1.0, 0.8, 1.0, 0.5, 0.5, 1.0, 0.8],
                     [1.0, 0.8, 1.0, 0.8, 0.5, 0.5, 0.8, 1.0],
                     [0.8, 1.0, 0.8, 1.0, 0.5, 0.5, 1.0, 0.8],
                     [1.0, 0.8, 1.0, 0.8, 0.5, 0.5, 0.8, 1.0],
                     [0.8, 1.0, 0.8, 1.0, 0.5, 0.5, 1.0, 0.8],
                     [1.0, 0.8, 1.0, 0.8, 0.5, 0.5, 0.8, 1.0],
                     [0.8, 1.0, 0.8, 1.0, 0.5, 0.5, 1.0, 0.8],
                     [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
                     [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
                     [1.0, 0.8, 1.0, 0.8, 0.5, 0.5, 0.8, 1.0],
                     [0.8, 1.0, 0.8, 1.0, 0.5, 0.5, 1.0, 0.0],
                    ])
aa = np.zeros(raw_data.shape)
colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

def datamap(ax, data, title, **kwargs):
    im = ax.imshow(data, **kwargs)

    # Show all ticks and label them with the respective list entries
    ax.set_title(title)#"Raw Data on Rx1 (14 bits)")

fig, ax = plt.subplots()

datamap(ax, raw_data, "Raw Data on Rx1 (14 bits)", cmap="Greens")
ax.set_xticks(range(len(ts1)), labels=ts1)
ax.set_yticks(range(len(chirps)), labels=chirps)

# Loop over data dimensions and create text annotations.
for i in range(len(chirps)):
    for j in range(len(ts)):
        if chirps[i] != "...":
            text = ax.text(j, i, ts[j],
                           ha="center", va="center", color="w")
        else:
            text = ax.text(j, i, "...",
                           ha="center", va="center", color="w")


fig.tight_layout()

fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3)
cmaps = ('Greens', 'Blues', 'Reds', 'Oranges', 'Purples', 'Greys')
datamap(ax1, raw_data, "Rx1", cmap=cmaps[0])
datamap(ax2, raw_data, "Rx2", cmap=cmaps[1])
datamap(ax3, raw_data, "Rx3", cmap=cmaps[2])
datamap(ax4, raw_data, "Rx4", cmap=cmaps[3])
datamap(ax5, raw_data, "Rx5", cmap=cmaps[4])
datamap(ax6, raw_data, "Rx6", cmap=cmaps[5])

fig = plt.figure()
ax1=plt.subplot(261)
ax2=plt.subplot(262)
ax3=plt.subplot(263)
ax6=plt.subplot(266)
ax7=plt.subplot(212)
datamap(ax1, np.vstack((raw_data[1], aa[2:-1])), "Rx1", cmap=cmaps[0])
datamap(ax2, np.vstack((raw_data[1], aa[2:-1])), "Rx2", cmap=cmaps[1])
datamap(ax3, np.vstack((raw_data[1], aa[2:-1])), "Rx3", cmap=cmaps[2])
#datamap(ax4, raw_data, "Rx4", cmap=cmaps[3])
#datamap(ax5, raw_data, "Rx5", cmap=cmaps[4])
datamap(ax6, np.vstack((raw_data[1], aa[2:-1])), "Rx6", cmap=cmaps[5])
datamap(ax7, raw_data[1:6], "First Chirp from 6 Rx")
plt.show()
