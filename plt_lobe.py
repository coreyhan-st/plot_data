import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000.0          # Sampling frequency [Hz]
f0 = 50#fs/256*97#50.0            # Signal frequency [Hz]

T_short = 0.1        # Short observation time [s]
T_long  = 0.2        # Long observation time [s]

# Generate time vectors
t_short = np.arange(0, 64)/fs#T_short, 1/fs)
t_long  = np.arange(0, 128)/fs#T_long,  1/fs)

# Generate sinusoidal signal
x_short = np.sin(2 * np.pi * f0 * t_short)
x_long  = np.sin(2 * np.pi * f0 * t_long)

def compute_spectrum(x, fs):
    N = len(x)
    # Zero-pad to improve visual frequency resolution (optional)
    Nfft = N*2
    X = np.fft.fft(x, n=Nfft)
    # One-sided spectrum
    freqs = np.fft.fftfreq(Nfft, d=1/fs)
    idx = freqs >= 0
    return freqs[idx], np.abs(X[idx]) / np.max(np.abs(X[idx]))

# Compute spectra
f_short, X_short = compute_spectrum(x_short, fs)
f_long,  X_long  = compute_spectrum(x_long,  fs)

# Plot
plt.figure(figsize=(10, 5))

plt.plot(f_short, X_short, label=f"Short window T = {T_short} s")
plt.plot(f_long,  X_long,  label=f"Long window T = {T_long} s", linestyle="--")

plt.xlim(0, 150)   # Focus around the main lobe region
plt.xlabel("Frequency [Hz]")
plt.ylabel("Normalized magnitude")
plt.title("Effect of observation time on spectrum main lobe width")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
