"""Return the jensen shannon divergence beetween a and b."""
from math import log

from .distances_utils import sort


def jensen_shannon(a: dict, b: dict)->float:
    """Return the jensen shannon divergence beetween a and b."""
    total = 0
    delta = 0
    big, small = sort(a, b)

    big_get = big.__getitem__

    for key, value in small.items():
        try:
            big_value = big_get(key)
            if big_value:
                denominator = (big_value + value) / 2
                total += value * log(value / denominator) + \
                    big_value * log(big_value / denominator)
                delta -= big_value
            else:
                delta += value
        except KeyError:
            delta += value

    total += (1 + delta) * log(2)
    return total / 2
