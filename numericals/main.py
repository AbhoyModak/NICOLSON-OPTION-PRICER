import numpy as np

from boundary import get_boundaries
from coefficients import Coefficients
from grid import Grid
from matrix import Matrix
from payoff import get_payoff
from rhs import Build_rhs
from solver import Solver


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

def run_option(
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
):
    
S, Z, delta_z, time, delta_t = Grid(
    S_min,
    S_max,
    M,
    T,
    N
)

(
    alpha,
    beta,
    gamma,
    alpha_rhs,
    beta_rhs,
    gamma_rhs
) = Coefficients(
    delta_z,
    delta_t,
    sigma,
    r,
    q
)


matrix = Matrix(
    alpha,
    beta,
    gamma,
    M
)

known_row = get_payoff(
    option_type,
    S,
    K
)

for i in range(N - 1, -1, -1):

    t_current = i * delta_t

    lower_boundary, upper_boundary = get_boundaries(
        option_type,
        S_max,
        K,
        r,
        T,
        t_current
    )

    rhs = Build_rhs(
        known_row,
        alpha,
        gamma,
        alpha_rhs,
        beta_rhs,
        gamma_rhs,
        lower_boundary,
        upper_boundary
    )

    current_values = Solver(
        matrix,
        rhs
    )

    if option_style == "american":
        exercise_payoff = get_payoff(
            option_type,
            S[1:-1],
            K
        )
        current_values = np.maximum(current_values, exercise_payoff)
        
    current_row = np.concatenate(
        (
            [lower_boundary],
            current_values,
            [upper_boundary]
        )
    )

    known_row = current_row


price = np.interp(
    S0,
    S,
    known_row
)

print()
print("OPTION TYPE: ", option_type)
print("OPTION STYLE: ", option_style)
print("OPTOIN PRICE: ", price)