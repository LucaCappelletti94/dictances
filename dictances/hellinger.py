"""Determine the Hellinger distance."""
from math import sqrt

from .distances_utils import sort


def hellinger(a: dict, b: dict) -> float:
    """Determine the Hellinger distance."""
    total = 0
    big, small = sort(a, b)
    big_get = big.__getitem__
    for key, small_value in small.items():
        try:
            total += (sqrt(small_value) - sqrt(big_get(key)))**2
        except KeyError:
            pass
    return sqrt(total) / sqrt(2)
