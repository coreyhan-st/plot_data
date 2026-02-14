import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift

rx = np.ones(6)/6
rx_v = np.ones(36)/36

yf1 = fft(rx, 8)
yf2 = fft(rx, 64)
yf3 = fft(rx, 1024)
yf_v = fft(rx_v, 1024)

fig, ax = plt.subplots()
ax.plot(np.arange(-np.pi, np.pi, np.pi*2/8), 20*np.log10(fftshift(np.abs(yf1))), label="FFT size 8")
ax.plot(np.arange(-np.pi, np.pi, np.pi*2/64), 20*np.log10(fftshift(np.abs(yf2))), label="FFT size 64")
ax.plot(np.arange(-np.pi, np.pi, np.pi*2/1024), 20*np.log10(fftshift(np.abs(yf3))), ".-", label="FFT size 1024")
ax.plot(np.arange(-np.pi, np.pi, np.pi*2/1024), 20*np.log10(fftshift(np.abs(yf_v))), label="Virtual array 36 Rx")
ax.set_xticks([-np.pi, 0, np.pi], labels=['-\u03c0', '0', '\u03c0'])
ax.legend()
ax.set_title("Different angle FFT size vs Virtual Rx array size")
plt.grid(True)
plt.show()
