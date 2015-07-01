import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

def plot_copula(C,
            marginals_1,
            marginals_2,
            path='/tmp/test.png',
            title='',
            ylabel = '',
            xlabel = '',
            ylim = [0,1],
            xlim = [0,1]
           ):


    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    xx, yy = np.meshgrid(x, y, sparse=False)

    n1 = yy.shape[0]
    n2 = yy.shape[1]

    yy = np.reshape(yy,n1*n2)
    xx = np.reshape(xx,n1*n2)
    X = np.vstack((xx,yy)).T
    ZZ = C(X)

    XX = X[:,0]
    YY = X[:,1]
    X = np.reshape(XX,(n1,n2))
    Y = np.reshape(YY,(n1,n2))
    Z = np.reshape(ZZ,(n1,n2))

    cdf_1 = np.cumsum(marginals_1)
    cdf_1 = np.hstack(([0],cdf_1))
    cdf_2 = np.cumsum(marginals_2)
    cdf_2 = np.hstack(([0],cdf_2))

    pred = np.zeros((len(marginals_1),len(marginals_1)))
    for i in range(1,len(cdf_1)):
        for j in range(1,len(cdf_2)):
            x0 = cdf_1[i-1]
            x1 = cdf_1[i]
            y0 = cdf_2[j-1]
            y1 = cdf_2[j]
            x = np.array([
                [x0,y0],
                [x1,y0],
                [x0,y1],
                [x1,y1],
            ])
            res = C(x)
            pred[i-1,j-1] = res[0]-res[1]-res[2]+res[3]

    fig = plt.figure()

    ax = fig.add_subplot(221)
    plt.pcolor(X, Y, Z, cmap='jet')
    plt.colorbar()
    CS = plt.contour(X, Y, Z, cmap='jet')
    plt.clabel(CS, inline=1, fontsize=12)
    zc = CS.collections[:]
    plt.setp(zc, linewidth=4)
    plt.axis(np.hstack((xlim,ylim)))
    ax.set_xlabel('u = CDF(P(x))')
    ax.set_ylabel('v = CDF(P(y))')
    ax.set_title('Copula: C(u,v)')
    for i in cdf_1:plt.axvline([i], color='r',alpha=0.2)
    for i in cdf_2:plt.axhline([i], color='r',alpha=0.2)

    ax = fig.add_subplot(222)
    ax.set_title('Joint Density: c(x,y)')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    im = ax.imshow(pred, interpolation='nearest')
    plt.colorbar(im)
    plt.savefig(path, bbox_inches='tight')




if __name__ == "__main__":
    def Frank(X,d):
        A = np.prod( np.exp( -d*X )-1, 1)
        B = np.exp( -d ) - 1
        return -(1/d) * np.log( 1 + A/B )

    def C(X):return Frank(X,-1.5)
    M1 = np.ones(10)
    M1 = M1/np.sum(M1)
    M2 = np.ones(10)
    M2 = M2/np.sum(M2)

    plot_copula(C,M1,M2,path='/tmp/C.png')
