"""Determine the bhattacharyya distance."""
from math import log, sqrt
from typing import Dict
from .distances_utils import sort


def bhattacharyya_coefficient(a: Dict, b: Dict) -> float:
    """Determine the bhattacharyya coefficient."""
    total = 0
    big, small = sort(a, b)
    big_get = big.__getitem__
    for k, small_value in small.items():
        try:
            total += sqrt(big_get(k) * small_value)
        except KeyError:
            pass
    return total


def bhattacharyya(a: Dict, b: Dict) -> float:
    """Determine the bhattacharyya distance."""
    return -log(bhattacharyya_coefficient(a, b))
