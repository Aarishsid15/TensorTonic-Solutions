import numpy as np

def matrix_transpose(A):
        m = len(A[0])
        n = len(A)
        res_matrix = np.zeros((m,n))

        for i in range(m):
            for j in range(n):
                res_matrix[i][j] = A[j][i]

        return res_matrix
       
