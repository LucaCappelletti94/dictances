"""Return the mean absolute error beetween the given dictionaries."""

from typing import Dict
from dictances.distances_utils import mean
from dictances.total_variation import total_variation


def mae(a: Dict, b: Dict) -> float:
    """Return the mean absolute error beetween the given dictionaries.

    Parameters
    ----------------------------
    a: Dict,
        First dictionary to consider.
    b: Dict,
        Second dictionary to consider.

    Returns
    ----------------------------
    Return the mean absolute error beetween the given dictionaries.
    """
    return mean(a, b, total_variation)
