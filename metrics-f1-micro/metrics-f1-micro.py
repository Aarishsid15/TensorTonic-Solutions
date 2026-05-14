import numpy as np
def f1_micro(y_true, y_pred) -> float:
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

      # Count correct predictions
    TP = np.sum(y_true == y_pred)
    
    # Count wrong predictions
    FP = np.sum(y_true != y_pred)
    
    FN = np.sum(y_true != y_pred)
    
    # Micro F1 Score
    f1_micro = (2 * TP) / (2 * TP + FP + FN)

    return f1_micro
    
        
    

    