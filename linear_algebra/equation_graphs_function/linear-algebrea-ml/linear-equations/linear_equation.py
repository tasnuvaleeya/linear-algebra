import pandas as pd

from matplotlib import pyplot as plt

'''
2𝑦+3=3𝑥−1
'''
# Create a data-frame with an x column containing values from -10 to 10

df = pd.DataFrame({'x': range(-10, 11)})

# add a y column by applying the solved equation to x

df['y'] = (3 * df['x'] - 4)/2

# print(df)
plt.plot(df.x, df.y, color="grey", marker="o")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline()
plt.axvline()
plt.annotate("x-intercept", (1.333, 0))
plt.annotate("y-intercept", (0, -2))
plt.show()
