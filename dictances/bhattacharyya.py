"""Determine the bhattacharyya distance beetween the given dictionaries."""
import numpy as np
from math import sqrt
from typing import Dict
from .distances_utils import sort


def bhattacharyya_coefficient(a: Dict, b: Dict) -> float:
    """Determine the Bhattacharyya coefficient beetween the given dictionaries.

    Parameters
    ----------------------------
    a: Dict,
        First dictionary to consider.
    b: Dict,
        Second dictionary to consider.

    Returns
    ----------------------------
    Return the Bhattacharyya coefficient beetween the given dictionaries.
    """
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
    """Determine the Bhattacharyya distance beetween the given dictionaries.

    Parameters
    ----------------------------
    a: Dict,
        First dictionary to consider.
    b: Dict,
        Second dictionary to consider.

    Returns
    ----------------------------
    Return the Bhattacharyya distance beetween the given dictionaries.
    """
    distance = -np.log(bhattacharyya_coefficient(a, b))
    if np.isinf(distance):
        return 0
    return distance