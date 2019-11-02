"""Return the nth power distance beetween the given dictionaries."""
from typing import Dict


def _even_nth(a_val: float, b_val: float) -> float:
    return a_val - b_val


def _odd_nth(a_val: float, b_val: float) -> float:
    return abs(a_val - b_val)


def nth_variation(a: Dict, b: Dict, exp: float = 2, overlap: bool = False) -> float:
    """Return the nth power distance beetween the given dictionaries.

    Parameters
    ----------------------------
    a: Dict,
        First dictionary to consider.
    b: Dict,
        Second dictionary to consider.
    exp: float,
        The exponent for the nth power distance.
    overlap: bool,
        Whetever to return or not the overlap number.

    Returns
    ----------------------------
    Return the nth power distance distance beetween the given dictionaries.
    """
    total = 0
    n = 0
    bget = b.__getitem__
    aget = a.__getitem__

    if exp % 2 == 0:
        nth = _even_nth
    else:
        nth = _odd_nth

    for k, a_val in a.items():
        try:
            total += nth(a_val, bget(k))**exp
        except KeyError:
            total += a_val**exp
        n += 1
    for k, b_val in b.items():
        try:
            aget(k)
        except KeyError:
            total += b_val**exp
            n += 1
    result = total
    if overlap:
        return result, n
    return result
