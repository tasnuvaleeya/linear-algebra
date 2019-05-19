import numpy as np
from matplotlib import pyplot as plt


def r(x):
    return (x)**2 + x

x = np.array(range(0, 11))
secant = np.array([2, 7])
x1 = secant[0]
x2 = secant[-1]
y1 = r(x1)
y2 = r(x2)
a = (y2 - y1)/(x2 - x1)
plt.xlabel('Seconds')
plt.ylabel('Meters')
plt.axhline()
plt.axvline()
plt.grid()
plt.plot(x, r(x), color='green')
plt.plot(secant, r(secant), color='magenta')
plt.annotate('Average Velocity = ' + str(a) + ' m/s', ((x2 + x1)/2, (y2 + y1)/2))
plt.show()