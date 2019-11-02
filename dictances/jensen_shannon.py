"""Return the Jensen Shannon Divergence beetween the given dictionaries."""
from math import log
from typing import Dict
from .distances_utils import sort


def jensen_shannon(a: Dict, b: Dict)->float:
    """Return the Jensen Shannon divergence beetween the given dictionaries.

    Parameters
    ----------------------------
    a: Dict,
        First dictionary to consider.
    b: Dict,
        Second dictionary to consider.

    Returns
    ----------------------------
    Return the Jensen Shannon divergence beetween the given dictionaries.
    """
    total = 0
    delta = 0
    big, small = sort(a, b)

    big_get = big.__getitem__

    for key, small_value in small.items():
        try:
            big_value = big_get(key)
            if big_value:
                denominator = (big_value + small_value) / 2
                total += small_value * log(small_value / denominator) + \
                    big_value * log(big_value / denominator)
                delta += big_value + small_value
        except KeyError:
            pass

    total += (2 - delta) * log(2)
    return total / 2
