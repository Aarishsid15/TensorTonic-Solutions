import numpy as np

def dropout(x, p=0.5, rng=None):
    arr = np.array(x)

    # handle edge case
    if p == 0:
        mask = np.ones(arr.shape)
        return arr, mask

    flat = arr.flatten()
    n = len(flat)

    if rng is not None:
        rand = rng.random(n)
    else:
        rand = np.random.random(n)

    mask = (rand > p).astype(int)

     # scaled output
    scaled_output = (flat * mask) / (1 - p)

    # scaled mask
    scaled_mask = mask / (1 - p)

    # reshape
    scaled_output = np.reshape(scaled_output, arr.shape)
    scaled_mask = np.reshape(scaled_mask, arr.shape)

    return scaled_output, scaled_mask
        