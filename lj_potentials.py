import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('classic')

r = np.linspace(0.01, 100.0, 100000)


def E_LJ(r, epsilon, sigma):
    return 4 * epsilon * ((sigma / r) ** 12 - (sigma / r) ** 6)


def F_LJ(r, epsilon, sigma):
    return 24 * epsilon * ((sigma / r) ** 6 - 2 * (sigma / r) ** 12)


epsilon = 30
sigma = 30
r0 = sigma * 2 ** (1 / 6)

plt.figure(facecolor='white', figsize=(6, 6))
plt.title(r"$Lennard-Jones\ Potential$", fontsize=16)
plt.plot(r, E_LJ(r, epsilon, sigma), color='red', label="$LJ\ potential$")
plt.plot(r, F_LJ(r, epsilon, sigma), color='blue', label=r"$LJ\ force$")
plt.scatter(r0, 0, color='black', marker='o', s=30)
plt.xlim([0.0, 3*sigma])
plt.ylim([-1.5*epsilon, 1.5*epsilon])
plt.xlabel(r"$r$", fontsize=12)
plt.ylabel(r"$E_{LJ}(r)$", fontsize=12)
plt.axvline(r0, color='black', linestyle='--', linewidth=1.2)
plt.axhline(0, color='black', linestyle='--', linewidth=1.2)
plt.grid(color='grey', linestyle='solid', linewidth=0.3)
plt.legend()
plt.show()
# plt.savefig('mm.png', dpi=300)
