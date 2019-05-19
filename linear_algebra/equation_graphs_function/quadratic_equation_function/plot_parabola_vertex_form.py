import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

'''
y = a(x-h)**2 + k
'''

def plot_parabola_from_vertex_form(a, h, k):
    df = pd.DataFrame({'x': range(h - 10, h + 11)})
    df['y'] = a * (df['x'] - h)**2 + k
    miny = df.y.min()
    maxy = df.y.max()
    # calculate y when x is 0 (h+-h)
    y = a * (0 - h)**2 + k

    plt.plot(df.x, df.y, color='grey')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.axvline()
    plt.axhline()
    # Plot calculated y values for x = 0 (h-h and h+h)
    plt.scatter([h-h, h+h], [y, y], color='green')
    plt.annotate(str(h-h) + "," + str(y), (h-h, y))
    plt.annotate(str(h+h) + ", " + str(y), (h+h, y))
    # plot the line of symmetry (x = h)

    sx = [h, h]
    sy = [miny, maxy]
    plt.plot(sx, sy, color='magenta')

    # Annotate the vertex (h, k)
    plt.scatter(h, k, color='red')
    plt.annotate('v=' + str(h) + ',' + str(k), (h,k), xytext=(h-1, (k-10)))

    plt.show()


# print(plot_parabola_from_vertex_form(2, 4, -30))
print(plot_parabola_from_vertex_form(3, -1, -1))
