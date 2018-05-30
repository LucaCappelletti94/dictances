"""Determine the Normalized Total Variation distance."""
from .distances_utils import sort


def normal_total_variation(a: dict, b: dict) -> float:
    """Determine the Normalized Total Variation distance."""
    big, small = sort(a, b)
    big_get = big.__getitem__
    total = 2
    for k, small_value in small.items():
        try:
            big_value = big_get(k)
            total += abs(big_value - small_value) - big_value - small_value
        except KeyError as e:
            pass
    return total / 2
