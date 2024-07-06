"""Return the mean total squared variation."""

from typing import Dict
from dictances.distances_utils import mean
from dictances.squared_variation import squared_variation


def mse(a: Dict, b: Dict) -> float:
    """Return the mean squared error beetween the given dictionaries.

    Parameters
    ----------------------------
    a: Dict,
        First dictionary to consider.
    b: Dict,
        Second dictionary to consider.

    Returns
    ----------------------------
    Return the mean squared error beetween the given dictionaries.
    """
    return mean(a, b, squared_variation)
