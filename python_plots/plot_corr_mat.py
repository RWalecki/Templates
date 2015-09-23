import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
def plot_corr_mat(
    data,
    xname = None,
    xlabel= '',
    path = '/tmp/test.pdf'
):
    corr = np.corrcoef(data)
    fig, ax = plt.subplots()
    plt.imshow(corr,interpolation='none',cmap=cm.Spectral_r)
    N = corr.shape[1]
    if xname == None:
        xname = range(N)

    ax.set_xticklabels( xname )
    ax.set_xticks( range(N) )
    ax.set_xlabel(xlabel)

    ax.set_yticklabels( xname )
    ax.set_yticks( range(N) )
    ax.set_ylabel(xlabel)

    for x in range(corr.shape[0]):
        for y in range(corr.shape[1]):
            plt.text(x-0.33, y+0.1, np.int8(corr[x,y]*100)/100.,size=10)

    plt.savefig(path)
