from math import comb
"""
n -> group number
r -> sub group number
p -> probability
* pascal == negative binomial.
"""
# Term


def binomial_term(n: int, r: int, p: float) -> float:
    return comb(n, r) * pow(p, r) * pow((1 - p), (n-r))


def geometrical_term(n: int, p: float) -> float:
    return p * pow((1-p), n-1)


def pascal_term(n: int, r: int, p: float) -> float:
    return comb(n-1, r-1) * pow(p, r) * pow((1 - p), n-r)

# Population parameter


def binomial_desviation(n, p) -> float:
    return n * p * (1-p)


def binomial_media(n, p) -> float:
    return n * p


def geometrical_media(p) -> float:
    return 1 / p


def geometrical_dedsviation(p) -> float:
    return (1 - p) / pow(p, 2)


def pascal_media(r, p) -> float:
    return r / p


def pascal_desviation(r, p) -> float:
    return r * (1-p) / pow(p, 2)
