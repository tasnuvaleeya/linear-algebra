
import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'x': range(-10, 10)})

# define slope and y intercept
m = 1.5
yIntercept = -2
df['y'] = m*df['x'] + yIntercept

# plot the line

plt.plot(df.x, df.y, color='grey')
plt.xlabel('x')
plt.ylabel('y')
plt.axvline()
plt.axhline()

# label the y-intercept

plt.annotate('y-intercept', (0, yIntercept))

# plot the slope from the y-intercept for 1x

mx = [0, 1]
my = [yIntercept, yIntercept + m]
plt.plot(mx, my, color='red', lw=5)
plt.show()

