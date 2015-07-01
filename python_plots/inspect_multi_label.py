import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import itertools

def bla():pass

def inspect_multi_label(y,
               m_name='',
               s_name='',
               title='',
               ylabel = '',
               xlabel = '',
               path='/tmp/test.png'
               ):
    print y
    cov = np.cov(y.T)

    res = {}

    # loop over all possible combinations of models
    for i,j in itertools.combinations(range(y.shape[1]),2):
        a1 = y[:,i]
        a2 = y[:,j]
        u = np.unique((a1,a2))
        tmp = np.zeros((len(u),len(u)))

        #loop over all possible combination of classes
        for k in u:
            for l in u:
                x_i = np.where(u==k)[0][0]
                y_i = np.where(u==l)[0][0]
                # compute coocurance of model-combination i,j and class-combination l,k
                # in temporar matrix tmp
                tmp[x_i,y_i] = np.sum(a1[a2==l]==k)
        tmp = tmp/float(y.shape[1])

        #save coocurance matrix
        res[i,j] = tmp

    fig, ax = plt.subplots()
    a = 0;
    for i in res:
        a+=1;
        plt.subplot(y.shape[1], (y.shape[1])/2, a)
        plt.imshow(res[i],interpolation='none',cmap=cm.Spectral_r)
        plt.gca().xaxis.set_major_locator(plt.NullLocator())
        plt.gca().yaxis.set_major_locator(plt.NullLocator())
        plt.title('class: '+str(i[0])+' and '+str(i[1]))
    plt.imshow(cov,interpolation='none',cmap=cm.Spectral_r)
    plt.show()



if __name__ == "__main__":
    pass

    #100 frames
    #5 models
    #10 classes
    dat = np.random.randint(0,10,(100,5))

    #everything should be random
    inspect_multi_label(dat)
