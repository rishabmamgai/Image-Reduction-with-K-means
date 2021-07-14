from numpy.lib.npyio import load
from scipy.io import loadmat
from random import randint


def load_data(file):
    features = loadmat(file)
    
    return features['X']


def initialize_centroids(X, K):
    centroids = []

    while range(K):
        i = randint(0, len(X)-1)
        centroids.append(X[i][:])
        K -= 1

    return centroids

