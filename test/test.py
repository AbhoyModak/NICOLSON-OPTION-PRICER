import numpy as np
from scipy.stats import norm



import sys
from pathlib import Path


numericals_path = Path(__file__).resolve().parent.parent / 'numericals'

sys.path.append(str(numericals_path))

from main import run_option

S_min = 20
S_max = 300
S0 = 100

K = 100

r = 0.10
q = 0.0
sigma = 0.20

T = 1.0

N = 200
M = 200

option_type = input("PUT / CALL: ").lower()
option_style = input("EUROPEAN / AMERICAN: ").lower()

def black_scholes(option_type, S0, K, sigma, r, T):
    
    d1 = (
        (np.log(S0 / K)
        + ((r + 0.5 * (sigma ** 2) * T)) / (sigma * np.sqrt(T)))
    )
        
    d2 = d1 - (sigma * np.sqrt(T))
    
    if option_type == "call":
        price = (
            S0 * norm.cdf(d1) 
            - ((K * np.exp(-r * T)) * norm.cdf(d2))
        )
        
    elif option_type == "put":
        price = (
            (K * np.exp(-r * T) * norm.cdf (-d2) - (S0 * norm.cdf (-d1)))
        )
        
    else:
        raise ValueError("OPTION MUST BE 'CALL' OR 'PUT'")
    
    return price


bs_price = black_scholes(
    option_type,
    S0,
    K,
    sigma,
    r,
    T
)


option_type, option_style, cn_price = run_option(
    S_min,
    S_max,
    S0,
    K,
    r,
    q,
    sigma,
    T,
    N,
    M,
    option_type,
    option_style
)

error = abs(cn_price - bs_price)

print()
print ("BLACK SCHOLES PRICE: ", bs_price)
print("CN OPTION PRICE: ", cn_price)
print("ERROR: ", error)