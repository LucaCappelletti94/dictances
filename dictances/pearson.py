"""Return the nth power distance beetween a and b."""
from math import sqrt
from typing import Dict

def pearson(a: Dict, b: Dict)->float:
    """Return the nth power distance beetween a and b."""
    bget = b.get

    ab = 0
    n_mul = 0
    a_sum = 0
    b_sum = 0
    a_sum2 = 0
    b_sum2 = 0

    for k, a_val in a.items():
        b_val = bget(k)
        a_sum += a_val
        a_sum2 += a_val**2
        if b_val:
            n_mul += 1
            ab += a_val * b_val

    for k, b_val in b.items():
        b_sum += b_val
        b_sum2 += b_val**2

    len_a = len(a)
    len_b = len(b)

    a_mean = a_sum / len_a
    b_mean = b_sum / len_b

    return 1 - (ab - n_mul * a_mean * b_mean) / (sqrt(a_sum2 - len_a * a_mean**2) * sqrt(b_sum2 - len_b * b_mean**2))
