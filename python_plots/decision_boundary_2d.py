import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def decision_boundary_2d(X,
                         y,
                         fun,
                         path='/tmp/test.png',
                         title='',
                         ylabel = '',
                         xlabel = '',
                         ylim = [],
                         legend_size = 12,
                         legend_loc = 1,
                         ):
    h = 0.01
    c_map = cm.Spectral_r(np.linspace(0, 1, 3))

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),np.arange(y_min, y_max, h))
    decision = fun(np.c_[xx.ravel(), yy.ravel()])
    decision = decision.reshape(xx.shape)
    #plt.axis('off')

    fig, ax = plt.subplots()

    #Plot also the training points
    plt.contourf(xx, yy, decision,cmap=cm.Spectral_r)
    plt.colorbar()
    plt.scatter(X[:, 0], X[:, 1], c=y,cmap=cm.Spectral_r,s=200)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.yaxis.grid()
    ax.xaxis.grid()
    ax.set_title(title)
    plt.savefig(path, bbox_inches='tight')


if __name__ == "__main__":

    x1 = np.random.rand(10,2)+[1,1]
    x2 = np.random.rand(10,2)-[0,0]
    y1 = 1*np.ones(10)
    y2 = 2*np.ones(10)
    X = np.concatenate((x1,x2))
    y = np.concatenate(([y1],[y2]),1).T
    def fun(x):
        w = np.array([1,1])
        b = -2
        lab = ((np.sum((x**3)*np.tile(w,(x.shape[0],1)),1)+b)<0).astype('int16')
        return lab

    decision_boundary_2d(X,y,fun,xlabel='X-feature',ylabel='y-feature')

