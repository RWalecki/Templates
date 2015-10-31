import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.patches import Rectangle
from matplotlib.colors import LogNorm



def plot_corr_mat(
    corr_mat,
    xname = None,
    xlabel= '',
    highlight = None,
    trashold = 0,
    path = '/tmp/test.pdf',
):
    fig, ax = plt.subplots()
    corr_mat[np.abs(corr_mat)<trashold]=0
    col = np.copy(corr_mat)
    #col[corr_mat<0]=1
    #col[corr_mat>0]=-1
    #for i in range(col.shape[0]):
        #for j in range(col.shape[0]):
            #if i>=j:col[i,j]=0
    v_max = np.max(np.abs(col))
    plt.imshow(col.T,
               interpolation='nearest',
               cmap=cm.seismic,
               vmin=-v_max, vmax=v_max
               )


    N = corr_mat.shape[1]
    if xname == None:
        xname = range(N)

    ax.set_xticklabels( xname )
    ax.set_xticks( range(N) )
    ax.set_xlabel(xlabel,fontsize=22)

    ax.set_yticklabels( xname )
    ax.set_yticks( range(N) )
    ax.set_ylabel(xlabel,fontsize=22)

    plt.tick_params(axis='both', which='major', labelsize=16)

    min_val, max_val = 0, corr_mat.shape[0]
    ind_array = np.arange(min_val, max_val, 1.0)
    x, y = np.meshgrid(ind_array, ind_array)

    for i, (x_val, y_val) in enumerate(zip(x.flatten(), y.flatten())):
        #if x_val>=y_val:continue
        val = corr_mat[x_val,y_val]
        if val==0:continue
        c = np.int32(val*100)/100.
        if val<=-0.4:
            ax.text(x_val, y_val, c, va='center', ha='center',size=10,color='white')
        else:
            ax.text(x_val, y_val, c, va='center', ha='center',size=10,color='black')


    if highlight!=None:
        for i1,i2 in highlight:
            #if i2>=i1:continue
            ax.add_patch(Rectangle((i2-0.5, i1-0.5), 1, 1, fill=None, alpha=1,linewidth=4,color='k'))
    for i1 in range(col.shape[0]):
        for i2 in range(col.shape[0]):
            #if i2>=i1:continue
            ax.add_patch(Rectangle((i2-0.5, i1-0.5), 1, 1, fill=None, alpha=1,linewidth=0.5,color='k'))



    plt.savefig(path,bbox_inches='tight')

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
