import numpy as np

def sigmoid(x):
   scaler = np.array(x)

   result = 1/(1+np.exp(-scaler))

   return result
 