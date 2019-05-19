import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def h(x):
    if x >= 0:
        return 2 * np.sqrt(x)


x = range(-100, 101)
# get the corresponding y value from function
y = [h(a) for a in x]
plt.xlabel('x')
plt.ylabel('h(x)')
plt.grid()
plt.plot(x, y, color='purple')
# plot a filled circle at the end to indicate a closed interval
plt.plot(0, h(0), color='purple', marker='o', markerfacecolor='purple', markersize=8)
plt.show()
