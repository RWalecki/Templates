from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def applyPCA(X,n):
    print 'applying PCA:'
    pca = PCA(n_components=n)
    pca.fit(X)
    print sum(pca.explained_variance_ratio_)
    return pca.fit_transform(X)

def features_2d(X,
                y,
                path = '/tmp/feat.png'):

    X = applyPCA(X,2)
    for i in range(y.shape[1]):
        plt.subplot(2, 2, i+1)
        plt.title('Group-'+str(i+1))
        plt.scatter(X[:, 0], X[:, 1], c=y[:,i],cmap=cm.Spectral_r,s=100)
    plt.savefig(path)

def covariance_lables(y,
                      path = '/tmp/Cov.png'):

    cov_mat = np.cov(y.T)
    fig, ax = plt.subplots()
    plt.imshow(cov_mat, interpolation='nearest',cmap=cm.Spectral_r)
    plt.title('Covariance Matrix')
    ax.set_xticks(range(y.shape[1]))
    ax.set_xticklabels(np.arange(y.shape[1])+1)
    ax.set_yticks(range(y.shape[1]))
    ax.set_yticklabels(np.arange(y.shape[1])+1)
    plt.colorbar()
    plt.savefig(path)
