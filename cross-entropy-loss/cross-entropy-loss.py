import numpy as np

def cross_entropy_loss(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    log_loss = -np.mean(np.log(y_pred[np.arange(len(y_true)), y_true]))

    return log_loss