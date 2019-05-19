import pandas as pd
from matplotlib import pyplot as plt

# Get the max of 10 and 25 pound's chips

chipsAll10s = [16, 0]
chipsAll25s = [0, 16]

# get the max value for both 10 and 25 pound's chips

valuesAll10s = [25, 0]
valuesAll25s = [0, 10]

plt.plot(chipsAll10s, chipsAll25s, color='blue')
plt.plot(valuesAll10s, valuesAll25s, color='green')
plt.xlabel('x (10 pound\'s chips)')
plt.ylabel('y (25 pound\'s chips')
plt.grid()
plt.show()
