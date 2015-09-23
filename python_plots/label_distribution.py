import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def label_distribution(data,
               m_name='',
               s_name='',
               title='',
               ylabel = '',
               xlabel = '',
               xname = [],
               ylim = [],
               legend_size = 12,
               legend_loc = 1,
               path='/tmp/test.pdf'
               ):

    fig, ax = plt.subplots()
    classes = np.unique(data)

    c_map = cm.Spectral_r(np.linspace(0, 1, len(classes)*2))
    for i in classes[::-1]:
        tmp = np.sum(data<=i,1)
        plt.bar(range(len(tmp)),tmp,color=c_map[i])


    ax.set_xticklabels( xname )
    ax.set_xticks( np.arange(len(xname))+0.4 )
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend(classes[::-1],fontsize=legend_size,loc = legend_loc)
    plt.savefig(path)




if __name__ == "__main__":

    dat = np.random.randint(0,7,(10,10))
    label_distribution(
        dat,
        xname=[1,2,3,4,5,666,7,8,999,10],
        xlabel='AUs',
        ylabel='# - active',
    )



