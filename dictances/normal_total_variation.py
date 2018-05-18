from .distances_utils import sort


def normal_total_variation(a: dict, b: dict) -> float:
    """Determines the Normalized Total Variation distance"""
    big, small = sort(a, b)
    big_get = big.get
    total = 2
    for k, small_value in small.items():
        big_value = big_get(k)
        if big_value:
            total += abs(big_value-small_value) - big_value - small_value
    return round(total/2, 14)
