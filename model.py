from scipy.spatial import distance as dist
from data import initialize_centroids
import numpy as np
from sys import maxsize
from math import sqrt


def Kmeans(X, K, iters):
    final_centroids = 0
    final_cluster_loc = 0
    final_distortion = maxsize

    for i in range(iters):
        print(f"iters - {i+1}")

        centroids = initialize_centroids(X, K)
        cluster_loc = findCentroid(X, K, centroids)
        distortion = distortion_function(X, centroids, cluster_loc)

        if distortion < final_distortion:
            final_centroids = centroids
            final_cluster_loc = cluster_loc
            final_distortion = distortion
    
    return np.array(final_centroids), np.array(final_cluster_loc), np.array(final_distortion)


def findCentroid(X, K, centroids):
    centroid_loc = []

    for i in range(len(X)):
        min = maxsize
        min_idx = len(X)

        # Find dist b/w feature vector and centroid
        for j in range(K):
            vec_len = sqrt(dist.euclidean(X[i], centroids[j]))

            if(vec_len < min):
                min = vec_len
                min_idx = j

        centroid_loc.append(min_idx)

    return np.array(centroid_loc)
        

def distortion_function(X, centroids, cluster_loc):
    m = len(X)
    distortion = 0

    for i in range(m):
        vec_len = sqrt(dist.euclidean(X[i], centroids[cluster_loc[i]]))

        distortion += vec_len

    return distortion / m

