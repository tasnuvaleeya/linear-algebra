import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'x': range(-10, 10)})
df['y'] = (3 * df['x'] - 4)/2

plt.plot(df.x, df.y, color='grey')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axvline()
plt.axhline()
# plt.show()

m = 1.5

yIntercept = -2
# xIntercept =
mx = [0, 1]
my = [yIntercept, yIntercept + m]
plt.plot(mx, my, color="red", lw=5)
plt.show()