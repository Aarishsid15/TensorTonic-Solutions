import numpy as np

def entropy_node(y):
    y = np.array(y)
    value,counts = np.unique(y, return_counts=True)
    p = counts/len(y)

    log = np.log2(p)
    result = np.dot(p,log)

    return abs(result)
    
    

    