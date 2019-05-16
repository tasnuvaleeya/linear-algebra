import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# Create an array of x values from -100 to 100
x = np.array(range(-100, 101))
# Set up the graph


plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.plot(x, f(x), color='purple')
plt.show()
