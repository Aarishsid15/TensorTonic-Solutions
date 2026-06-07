import numpy as np

def softmax(x):
    x = np.array(x)
    if x.ndim == 1:
        expo = np.exp(x - np.max(x))
        result = expo / np.sum(expo)
        return result                
    else:                 
        expo = np.exp(x - np.max(x, axis=1, keepdims=True))
        result = expo / np.sum(expo, axis=1, keepdims=True)
        return result 

    