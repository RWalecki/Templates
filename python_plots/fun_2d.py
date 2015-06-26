import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

def Copula2d(C,
            marginals_1,
            marginals_2,
            path='/tmp/test.png',
            title='',
            ylabel = '',
            xlabel = '',
            ylim = [0,1],
            xlim = [0,1]
           ):
    c_map = cm.Spectral_r(np.linspace(0, 1, 3))
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

    fig = plt.figure()
    cdf_1 = np.cumsum(marginals_1)
    cdf_2 = np.cumsum(marginals_2)

    ax = fig.add_subplot(221)
    plt.pcolor(X, Y, Z, cmap='jet')
    plt.colorbar()
    CS = plt.contour(X, Y, Z, cmap='jet')
    plt.clabel(CS, inline=1, fontsize=18)
    zc = CS.collections[:]
    plt.setp(zc, linewidth=4)
    plt.axis(np.hstack((xlim,ylim)))
    ax.set_xlabel('u = CDF(margin_1)')
    ax.set_ylabel('v = CDF(margin_2)')
    ax.set_title('Copula')
    for i in cdf_1:plt.axvline([i], color='r')
    for i in cdf_2:plt.axhline([i], color='r')

    ax = fig.add_subplot(222)
    ax.set_title('marginals_1 (u)')
    ax.bar(np.arange(len(marginals_1)),cdf_1,color='r')
    ax.bar(np.arange(len(marginals_1)),marginals_1)
    ax.set_ylim([0,1])

    ax = fig.add_subplot(223)
    ax.set_title('marginals_2 (v)')
    ax.bar(np.arange(len(marginals_2)),cdf_2,color='r')
    ax.bar(np.arange(len(marginals_2)),marginals_2)
    ax.set_ylim([0,1])

    cdf_1 = np.hstack(([0],cdf_1))
    cdf_2 = np.hstack(([0],cdf_1))
    PRED = np.zeros((len(marginals_1),len(marginals_1)))
    for i in range(len(marginals_1)):
        for j in range(len(marginals_2)):
            x0 = cdf_1[i]
            x1 = cdf_1[i+1]
            y0 = cdf_2[j]
            y1 = cdf_2[j+1]
            X = np.array([
                [x0,y0],
                [x1,y0],
                [x0,y1],
                [x1,y1],
            ])
            res = C(X)
            PRED[i,j] = res[0]-res[1]-res[2]+res[3]

    ax = fig.add_subplot(224)
    im = ax.imshow(PRED, interpolation='nearest')
    plt.colorbar(im)
    plt.savefig(path, bbox_inches='tight')



if __name__ == "__main__":
    def Frank(X,d):
        #return np.prod(X,1)
        A = np.prod( np.exp( -d*X )-1, 1)
        B = np.exp( -d ) - 1
        return -(1/d) * np.log( 1 + A/B )

    def C(X):return Frank(X,-1.9)
    M1 = [0.1, 0.1, 0.2, 0.5, 0.1]
    #M2 = [0.2, 0.2, 0.2, 0.2, 0.2]
    M2 = [0.2, 0.2, 0.2, 0.2, 0.2]

    Copula2d(C,M1,M2,path='/tmp/C.png')
