import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    lent = len(seqs)
    if max_len is None:
        max_len = max(len(seq) for seq in seqs)
    matrix = np.full((lent,max_len), pad_value)

    
    for i, seq in enumerate(seqs):
        length = min(len(seq), max_len)
        matrix[i, :length] = seq[:length]
        
    return matrix
        
    