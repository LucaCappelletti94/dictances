"""Determine the Kullback Leibler divergence."""
from math import log
from typing import Dict
from .distances_utils import sort


def kullback_leibler(a: Dict, b: Dict) -> float:
    """Determine the Kullback Leibler divergence."""
    total = 0
    big, small = sort(a, b)
    big_get = big.__getitem__
    for key, small_value in a.items():
        try:
            big_value = big_get(key)
            if big_value:
                total += small_value * log(small_value / big_value)
        except KeyError:
            pass

    return total
