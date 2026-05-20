import numpy as np

def euclidean_distance(x, y):
    x = np.array(x)
    y = np.array(y)

    distance = np.sqrt(np.sum((x-y)**2))

    return distance