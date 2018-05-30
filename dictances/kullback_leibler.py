"""Determine the Kullback Leibler divergence."""
from math import log

from .distances_utils import sort


def kullback_leibler(a: dict, b: dict) -> float:
    """Determine the Kullback Leibler divergence."""
    total = 0
    big, small = sort(a, b)
    big_get = big.__getitem__
    for key, small_value in a.items():
        try:
            bvalue = big_get(key)
            if bvalue:
                total += small_value * log(small_value / big_get(key))
        except KeyError:
            pass

    return total
