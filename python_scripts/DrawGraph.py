import daft
import matplotlib.pyplot as plt
import numpy as np
def DrawGraph(Np,Ep=None,name=None,save=None):
    pgm = daft.PGM([8, 8],
                   origin=[-4, -4],
                   directed=False,
                   node_unit=1,
                   grid_unit=1,
                   aspect=1,
                   node_ec=[0,0,0],
                   )
    N = Np.shape[0]
    alpha = np.linspace(0,2*np.pi,N+1)[:-1]

    for i,a in enumerate(alpha):

        x = np.cos(a+np.pi/2)*3.3
        y = np.sin(a+np.pi/2)*3.3

        if name:
            label = name[i]
        else:
            label = str(i)

        pgm.add_node(daft.Node(i, label, x, y,observed=False))

    if Ep:
        for e1,e2 in Ep:
            pgm.add_edge(e1, e2)

    pgm.render()
    if save:
        plt.savefig(save)
    else:
        plt.show()
