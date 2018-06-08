"""Determine the Squared Hellinger distance."""
from math import sqrt

from .distances_utils import sort


def squared_hellinger(a: dict, b: dict) -> float:
    """Determine the Squared Hellinger distance."""
    total = 1
    big, small = sort(a, b)
    big_get = big.__getitem__
    for key, small_value in small.items():
        try:
            total -= sqrt(small_value * big_get(key))
        except KeyError:
            pass
    return total
