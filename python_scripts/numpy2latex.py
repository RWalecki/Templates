import pandas as pd
import numpy as np

def np2tex(dat, xlabel = None, ylabel = None, path = '/tmp/test.tex' ):
    '''
    how to use in latex:

        \documentclass{article}
        \usepackage{booktabs}
        \begin{document}
            \input{./table.tex}
        \end{document}

    '''

    # define precision
    def format(x):return str(np.int8(x*100)/100.)

    tab = pd.DataFrame(dat,index=xlabel,columns=ylabel)
    tab.to_latex(buf=path,float_format=format)
