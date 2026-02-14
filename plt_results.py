import scipy.io as sio
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt


colors = [(0,0,0),(1, 0, 0),(0, 0, 1),(0, 1, 0)]

cmap = LinearSegmentedColormap.from_list('my_list', colors, N=4)

filename="results1.mat"
results = sio.loadmat(filename)
print(results.keys())
new_map = results['peaks_map'] # miss: 1
new_map += results['selected_cells_map']*2 # hit: 3, false: 2
plt.figure()
plt.imshow(new_map, cmap=cmap, aspect=0.125)
plt.show()

