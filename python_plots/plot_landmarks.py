import matplotlib.pyplot as plt
def plot_landmarks(X):
    mean_face = X.mean(0)

    plt.scatter(X[:,1,:], -X[:,0,:], alpha=0.002,color='g')
    plt.scatter(mean_face[1], -mean_face[0], alpha=1,color='r')
    plt.show()
