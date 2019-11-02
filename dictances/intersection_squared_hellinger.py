"""Determine the Intersection Squared Hellinger distance."""
from math import sqrt
from typing import Dict
from .distances_utils import sort


def intersection_squared_hellinger(a: Dict, b: Dict) -> float:
    """Determine the Intersection Squared Hellinger distance."""
    total = 0
    big, small = sort(a, b)
    big_get = big.__getitem__
    for key, small_value in small.items():
        try:
            total += (sqrt(small_value) - sqrt(big_get(key)))**2
        except KeyError:
            pass
    return total
