"""Return the mean absolute error beetween the given dictionaries."""
from .distances_utils import mean
from .total_variation import total_variation
from typing import Dict


def mae(a:Dict, b:Dict)->float:
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
