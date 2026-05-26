import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):
    scores_shape = scores.shape[-1]

    mask = np.triu(np.ones((scores_shape, scores_shape)),k=1)

    scores = np.where(mask == 1, mask_value, scores)

    return scores
    