import numpy as np
from matplotlib import pyplot as plt


def q(x):
    return 2 * x + 1


x = np.array(range(0, 11))

plt.xlabel('Seconds')
plt.ylabel('Meters')
plt.xticks(range(0, 11, 1))
plt.yticks(range(0, 22, 2))
plt.grid()
plt.plot(x, q(x), color='green')
plt.show()
