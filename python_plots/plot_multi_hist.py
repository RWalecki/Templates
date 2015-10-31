import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def plot_multi_hist(X,y,
               title='',
               ylabel = '',
               xlabel = '',
               legend_size = 12,
               legend_loc = 1,
               legend_title = None,
               ):

    c_map = cm.rainbow(np.linspace(0, 1, len(np.unique(y))))
    x0 = X.mean()-3*X.std()
    x1 = X.mean()+3*X.std()
    if x0<X.min():x0=X.min()
    if x1>X.max():x1=X.max()
    labels = np.unique(y)
    bins = np.linspace(x0, x1, 50)

    for i in labels:
        print i
        x_ = X[y==i]
        plt.hist(x_,bins=bins,alpha=0.75,color = c_map[i])
    plt.xlim([x0,x1])
    plt.xlabel(xlabel,fontsize=22)
    plt.ylabel(ylabel,fontsize=22)
    legend = plt.legend(labels,
                       fontsize=16,
                       loc = legend_loc,
                       title=legend_title,
                       ncol=2,
                       fancybox=True, shadow=False)
    plt.tick_params(axis='both', which='major', labelsize=16)

    legend.get_title().set_fontsize(22)
