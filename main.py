from model import distortion_function, Kmeans
from extract_image import get_pixel_mat, get_image
from visualize import plot_clusters
import numpy as np
import data


file = "features.mat"
X = data.load_data(file)

K = 3
iters = 50
#final_centroids, final_cluster_loc, final_distortion = run_Kmeans(X, K, iters)

#print(final_distortion)
#plot_clusters(X, final_cluster_loc, final_centroids)


pixel_mat = get_pixel_mat("image\original.jpg")
final_centroids, final_cluster_loc, final_distortion = Kmeans(pixel_mat, K, iters)

X_recovered = []

for i in range(len(final_cluster_loc)):
    X_recovered.append(final_centroids[final_cluster_loc[i]])


get_image(np.array(X_recovered) * 255)

plot_clusters(pixel_mat, final_cluster_loc, final_centroids)
