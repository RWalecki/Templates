import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def ScatterMatrix(
                    data,
                    bins = 30,
                    title = '',
                    save = None
                 ):

    n = len(data)

    for i in range(n):
        for j in range(n):
            fig = plt.subplot2grid((n,n),(i, j))
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
                fig.set_aspect('equal', 'datalim')
                plt.axis('scaled')
            #########################################################

            if i > j:
            #########################################################
            # 2D scatter plot:
            # shows the distribution
            #########################################################
                plt.scatter(x,y)
            #########################################################
            plt.suptitle(title)

    if save:
        plt.savefig(save)
    else:
        plt.show()
