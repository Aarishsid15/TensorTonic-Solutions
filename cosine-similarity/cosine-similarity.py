import numpy as np

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    dot_Product = np.dot(a,b)
    norms_a = np.linalg.norm(a)
    norms_b = np.linalg.norm(b)
    if norms_a  == 0 or norms_b == 0:
        return 0.0
    else:
        return dot_Product/np.dot(norms_a, norms_b)
   