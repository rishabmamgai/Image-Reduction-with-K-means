from data import load_data
import matplotlib.pyplot as plt
import numpy as np


def plot_features():
    X = load_data("features.mat")
    X = np.array(X)


    plt.scatter(X[:, 0], X[:, 1])
    plt.show()


def plot_clusters(X, cluster_loc, centroids):
    
    for i in range(len(X)):
        flag = False

        for j in range(len(centroids)):
            if(X[i][0] == centroids[j][0] and X[i][1] == centroids[j][1]):
                plt.scatter(X[i, 0], X[i, 1], c="black", marker="X")
                flag = True
                break

        if flag == False:
            if(cluster_loc[i] == 0):
                plt.plot_date(X[i, 0], X[i, 1], c="pink")
            
            elif(cluster_loc[i] == 1):
                plt.plot_date(X[i, 0], X[i, 1], c="blue")

            elif(cluster_loc[i] == 2):
                plt.plot_date(X[i, 0], X[i, 1], c="green")

    plt.show()


        
