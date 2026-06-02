import numpy as np

def global_avg_pool(x):
    x = np.array(x)
    
    # try:
    if len(x.shape) <= 2:
       raise ValueError("ValueError")
    else:
        size = len(x.shape)    
        result = np.mean(x, axis=(size-2, size-1))
        return result
    # except:
    #     raise ValueError("ValueError")