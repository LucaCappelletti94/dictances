"""Return the cosine distance beetween a and b."""
from math import sqrt


def cosine(a: dict, b: dict)->float:
    """Return the cosine distance beetween a and b."""
    prod_ab = 0
    sqr_a = 0
    sqr_b = 0
    bget = b.__getitem__
    for k, a_val in a.items():
        sqr_a += a_val**2
        try:
            prod_ab += bget(k) * a_val
        except Exception as e:
            pass

    for k, b_val in b.items():
        sqr_b += b_val**2

    return 1 - prod_ab / (sqrt(sqr_a) * sqrt(sqr_b))
