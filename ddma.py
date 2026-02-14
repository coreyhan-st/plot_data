import matplotlib.pyplot as plt
import numpy as np

N = 2048
v_a = 8
stride = N // v_a
labels = ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"]
locations = np.arange(0, N, stride)

fig, axs = plt.subplots(2, 1)
x = np.arange(N)
y1 = np.zeros((N,1))
y1[1:N-stride*2:stride] = 1
y2 = np.zeros((N,1))
y2[stride+64:N-stride:stride] = 1
axs[0].plot(x, y1, label='dopper1')
axs[0].plot(x, y2, label='dopper2')
axs[0].set_xticks(locations, labels)
axs[0].set_title("Two doppers can be separated")
axs[0].legend(title='Two dopplers')

y3 = np.zeros((N,1))
y3[stride+1:N-stride:stride] = 1
axs[1].plot(x, y1, label='dopper1')
axs[1].plot(x, y3, label='dopper2')
axs[1].set_xticks(locations, labels)
axs[1].set_title("Two doppers cannot be separated")
axs[1].legend(title='Two dopplers')

fig.tight_layout()
plt.savefig("ddma")
plt.show()
