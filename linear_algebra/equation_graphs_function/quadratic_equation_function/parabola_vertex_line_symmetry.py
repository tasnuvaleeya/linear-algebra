import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


def plot_parabola(a, b, c):
    # get the x value for the line of symmetry
    vx = (-1*b/2*a)
    # get the y value when x is at the line of symmetry
    vy = a*vx**2 + b*vx + c
    # Create a dataframe with an x column containing values from x-10 to x+10
    minx = int(vx - 10)
    maxx = int(vx + 10)

    df = pd.DataFrame({'x': range(minx, maxx)})
    # Add a y column by applying the quadratic equation to x
    df['y'] = a*df['x']**2 + b*df['x'] + c

    # get min and max of y value
    miny = df.y.min()
    maxy = df.y.max()

    plt.plot(df.x, df.y, color='grey')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.axvline()
    plt.axhline()

    # plot the line of symmetry
    sx = [vx, vx]
    sy = [miny, maxy]
    plt.plot(sx, sy, color='magenta')

    # Annotate the vertex
    plt.scatter(vx, vy, color='red')
    plt.annotate('vertex', (vx, vy), xytext=(vx - 1, (vy + 5) * np.sign(a)))
    plt.show()


plot_parabola(2, 2, -4)
plot_parabola(-2, 3, 5)




