import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def get_pixel_mat(file):
    image = Image.open(file)
    mat = np.array(image)

    # Reshaping original 3D pixel matrix of image to 2D matrix, where column represents RGB
    pixel_mat = np.reshape(mat, (len(mat)*len(mat), 3), order='C')

    return pixel_mat / 255


def get_image(pixel_mat):
    image = Image.open(r'image\original.jpg')
    mat = np.array(image)
    
    pixel_mat = np.reshape(pixel_mat, (mat.shape[0], mat.shape[1], 3), order='C')

    new_image = Image.fromarray((pixel_mat).astype(np.uint8))
    new_image.save(r'image\new.jpg')


    # Plotting original and new image
    fig = plt.figure(figsize=(1, 2))

    fig.add_subplot(1, 2, 1)
    plt.imshow(image)
    fig.add_subplot(1, 2, 2)
    plt.imshow(new_image)

    plt.show()
