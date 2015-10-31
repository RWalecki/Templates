import numpy as np
import matplotlib.pyplot as plt

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
               legend_title = None,
               path='/tmp/test.pdf'
               ):

    fig, ax = plt.subplots()
    classes = np.unique(data)

    #c_map = cm.Spectral_r(np.linspace(0, 1, len(classes)*2))
    c_map = cm.rainbow(np.linspace(0, 1, len(classes)))
    for i in classes[::-1]:
        tmp = np.sum(data<=i,1)
        plt.bar(range(len(tmp)),tmp,color=c_map[i])


    ax.set_xticklabels( xname ,fontsize=18)
    ax.set_xticks( np.arange(len(xname))+0.4 )
    plt.grid(True)
    plt.tick_params(axis='both', which='major', labelsize=16)
    ax.set_xlabel(xlabel,fontsize=22)
    ax.set_ylabel(ylabel,fontsize=22)
    box = ax.get_position()

    # Put a legend to the right of the current axis
    # ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    legend = ax.legend(classes[::-1],
                       fontsize=legend_size,
                       loc = legend_loc,
                       title=legend_title,
                       ncol=2,
                       fancybox=True, shadow=False)
    legend.get_title().set_fontsize(legend_size*1.2)
    #plt.savefig(path)
    #ax.set_position([box.x0, box.y0, box.width, box.height])
    plt.savefig(path,bbox_inches='tight')




if __name__ == "__main__":

    dat = np.random.randint(0,7,(10,10))
    label_distribution(
        dat,
        xname=[1,2,3,4,5,666,7,8,999,10],
        xlabel='AUs',
        ylabel='# - active',
    )



