"""Return the canberra distance beetween the given dictionaries."""
from typing import Dict


def canberra(a: Dict, b: Dict) -> float:
    """Return the canberra distance beetween the given dictionaries.

    Parameters
    ----------------------------
    a: Dict,
        First dictionary to consider.
    b: Dict,
        Second dictionary to consider.

    Returns
    ----------------------------
    Return the canberra distance beetween the given dictionaries.
    """
    total = 0
    bget = b.__getitem__
    aget = a.__getitem__
    for k, aval in a.items():
        try:
            bval = bget(k)
            total += abs(aval - bval) / (aval + bval)
        except KeyError:
            total += 1
    for k in b:
        try:
            aget(k)
        except KeyError:
            total += 1
    return total
