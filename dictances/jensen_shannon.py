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
            ov = big_get(key)
            denominator = (ov + value) / 2
            total += value * log(value / denominator) + \
                ov * log(ov / denominator)
            delta -= ov
        except KeyError:
            delta += value

    total += (1 + delta) * log(2)
    return total / 2
