import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def j(x):
    if x >= 0 and x <= 5:
        return x + 2

x = range(-100, 101)

y = [j(i) for i in x]

plt.xlabel('x')
plt.ylabel('y')
plt.grid()

plt.plot(x, y, color='purple')
plt.plot(0, j(0), color='purple', markefacecolor='purple', )