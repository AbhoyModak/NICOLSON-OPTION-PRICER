import numpy as np

def Build_rhs (known_row, alpha, gamma, alpha_rhs, beta_rhs, gamma_rhs, lowerBoundary, upperBoundary) :
    
    no_of_r = len(known_row) - 2
    rhs = np.zeros(no_of_r)
    
    for j in range(1, no_of_r + 1):
        
        rhs[j - 1] = ((alpha_rhs * known_row[j - 1]) + (beta_rhs * known_row[j]) + (gamma_rhs * known_row[j + 1]))
    
        if j == 1 :
            rhs[j - 1] = rhs[j - 1] - (alpha * lowerBoundary)
            
        if j == no_of_r:
            rhs[j - 1] = rhs[j - 1] - (gamma * upperBoundary)
            

    return rhs