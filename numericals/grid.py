    
import numpy as np

def Grid (s_min, s_max, m, T, n):
    
    z_min = np.log(s_min)
    z_max = np.log(s_max)

    z = np.linspace(z_min, z_max, m + 1)

    delta_z = (z_max - z_min) / (m)

    s = np.exp(z)
    
    t = np.linspace(0.0, T, n+1)
    delta_t = T / n
    
    return s, z, delta_z, t, delta_t


    