import pandas as pd
import numpy as np
form numpy2latex import *

dat = np.random.rand(3,6)
ylabel = [1, 2, 4, 6, 8, 12]
xlabel = ['mlr','sor','cor']
np2tex(dat,xlabel,ylabel,'./build/table.tex')
