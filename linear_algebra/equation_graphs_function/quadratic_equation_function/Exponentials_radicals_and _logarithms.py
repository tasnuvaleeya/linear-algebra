# import math
# x = math.sqrt(25)
# cuberoot = round(64 ** (1/3))
# print(cuberoot)
# print(math.log(16, 4))
# print(math.log(10))
# print(math.log10(10))

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


df = pd.DataFrame({'x': range(-10, 10)})

df['y'] = 3 * df['x']**3

plt.plot(df.x, df.y, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axvline()
plt.axhline()
plt.show()
