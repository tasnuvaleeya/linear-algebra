import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def g(x):
    if x != 0:
        return (12/(2*x))**2


x = range(-100, 101)

y = [g(a) for a in x]


# Create an array of x values from -100 to 100
x = np.array(range(-100, 101))

plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid()


# Plot x against g(x)
plt.plot(x, y, color='purple')

# plot an empty circle to show the undefined point
plt.plot(0, g(0.0000001), color='purple', marker='o', markerfacecolor='w', markersize=8)

plt.show()