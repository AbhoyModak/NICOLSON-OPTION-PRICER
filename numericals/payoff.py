import numpy as np

def get_payoff(option_type, S, K):
    
    if option_type == "call" :
        return np.maximum(S - K, 0.0)
    
    if option_type == "put" :
        return np.maximum(K - S, 0.0)
    
    
    