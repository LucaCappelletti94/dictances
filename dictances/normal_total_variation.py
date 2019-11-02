"""Determine the normalized total variation distance beetween the given dictionaries."""
from .distances_utils import sort
from typing import Dict


def normal_total_variation(a: Dict, b: Dict) -> float:
    """Determine the normalized total variation distance beetween the given dictionaries.
    
    Parameters
    ----------------------------
    a: Dict,
        First dictionary to consider.
    b: Dict,
        Second dictionary to consider.

    Returns
    ----------------------------
    Return the normalized total variation beetween the given dictionaries.
    """
    big, small = sort(a, b)
    big_get = big.__getitem__
    total = 2
    for k, small_value in small.items():
        try:
            big_value = big_get(k)
            if big_value:
                total += abs(big_value - small_value) - big_value - small_value
        except KeyError:
            pass
    return total / 2
