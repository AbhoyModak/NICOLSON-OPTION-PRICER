def Coefficients(delta_z, delta_t, sigma, r, q):

    B = (sigma ** 2) / 2
    A = r - q - B

    # LHS matrix coefficients
    alpha = (
        -delta_t * B / (2 * delta_z ** 2)
        + delta_t * A / (4 * delta_z)
    )

    beta = (
        1
        + delta_t * B / (delta_z ** 2)
        + r * delta_t / 2
    )

    gamma = (
        -delta_t * B / (2 * delta_z ** 2)
        - delta_t * A / (4 * delta_z)
    )

    # RHS coefficients
    alpha_rhs = (
        delta_t * B / (2 * delta_z ** 2)
        - delta_t * A / (4 * delta_z)
    )

    beta_rhs = (
        1
        - delta_t * B / (delta_z ** 2)
        - r * delta_t / 2
    )

    gamma_rhs = (
        delta_t * B / (2 * delta_z ** 2)
        + delta_t * A / (4 * delta_z)
    )

    return (
        alpha,
        beta,
        gamma,
        alpha_rhs,
        beta_rhs,
        gamma_rhs
    )