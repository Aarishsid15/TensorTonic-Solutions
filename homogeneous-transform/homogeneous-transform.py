import numpy as np

def apply_homogeneous_transform(T, points):
    points = np.array(points)
    T = np.array(T)
    if np.ndim(points) == 1:
        homogenious_points = np.hstack((points,1))
        transform = T @ homogenious_points

        return transform[:3]
    else:
        ones = np.ones((points.shape[0], 1))
        homogenious_points = np.hstack((points,ones))

        tranform = (T @ homogenious_points.T).T

        return tranform[: , :3]