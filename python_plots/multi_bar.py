import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def multi_bar(data,
               m_name='',
               s_name='',
               title='',
               ylabel = '',
               xlabel = '',
               ylim = [],
               legend_size = 12,
               legend_loc = 1,
               path='/tmp/test.png'
               ):

    # initial number of groups, sup groups and colormap
    ##########################################################################
    n_s, n_m = data.shape
    c_map = cm.Spectral_r(np.linspace(0, 1, 20))
    ##########################################################################


    # the x locations for the groups
    ##########################################################################
    ind = np.arange(data.shape[1])
    ##########################################################################


    # the width of the bars, fill 80% of the area and let 20% for spaces
    # between main groups
    ##########################################################################
    width = (n_m/float(n_s * n_m))*0.8
    ##########################################################################


    # generate all the bar plots
    ##########################################################################
    fig, ax = plt.subplots()
    width_runner = 0;
    rects = []
    for idx,i in enumerate(data):
        rects.append(ax.bar(ind+width_runner, i, width, color=c_map[idx]))
        width_runner+=width
    ##########################################################################


    # add some text for labels, title and axes ticks
    ##########################################################################
    ax.set_ylabel(ylabel)
    ax.yaxis.grid()
    ax.set_xlabel(xlabel)
    ax.set_title(title)
    ax.set_xticks(ind+width*n_s/2)
    ax.set_xticklabels( m_name )
    if ylim!=[]:ax.set_ylim(ylim)
    ax.legend( rects, s_name ,fontsize=legend_size,loc = legend_loc)
    ##########################################################################

    plt.savefig(path, bbox_inches='tight')


if __name__ == "__main__":

    dat = np.random.rand(10,5)
    m_name = np.array(['m_'+str(i) for i in range(10)])
    s_name = np.array(['s_'+str(i) for i in range(5)])


    multi_bar(
        data = dat,
        title = 'Title',
        ylabel = 'Y-Axis',
        xlabel = 'X-Axis',
        ylim = [0,2],
        m_name = m_name,
        s_name = s_name,
        legend_size = 12,
        legend_loc = 1,
    )
