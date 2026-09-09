import numpy as np

def get_boundaries(option_type, option_style, S_max, k, r, T,t):
    
    if option_type == "call": 
        lowerBoundary = 0.00
        upperBoundary = S_max - k * np.exp(-r * (T- t))
    
    elif option_type == "put":
        
        if option_style == "american":
            
            lowerBoundary = k
        else:
            lowerBoundary = k * np.exp(-r * (T- t))
       
        upperBoundary = 0.00
    
    return lowerBoundary, upperBoundary

