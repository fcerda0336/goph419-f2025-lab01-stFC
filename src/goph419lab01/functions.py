 # src/goph419lab01/functions.py

import math

def sqrt(x):
    """
    Approximate the positive square root of x using a Taylor series expansion.

    Parameters
    ----------
    x : float
        The input value (must be non-negative).

    Returns
    -------
    y : float
        Approximation of sqrt(x).
    """
    if x < 0:
        raise ValueError("sqrt(x) not defined for negative x")
    if x == 0:
        return 0.0

    # Choose expansion point near x for stability
    possible_a = [1, 2, 4, 9, 16]
    a = min(possible_a, key=lambda k: abs(x - k))

    # Derivatives of sqrt at a
    f_a = math.sqrt(a)
    fprime_a = 1 / (2 * f_a)
    f2prime_a = -1 / (4 * a ** (3/2))
    f3prime_a = 3 / (8 * a ** (5/2))

    dx = x - a
    y = (f_a
         + fprime_a * dx
         + (f2prime_a / 2) * dx ** 2
         + (f3prime_a / 6) * dx ** 3)
    return y


def arcsin(x):
    """
    Approximate arcsin(x) using a Taylor series expansion around x=0.

    Parameters
    ----------
    x : float
        Input value, must be in [-1, 1].

    Returns
    -------
    y : float
        Approximation of arcsin(x) in radians.
    """
    if abs(x) > 1:
        raise ValueError("arcsin(x) not defined for |x| > 1")

    # 4-term Taylor series expansion around 0
    y = (x
         + (x**3) / 6
         + (3 * x**5) / 40
         + (5 * x**7) / 112)
    return y


def launch_angle_range(ve_v0, alpha, tol_alpha):
    """
    Compute the minimum and maximum launch angles for given parameters.

    Equation (17)-based approach.

    Parameters
    ----------
    ve_v0 : float
        Velocity ratio.
    alpha : float
        Parameter alpha.
    tol_alpha : float
        Allowed tolerance on alpha.

    Returns
    -------
    (min_angle, max_angle) : tuple of floats
        The angle range in radians.
    """
    alphamin = alpha*(1 + tol_alpha)
    alphamax = alpha*(1 - tol_alpha)
    inside_sqrtmin = 1 - (alphamin/(1+alphamin))*(ve_v0 ** 2)
    inside_sqrtmax = 1 - (alphamax/(1+alphamax))*(ve_v0 ** 2)
    if inside_sqrtmin < 0:
        raise ValueError("Square root argument negative — invalid parameters.")
    if inside_sqrtmax < 0:
        raise ValueError("Square root argument negative — invalid parameters.")

    sin_phimin = (1+alphamin)*sqrt(inside_sqrtmin)
    sin_phimax = (1+alphamax)*sqrt(inside_sqrtmax)
    phimin = arcsin(sin_phimin)
    phimax = arcsin(sin_phimax)
    

    return (phimin, phimax)