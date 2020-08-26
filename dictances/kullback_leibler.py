"""Determine the Kullback Leibler divergence beetween the given dictionaries."""
from math import log, inf
from typing import Dict
from .distances_utils import sort


def kullback_leibler(p: Dict, q: Dict) -> float:
    """Determine the Kullback Leibler divergence beetween the given dictionaries.

    Parameters
    ----------------------------
    p: Dict,
        First dictionary to consider.
    q: Dict,
        Second dictionary to consider.

    Returns
    ----------------------------
    Return the Kullback Leibler divergence beetween the given dictionaries.
    """
    total = 0
    overlap = 0
    _, small = sort(p, q)
    for key in small:
        try:
            total += p[key] * log(p[key] / q[key])
            overlap += 1
        except KeyError:
            pass

    if overlap == 0 and (len(p) != 0 or len(q) != 0):
        return inf
    return total
