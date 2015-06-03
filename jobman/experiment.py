from sklearn import linear_model, datasets
from jobman.tools import DD, flatten
import numpy as np
def sk_log_reg(state, channel):
    iris = datasets.load_iris()

    X = iris.data[:, :]  # we only take the first two features.
    Y = iris.target


    l2 = state.l2+state.second
    logreg = linear_model.LogisticRegression(penalty='l2',C=l2)

    logreg.fit(X, Y)
    y_hat = logreg.predict(X)
    acc = np.mean(y_hat==Y)
    state.result = acc
    print 'result =', state.result

    return channel.COMPLETE
