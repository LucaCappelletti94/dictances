"""Determine the Kullback Leibler divergence beetween the given dictionaries."""
from math import log, inf
from typing import Dict
from .distances_utils import sort


def kullback_leibler(a: Dict, b: Dict) -> float:
    """Determine the Kullback Leibler divergence beetween the given dictionaries.

    Parameters
    ----------------------------
    a: Dict,
        First dictionary to consider.
    b: Dict,
        Second dictionary to consider.

    Returns
    ----------------------------
    Return the Kullback Leibler divergence beetween the given dictionaries.
    """
    total = 0
    overlap = 0
    big, small = sort(a, b)
    big_get = big.__getitem__
    for key, small_value in small.items():
        try:
            total += small_value * log(small_value / big_get(key))
            overlap += 1
        except KeyError:
            pass
    
    if overlap == 0 and (len(a) != 0 or len(b) != 0):
        return inf
    return total
