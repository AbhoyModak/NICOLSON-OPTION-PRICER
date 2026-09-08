import numpy as np

def Solver(matrix, rhs):
    current_values = np.linalg.solve(matrix, rhs)
    
    return current_values