import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

'''
𝑦=2(𝑥−1)(𝑥+2)

when y=0 x=-2 or 1


'''
x1 = -2
x2 = 1

# Create a dataframe with an x column containing some values to plot

df = pd.DataFrame({'x': range(x1-5, x2+6)})

# Add a y column by applying the quadratic equation to x

df['y'] = 2 * (df['x'] - 1) * (df['x'] + 2)
# Get x at the line of symmetry (halfway between x1 and x2)
vx = (x1 + x2)/2
# Get y when x is at the line of symmetry
vy = 2 * (vx - 1) * (vx + 2)
# get min and max y values
miny = df.y.min()
maxy = df.y.max()

plt.plot(df.x, df.y, color='grey')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline()
plt.axvline()
# plt.show()
# Plot calculated x value for y = 0

plt.scatter([x1, x2], [0, 0], color='green')
plt.annotate('x1', (x1, 0))
plt.annotate('x2', (x2, 0))
# plt.show()
# plot the line of symmetry
sx = [vx, vx]
sy = [miny, maxy]

plt.plot(sx, sy, color='magenta')

# Annotate the vertex
plt.scatter(vx, vy, color='red')
plt.annotate('vertex', (vx, vy), xytext=(vx - 1, (vy-5)))
plt.show()
