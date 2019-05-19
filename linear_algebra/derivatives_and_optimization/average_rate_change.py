import numpy as np
from matplotlib import pyplot as plt

def r(x):
    return (x)**2 + x

x = np.array(range(0, 11))

# Create an array for the secant line
secant = np.array([0, 10])
plt.xlabel('Seconds')
plt.ylabel('Meters')
plt.grid()
plt.plot(x, r(x), color='green')
plt.plot(secant, r(secant), color='magenta')
plt.axvline()
plt.axhline()
plt.show()