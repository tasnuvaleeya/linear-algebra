import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import math

'''
y = 3x**2 - 12
0 = 3x**2 -12
3x**2 = 12
x**2 = 4
x = +2, -2
'''

y = 0
x1 = int(- math.sqrt(12/3))
x2 = int(math.sqrt(12/3))

df = pd.DataFrame({'x': range(x1 - 10, x2 + 11)})

df['y'] = 3*df['x']**2 - 12
# Get x at the line of symmetry (halfway between x1 and x2)

vx = (x1 + x2)/2

# Get y when x is at the line of symmetry
vy = 3 * vx**2 - 12

# Get min and max y value

miny = df.y.min()
maxy = df.y.max()

# Plot the line

plt.plot(df.x, df.y, color='grey')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axvline()
plt.axhline()


# plot calculated x values when y=0

plt.scatter([x1, x2], [0, 0], color='green')
plt.annotate('x1', (x1, 0))
plt.annotate('x2', (x2, 0))

# Plot the line of symmetry
sx = [vx, vx]
sy = [miny, maxy]

plt.plot(sx, sy, color='magenta')

# Annotate the vertex
plt.scatter(vx, vy, color='red')
plt.annotate('vertex', (vx, vy), xytext=(vx - 1, (vy-20)))
plt.show()
