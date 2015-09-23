from DrawGraph import DrawGraph
from ScatterMatrix import ScatterMatrix





if __name__ == "__main__":
    import itertools
    N = 6
    n = np.random.rand(N,6)
    name = [
        '$AU_1$',
        '$AU_2$',
        '$AU_4$',
        '$AU_6$',
        '$AU_{12}$',
        '$AU_{20}$',
    ]
    e = []
    for i in itertools.combinations(range(N),2):e.append(i)
    DrawGraph(n,e,name,save='/tmp/tmp.pdf')
