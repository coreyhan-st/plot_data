import matplotlib.pyplot as plt
import numpy as np

import matplotlib
import matplotlib as mpl

import matplotlib.colors as mcolors
from parameters import colors
from parameters import chirps, ts, raw_data

def datamap(ax, data, title, **kwargs):
    im = ax.imshow(data, **kwargs)

    # Show all ticks and label them with the respective list entries
    ax.set_title(title)#"Raw Data on Rx1 (14 bits)")

np.random.seed(19680801)
r1d = np.zeros((12,8))
for i in range(8):
    r1d[0:6, i] = np.array([1,2,3,4,5,6]) - (i%2)*0.5
#print(r1d)
new_raw_data = np.zeros(raw_data.shape)
for i in range(6):
    new_raw_data[:,i] = raw_data[:, 0]+i
new_raw_data[8:10, :] = 0.0


input_data = np.vstack((r1d,r1d,np.ones((4,8))*6.5, r1d))
data_shape = input_data.shape
output_data = np.random.rand(data_shape[0], data_shape[1])
output_data[24:28, :] = 0

fig = plt.figure(figsize=(10,10))
ax1 = plt.subplot(221)
ax2 = plt.subplot(122)
ax3 = plt.subplot(223)
cmap = mcolors.LinearSegmentedColormap.from_list("my_cmap", [(0.5,0.5,0.5)]+colors[0]+colors[1]+colors[2]+colors[3]+colors[4]+colors[5])# N=13)
datamap(ax1, new_raw_data[:, 0:6], "Doppler for 6 Rx Antennas", cmap=cmap, aspect=0.75)
ax1.set_xticks(range(6), labels=['Rx1', 'Rx2', 'Rx3', 'Rx4', 'Rx5', 'Rx6'])
ax1.set_yticks([0,2,4,6,10,11], labels=['d1', 'd3', 'd5', 'd7', 'd2047', 'd2048'])

cmap = mcolors.LinearSegmentedColormap.from_list("my_cmap", [(1,1,1)]+colors[0]+colors[1]+colors[2]+colors[3]+colors[4]+colors[5]+[(0.5,0.5,0.5)])
datamap(ax2, input_data, "Rearange data for angle FFT", cmap=cmap, aspect=0.3)
for i in range(6):
    for j in range(8):
        text = ax2.text(j, i, "d"+str(j+1)+"rx"+str(i+1),
                          ha="center", va="center", color="w")
for i in range(6):
    for j in range(8):
        text = ax2.text(j, 12+i, "d"+str(j+1+8)+"rx"+str(i+1),
                          ha="center", va="center", color="w")
for i in range(6):
    for j in range(8):
        text = ax2.text(j, 24+4+i, "d"+str(j+1+8*15)+"rx"+str(i+1),
                          ha="center", va="center", color="w")

ax2.set_xticks(range(8), labels=['1', '2', '3', '4', '5', '6', '7', '8'])
ax2.set_yticks([0,12,24+4, 24+4+11], labels=['1', '65', '961', '1024'])
cmap = mcolors.LinearSegmentedColormap.from_list("my_cmap", [(0.5,0.5,0.5)]+colors[0]+colors[1]+colors[2]+colors[3]+colors[4]+colors[5], N=32)
datamap(ax3, output_data, "Data after angle FFT", cmap=cmap, aspect=0.3)
ax3.set_xticks(range(8), labels=['1', '2', '3', '4', '5', '6', '7', '8'])
ax3.set_yticks([0,12,24+4, 24+4+11], labels=['1', '65', '961', '1024'])
fig.tight_layout()
plt.savefig("angle_fft.png")
plt.show()
