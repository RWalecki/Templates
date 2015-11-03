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
    plt.xlabel(xlabel,fontsize=33)
    plt.ylabel(ylabel,fontsize=33)

    #plt.legend(
    #loc=3,
                        #ncol=2, mode="expand", borderaxespad=0.)

    legend = plt.legend(labels,
                       fontsize=16,
                        bbox_to_anchor=(0.06, 1, 1.,0),
                       loc = legend_loc,
                       title=legend_title,
                       ncol=5,
                       fancybox=True, shadow=False)
    plt.tick_params(axis='both', which='major', labelsize=33)
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,1))

    legend.get_title().set_fontsize(22)
