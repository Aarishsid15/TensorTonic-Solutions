import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    X = np.array(X)
    
    min = np.min(X, axis=axis, keepdims=True)
    max = np.max(X, axis=axis, keepdims=True)

    subtract = max-min

    denominator = np.maximum(subtract, eps)

    return (X-min)/denominator

    
    