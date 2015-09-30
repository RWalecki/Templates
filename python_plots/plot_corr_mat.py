import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def plot_corr_mat(
    corr_mat,
    xname = None,
    xlabel= '',
    trashold = 0,
    path = '/tmp/test.pdf',
):
    fig, ax = plt.subplots()
    corr_mat[np.abs(corr_mat)<trashold]=0
    v_max = np.max(np.abs(corr_mat))
    plt.imshow(corr_mat.T,
               interpolation='nearest',
               cmap=cm.seismic,
               vmin=-v_max, vmax=v_max
               )
    N = corr_mat.shape[1]
    if xname == None:
        xname = range(N)

    ax.set_xticklabels( xname )
    ax.set_xticks( range(N) )
    ax.set_xlabel(xlabel)

    ax.set_yticklabels( xname )
    ax.set_yticks( range(N) )
    ax.set_ylabel(xlabel)

    min_val, max_val = 0, corr_mat.shape[0]
    ind_array = np.arange(min_val, max_val, 1.0)
    x, y = np.meshgrid(ind_array, ind_array)

    for i, (x_val, y_val) in enumerate(zip(x.flatten(), y.flatten())):
        val = corr_mat[x_val,y_val]
        if val==0:continue
        c = np.int8(val*100)/100.
        ax.text(x_val, y_val, c, va='center', ha='center',size=10)
    plt.savefig(path)


if __name__ == "__main__":
    C = (np.random.rand(10,10)*2)-1
    prune_factor = 0.7

    for x in range(C.shape[0]):
        for y in range(C.shape[1]):
            if x==y:continue
            if np.random.rand()>prune_factor:continue
            C[x,y]=0

    plot_corr_mat(
        corr_mat=C,
        xname = [1,2,3,4,5,6,7,8,-9,100]
    )
