import numpy as np

def expected_value_discrete(x, p):
    x = np.array(x)
    p = np.array(p)
    
    if not np.isclose(np.sum(p),1.0):
        raise ValueError
    else:
        expected_value = np.dot(x,p)
        return expected_value