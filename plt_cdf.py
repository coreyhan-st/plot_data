import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
#data = np.random.normal(loc=0, scale=1, size=1000)
data = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    2,
    0,
    0,
    2,
    10,
    10,
    21,
    48,
    120,
    283,
    487,
    1016,
    1927,
    3541,
    6350,
    10523,
    15279,
    18544,
    21716,
    19350,
    13713,
    11543,
    4827,
    1369,
    391,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0]
print(len(data))
# Create the ECDF plot
total = sum(data)
cdf = np.zeros(64)
cdf[0] = data[0]
for i in range(1, 64):
    cdf[i] = cdf[i-1] + data[i]
cdf = cdf / total
print(cdf)
fig, ax1 = plt.subplots(figsize=(8,6))
ax1.bar(range(1,65),data, color='red', alpha=0.6)
ax1.set_ylabel('Histogram', color='red')
#ax1.xlim(1,64)
#plt.ecdf(data)

# Add labels and a title
#axs[0].title("Empirical Cumulative Distribution Function (ECDF)")
#axs[0].xlabel("Data values")
#axs[0].ylabel("Cumulative probability")
ax2 = ax1.twinx()
ax2.plot(range(1,65), cdf, 'o-', color='blue')
ax2.axhline(y=0.9, color='green', linestyle='--', linewidth=2, label='Threshold')
ax2.axvline(x=35.4, color='grey', linestyle='--', linewidth=2)
ax2.set_ylabel('CDF', color='blue')
ax2.set_xticks([1, 16, 32, 48, 64], labels=['1', '16', '32', '48', '64'])
plt.title("Histogram & CDF")
plt.xlim(1,64)
#plt.grid(axis='x')
plt.show()
