import numpy as np

def Matrix(alpha, beta, gamma, M):
    matrix = np.zeros((M - 1, M - 1))

    for i in range(M - 1):
        matrix[i, i] = beta
        
        if i > 0:
            matrix[i, i - 1] = alpha
        if i < M - 2:
            matrix[i, i + 1] = gamma
    
    return matrix
