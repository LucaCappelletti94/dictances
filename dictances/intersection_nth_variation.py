"""Return the nth power distance beetween the insersection of a and b."""
from typing import Dict

def _even_nth(a_val: float, b_val: float)->float:
    return a_val - b_val


def _odd_nth(a_val: float, b_val: float)->float:
    return abs(a_val - b_val)


def intersection_nth_variation(a: Dict, b: Dict, exp: float=2, overlap: bool=False)->float:
    """Return the nth power distance beetween the insersection of a and b."""
    total = 0
    n = 0
    bget = b.__getitem__

    if exp % 2 == 0:
        nth = _even_nth
    else:
        nth = _odd_nth

    for k, a_val in a.items():
        try:
            total += nth(a_val, bget(k))**exp
            n += 1
        except KeyError:
            pass
    result = total
    if overlap:
        return result, n
    return result
