"""Return the cosine distance beetween the given dictionaries."""
from math import sqrt
from typing import Dict

def cosine(a: Dict, b: Dict)->float:
    """Return the cosine distance beetween the given dictionaries.

    Parameters
    ----------------------------
    a: Dict,
        First dictionary to consider.
    b: Dict,
        Second dictionary to consider.

    Returns
    ----------------------------
    Return the cosine distance beetween the given dictionaries.
    """
    prod_ab = 0
    sqr_a = 0
    sqr_b = 0
    bget = b.__getitem__
    for k, a_val in a.items():
        sqr_a += a_val**2
        try:
            prod_ab += bget(k) * a_val
        except KeyError:
            pass

    for k, b_val in b.items():
        sqr_b += b_val**2

    return 1 - prod_ab / (sqrt(sqr_a) * sqrt(sqr_b))
