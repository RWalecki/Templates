import numpy as np
import matplotlib.pyplot as plt


def fun2d(function_xy,
               x_range = [0,1],
               y_range = [0,1],
               resolution = 100,
               ):

    x_values = np.linspace(x_range[0], x_range[1], resolution)
    y_values = np.linspace(y_range[0], y_range[1], resolution)

    xx, yy = np.meshgrid(x_values,y_values)
    zz = []
    for x,y in zip( xx.ravel(), yy.ravel() ):
        zz.append( function_xy( x, y ) )

    zz = np.array(zz)
    z = zz.reshape(xx.shape)

    pos = np.linspace(0,resolution,5)

    lab_x = x_range[0]+pos/float(resolution)*(x_range[1]-x_range[0])
    plt.xticks(pos,lab_x)

    lab_y = y_range[0]+pos/float(resolution)*(y_range[1]-y_range[0])
    plt.yticks(pos,lab_y)

    plt.imshow(z,origin='lower',interpolation='none')




if __name__ == "__main__":

    def fun(x,y):return x*y
    fun2d(fun)
    plt.show()
