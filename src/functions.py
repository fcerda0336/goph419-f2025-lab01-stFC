# functions.py
def sqrt(x, a):
    """
    Compute positive square root of x using Taylor/binomial series around base point a.

    Parameters
    ----------
    x : float
        Number to compute the square root of (0.0 <= x <= 2.5)
    a : float
        Base point for the Taylor expansion (0 < a <= 2.5)

    Returns
    -------
    y : float
        Approximation of sqrt(x) accurate to at least 8 significant figures
    """
    if x < 0.0 or x > 2.5:
        raise ValueError("x must be between 0.0 and 2.5")
    if a <= 0.0 or a > 2.5:
        raise ValueError("a must be between 0.0 and 2.5")

    h = x - a
    y = 0.0
    k = 0
    converged = False

    print(f"{'k':>2} | {'k!':>7} | {'prod_k':>10} | {'coef_k':>10} | {'term_k':>12} | {'sum_k':>12} | {'eps_k':>10}")
    print("-" * 80)

    while not converged:
        # factorial k
        if k == 0:
            fact_k = 1
        else:
            fact_k *= k  # running factorial

        # product prod_k = product of (0.5 - j) for j=0..k-1
        prod_k = 1.0
        for j in range(k):
            prod_k *= (0.5 - j)

        # coefficient
        coef_k = prod_k / fact_k

        # term
        term_k = coef_k * (h ** k) * (a ** (0.5 - k))

        # update running sum
        y += term_k
        sum_k = y

        # relative error estimate
        eps_k = abs(term_k) / abs(sum_k) if sum_k != 0 else abs(term_k)

        # print table row
        print(f"{k:2d} | {fact_k:7d} | {prod_k:10.6f} | {coef_k:10.6f} | {term_k:12.8f} | {sum_k:12.8f} | {eps_k:10.2e}")

        # check convergence (8 significant figures)
        if eps_k < 5e-9:
            converged = True

        k += 1

    return y


# Example usage
if __name__ == "__main__":
    x = float(input("Enter the value of x (0.0 to 2.5): "))
    a = float(input("Enter the base point a (0.0 < a <= 2.5): "))
    result = sqrt(x, a)
    print(f"\nApproximation of sqrt({x}) = {result:.10f}")
