"""
https://stackabuse.com/k-means-clustering-with-scikit-learn/
https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
"""


import matplotlib.pyplot as plt  
import numpy as np  
from sklearn.cluster import KMeans  


# The toy 2D dataset that I want to cluster. 
X = np.array([[5,3], [10,15], [15,12], [24,10], [30,45], [85,70], [71,80], [60,78], [55,52], [80,91],])


def view_data():
    """
    pyplot.scatter(
        x: all of the x values. Any array-like object will do (e.g. a list, a numpy array)
        y: all of the associated y values. Same type requirements as x
        label: 
    )
    """
    # He's using muti-axis (i.e. multidimensional) slicing here. What is the label argument?
    plt.scatter(X[:,0],X[:,1], label='True Position')  
    plt.show()
    plt.close()


def run_k_means():
    km = KMeans(n_clusters=2)
    km.fit(X)
    print(km.cluster_centers_)
    # Print out the cluster that was assigned to each data point. There were 10 data points, so there are 10 elements in this array. There were only
    # two clusters, so each element in the array can only have 1 of 2 values
    print(km.labels_) 
    # The 'c' parameter is for the marker color to apply to each data point. The cluster_centers_ output is such that using this label for this
    # purpose makes sense
    plt.scatter(X[:,0], X[:,1], c=km.labels_, cmap='rainbow')
    plt.scatter(km.cluster_centers_[:,0] ,km.cluster_centers_[:,1], color='black')  
    plt.show()


if __name__ == "__main__":
    #view_data()
    run_k_means()