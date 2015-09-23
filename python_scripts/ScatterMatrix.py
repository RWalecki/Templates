import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.gridspec as gridspec

def ScatterMatrix(
                    data,
                    bins = 30,
                    title = '',
                    save = None
                 ):

    n = len(data)

    gs = gridspec.GridSpec(n+1,n+1)


    for i in range(n):
        for j in range(n):
            fig = plt.subplot(gs[i, j+1])
            #fig.axis('off')
            fig.axes.get_xaxis().set_visible(False)
            fig.axes.get_yaxis().set_visible(False)
            x = data[i]
            y = data[j]

            if i == j:
            #########################################################
            # diagonal elements:
            # 1D histograms showing the marginals
            #########################################################
                plt.hist(
                        x,
                        bins = np.linspace(data.min(),data.max(),bins),
                        normed=1,
                        facecolor='green',
                        )
                ratio_default=(fig.get_xlim()[1]-fig.get_xlim()[0])/(fig.get_ylim()[1]-fig.get_ylim()[0])
                fig.set_aspect(ratio_default)
            #########################################################

            if i < j:
            #########################################################
            # Correlation:
            # Color shows the correlation
            #########################################################
                cor = np.corrcoef(x,y)[0,1]
                tmp = np.ones((3,3))*cor
                txt = str(np.round(cor*100)/100)
                plt.imshow(tmp,vmin=-1, vmax=1)
                fig.text(1,1,txt,ha="center", va="center")
            #########################################################

            if i > j:
            #########################################################
            # 2D scatter plot:
            # shows the distribution
            #########################################################
                plt.scatter(x,y)
                ratio_default=(fig.get_xlim()[1]-fig.get_xlim()[0])/(fig.get_ylim()[1]-fig.get_ylim()[0])
                fig.set_aspect(ratio_default)
            #########################################################

            plt.suptitle(title)


    plt.tight_layout()
    if save:
        plt.savefig(save)
    else:
        plt.show()
