import pandas as pd
import math
from matplotlib import pyplot as plt


def plot_parabola_from_formula(a, b, c):
    print('Calculating the Vertex')
    print('vx = -b/2a')

    nb = -b
    a2 = 2*a

    print('vx = ' + str(nb) + '/' + str(a2))
    vx = -b/(2*a)

    print('vx = ' + str(vx))

    print('\nvy = ax^2 + bx + c')
    print('vy = ' + str(a) + '(' + str(vx) + '^2) + ' + str(b) + '(' + str(vx) +') + ' + str(c))
    avx2 = a*vx**2
    bvx = b*vx
    print('vy = ' + str(avx2) + ' + ' + str(bvx) + ' + ' + str(c))

    vy = avx2 + bvx + c
    print('vy = ' + str(vy))
    print('\nv = ' + str(vx) + ',' + str(vy))

    # Get +x and -x (showing intermediate calculations)
    print('\n Calculating +x and -x for y=0')
    print('x = -b +- sqrt(b^2 - 4ac)/2a')
    b2 = b**2
    ac4 = 4*a*c
    print('x = ' + str(nb) + '+-sqrt(' + str(b2) + '-' + str(ac4) + ')/' + str(a2))
    sr = math.sqrt(b2 - ac4)
    print('x = ' + str(nb) + '+-' + str(sr) + ' / ' + str(a2))
    print('-x =' + str(nb) + ' - ' + str(sr) + ' / ' + str(a2))
    print('+x = ' + str(nb) + '+' + str(sr) + ' / ' + str(a2))
    posx = (nb + sr)/a2
    negx = (nb - sr)/a2

    print('-x = ' + str(negx))
    print('+x = ' + str(posx))

    print('\n Plotting the parabola')

    df = pd.DataFrame({'x': range(round(vx) - 10, round(vx) + 10)})
    df['y'] = a*df['x']**2 + b*df['x'] + c
    miny = df.y.min()
    maxy = df.y.max()

    plt.plot(df.x, df.y, color='grey')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.axvline()
    plt.axhline()
    # Plot calculated x values for y = 0
    plt.scatter([negx, posx], [0,0], color='green')
    plt.annotate('-x=' + str(negx) + ',' + str(0), (negx, 0), xytext=(negx - 3, 5))
    plt.annotate('+x=' + str(posx) + ',' + str(0), (posx, 0), xytext=(posx - 3, -10))
    # plot the line of symmetry

    sx = [vx, vx]
    sy = [miny, maxy]

    plt.plot(sx, sy, color='magenta')
    # Annotate the vertex
    plt.scatter(vx, vy, color='red')
    plt.annotate('v=' + str(vx) + ',' + str(vy), (vx, vy), xytext=(vx - 1, vy - 10))
    plt.show()


print(plot_parabola_from_formula(2, -16, 2))
