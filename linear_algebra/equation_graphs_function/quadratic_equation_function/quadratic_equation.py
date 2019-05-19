import pandas as pd
from matplotlib import pyplot as plt
'''
y = 2*x**2 + 2*x -4
'''

# Create a dataframe with an x column containing values to plot

df = pd.DataFrame({'x': range(-9, 9)})

df['y'] = 2*df['x']**2 + 2*df['x'] -4

plt.plot(df.x, df.y, color="grey")

plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axvline()
plt.axhline()
plt.show()