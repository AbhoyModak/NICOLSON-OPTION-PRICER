import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


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
        ((np.log(S0 / K)
        + ((r + 0.5 * (sigma ** 2) * T))) / (sigma * np.sqrt(T)))
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


option_type, option_style, S, cn_price, cn_values = run_option(
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


# GRAPH 1 - CRANK NICOLSON PRICE VS BLACK SCHOLES PRICE

bs_values = black_scholes(
    option_type,
    S,
    K,
    sigma,
    r,
    T
)


parameter_text = (
    f"OPTION TYPE = {option_style.upper()} {option_type.upper()} \n"
    f"$S_0$ = {S0}\n"
    f"$K$ = {K}\n"
    f"$\\sigma$ = {sigma:0.1%}\n"
    f"$r$ = {r:0.1%}\n"
    f"$K$ = {T}\n"
    
)
 
fig, ax = plt.subplots(figsize = (10, 6), dpi= 150)

ax.plot(
    S,
    cn_values,
    color = '#2B6CB0',
    label = "CRANK NICOLSON",
    linewidth = 2
)

ax.plot(
    S,
    bs_values,
    color = '#1A365D',
    label = "BLACK SCHOLES",
    linewidth = 2
)

ax.set_title("CRANK NICOLSON VS BLACK SCHOLES")
ax.set_xlabel("STOCK PRICE")
ax.set_ylabel("OPTION PRICE")


ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#333333')
ax.spines['bottom'].set_color('#333333')

ax.grid(True, linestyle = "--", alpha = 0.35)

ax.text(
    0.70,
    0.80,
    parameter_text,
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top",
    horizontalalignment = "left",
    bbox=dict(
        boxstyle="round,pad=0.5",
        facecolor="white",
        edgecolor="#CBD5E1",
        alpha=0.9
    )
)

ax.legend(
    loc = 'upper right',
    frameon = True,
    facecolor = "white",
    edgecolor = "none",
    fancybox = True
    
)

plt.tight_layout() 

plt.show()


# GRAPH 2 - NUMERICAL ERROR VS GRID SIZE


M_input = input ("ENTER M VALUES SEPERETED BY SPACE: ")
M_values = [int (x) for x in M_input.split()]

error_plotting = []

for M_test in M_values:
    _, _, _, cn_price_plotting, _ = run_option(
    S_min,
    S_max,
    S0,
    K,
    r,
    q,
    sigma,
    T,
    N,
    M_test,
    option_type,
    option_style
    )
    
    bs_price_plotting = black_scholes(
        option_type,
        S0,
        K,
        sigma,
        r,
        T
    )

    errors = abs(cn_price_plotting - bs_price_plotting)
    error_plotting.append(errors)
    
    
fig_2, ax_2 = plt.subplots(figsize = (10, 6), dpi = 150)

ax_2.plot(
    M_values,
    error_plotting,
    linewidth = 2,
    color = "#007791",
    linestyle = 'dotted'
)

ax_2.set_title ("NUMERICAL ERROR VS GRID SIZE")
ax_2.set_xlabel("M")
ax_2.set_ylabel("ABSOLUTE ERROR")

ax_2.spines['top'].set_visible(False)
ax_2.spines['right'].set_visible(False)
ax_2.spines['left'].set_color('#333333')
ax_2.spines['bottom'].set_color('#333333')

ax_2.legend()

ax_2.grid(
    True,
    linestyle = "--",
    alpha = 0.35
)

ax_2.text(
    0.70,
    0.90,
    parameter_text,
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top",
    horizontalalignment = "left",
    bbox=dict(
        boxstyle="round,pad=0.5",
        facecolor="white",
        edgecolor="#CBD5E1",
        alpha=0.9
    )
)


plt.tight_layout() 
plt.show()
