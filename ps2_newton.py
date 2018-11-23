# 6.00 Problem Set 2

# Successive Approximation

def evaluate_poly(poly, x):
    ##assert type(poly)== tuple and len(poly)>0
    ##assert type(x) == float and type(epsilon) == float
    result = 0
    for i in range(len(poly)):
        result += x**float(i)*poly[i]
    return result

def compute_eval_deriv(poly, x):
    ##assert type(poly)== tuple and len(poly)>0
    poly_computed = ()
    for i in range(1, len(poly)):
        poly_computed += (poly[i]*i,)
    return evaluate_poly(poly_computed, x)

def compute_root(poly, x, epsilon):
    num_iter=1
    result = evaluate_poly(poly, x)
    while result < -epsilon or result > 1.1*epsilon:
        num_iter += 1
        x -= result/compute_eval_deriv(poly, x)
        result = evaluate_poly(poly, x)
    return (x, num_iter)

##poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
##x = 0.1
##poly = (4, 4, 1)
##x = -1.89
poly = (0.0625, -0.5, 1)
x = 0.20
epsilon = 0.0001
print(compute_root(poly, x, epsilon))

"""
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """


##multiplication function without using "*"

##def rec_multiplication(m, n):
##    if n == 0 or m == 0:
##        return 0
##    elif n>0:
##        m, n = m, n
##    elif n < 0:
##        m, n = -m, -n
##    return m + rec_multiplication(m, n-1)


