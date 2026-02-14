import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# 1. Generate a sample signal
Fs = 8000  # Sampling frequency (Hz)
T = 1.0 / Fs # Sampling period (seconds)
N = 64   # Number of samples
t = np.arange(N) * T # Time vector
f0 = Fs/256*97

# A signal with 50 Hz and 120 Hz components
s = np.exp(1j * 2.0 * np.pi * f0 * t)
s1 = np.zeros(2*len(s))+1j*np.zeros(2*len(s))
s1[0::2] = s
s2 = np.append(s, np.zeros(N)+1j*np.zeros(N))
#print(s)
#print(s1)
#print(s2)

# 2. Compute the FFT
yf = fft(s)
# fig = plt.figure()
# plt.plot(np.abs(yf))
# plt.grid(True)
# plt.show()
# exit()
yf1 = fft(s1)
yf2 = fft(s2)
#print(yf)
#print(yf2)
#xf = fftfreq(N, T) # Frequency bins

# 3. Plot the magnitude spectrum (only positive frequencies)

fig = plt.figure(figsize=(10,5))
axs = [[0,0],[0,0]]
axs[0][0]=plt.subplot(2,2,1)
axs[0][1]=plt.subplot(2,2,2)
axs[1][0]=plt.subplot(2,2,3)
axs[1][1]=plt.subplot(2,2,4)
#fig, axs = plt.subplots(2, 2, figsize=(10, 5))
axs[0][0].plot(range(N), np.real(s), 'o-', label='orignal signal')
axs[0][0].plot(np.arange(0,N,0.5), np.real(s1), '.-', label='signal after inserting 0')
axs[0][0].set_xticks([0, 63], labels=['1', '64Ts'])
axs[0][0].legend()
axs[0][0].set_title('Before FFT ')
axs[0][1].plot(range(N), np.abs(yf), label='orignal signal')
axs[0][1].plot(np.arange(2*N), np.abs(yf1), '--', label='signal after inserting 0')
axs[0][1].set_xticks([0, 63, 127], labels=['1', 'Fs', '2Fs'])
axs[0][1].legend()
axs[0][1].set_title('After FFT')

axs[1][0].plot(range(N), np.real(s), label='orignal signal')
axs[1][0].plot(np.arange(2*N), np.real(s2), '--', label='signal after padding 0')
axs[1][0].set_xticks([0, 63, 127], labels=['1', '64Ts', '128Ts'])
axs[1][0].legend()
axs[1][0].set_title('Before FFT ')
axs[1][1].plot(range(N), np.abs(yf), 'o-', label='orignal signal')
axs[1][1].plot(np.arange(0,N,0.5), np.abs(yf2), '.-', label='signal after padding 0')
axs[1][1].set_xticks([0, 63], labels=['1', 'Fs'])
axs[1][1].legend()
axs[1][1].set_title('After FFT')

# plt.subplot(1, 2, 1)
# plt.plot(range(N), np.real(s))
# plt.title("Time Domain Signal")
# plt.xlabel("Time (s)")
# plt.ylabel("Amplitude")

# plt.subplot(1, 2, 2)
# # Keep only positive frequencies for plotting real signals
# # The spectrum is symmetric for real inputs
# #positive_freqs = xf > 0
# plt.plot(range(N), np.abs(yf))
# plt.title("Frequency Domain Spectrum")
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Magnitude")
#plt.legend()
plt.tight_layout()
plt.show()
