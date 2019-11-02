"""Generic utils used through all the package."""
from typing import Dict

def sort(a: Dict, b: Dict):
    """Return the bigger dict, then the smaller one."""
    if len(a) > len(b):
        return a, b
    return b, a


def mean(a, b, distance):
    """Return the mean of the given distance."""
    result, n = distance(a, b, overlap=True)
    return result / n