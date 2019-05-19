import pandas as pd
from matplotlib import pyplot as plt

'''
y = 2*x**2 + 6*x + 7
'''

df = pd.DataFrame({'x': range(-8, 12)})
df['y'] = -2*df['x']**2 + 6*df['x'] + 7

plt.plot(df.x, df.y, color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline()
plt.axvline()
plt.show()
