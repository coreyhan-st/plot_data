import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (needed for 3D projection)

# 1. Create grid
x = np.arange(0, 64)
y = np.arange(0, 2048)
X, Y = np.meshgrid(x, y)

# 2. Define several peaks (2D Gaussians)
def gaussian(x0, y0, sx, sy, amp=1.0):
    return amp * np.exp(-(((X - x0)**2)/(2*sx**2) + ((Y - y0)**2)/(2*sy**2)))
y1 = [(y*256-100)%2048 for y in range(6)]
Z = 0.1 * np.sin(0.5 * (X-32)/4) * np.cos(0.5 * (Y-1024)/256)
for i in range(6):
    Z += gaussian(16, y1[i], 2, 2, amp=0.3)
    Z += gaussian(48, y1[i], 2, 2, amp=0.2)

# Optionally add a small background / noise
#Z += 0.1 * np.sin(0.5 * (X-32)/4) * np.cos(0.5 * (Y-1024)/256)
Z *= 2**10*80
print(np.max(Z))
fig, ax = plt.subplots(figsize=(10, 10))
im = ax.imshow(abs(Z), aspect=1/16)
ax.set_xticks([0, 15, 31, 47, 63], labels=['1', '16', '32', '48', '64'])
ax.set_yticks([0, 511, 1023, 1535, 2047], labels=['1', '512', '1024', '1536', '2048'])
cbar = plt.colorbar(im)#surf, shrink=0.5, aspect=10)
cbar.set_label("Value scale")
ax.set_title("Amplitude in Doppler and Angle domain 2D plot")
ax.set_xlabel("Angle")
ax.set_ylabel("Doppler")
plt.savefig("amplitude_2D")

# 3. Plot the surface
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d")

surf = ax.plot_surface(
    X, Y, Z,
    cmap="viridis",
    linewidth=0,
    antialiased=True,
    rstride=1,
    cstride=1
)

# 4. Decorations
ax.set_title("Amplitude in Doppler and Angle domain 3D plot")
ax.set_xlabel("Angle")
ax.set_ylabel("Doppler")
ax.set_zlabel("Amplitude")
ax.set_xticks([0, 31, 63], labels=['1', '32', '64'])
ax.set_yticks([0, 511, 1023, 1535, 2047], labels=['1', '512', '1024', '1536', '2048'])

#fig.colorbar(surf, shrink=0.5, aspect=10)
plt.tight_layout()
plt.savefig("amplitude_3D")
plt.show()

